#include <stdlib.h>
#include <string.h>
#include "log/log.h"
#include "mq.h"

static void messageConsumer(MQHCONN   hConn,
        MQMD    * pMsgDesc,
        MQGMO   * pGetMsgOpts,
        MQBYTE  * Buffer,
        MQCBC   * pContext);

MQMESSAGE *gBuffer;
int bufferCount = 0;

MQCHAR QMgrName[MQ_Q_MGR_NAME_LENGTH];   /* queue manager name            */
MQCNO   cno = {MQCNO_DEFAULT};                /* connection description        */
MQCD     cd = {MQCD_CLIENT_CONN_DEFAULT};     /* client connection description */
MQOD     od = {MQOD_DEFAULT};                 /* object description            */
MQMD     md = {MQMD_DEFAULT};                 /* message description           */
MQGMO   gmo = {MQGMO_DEFAULT};                /* get message options           */
MQCBD   cbd = {MQCBD_DEFAULT};                /* callback description          */
MQCTLO ctlo = {MQCTLO_DEFAULT};               /* control options               */

MQLONG o_options;             /* MQOPEN options                */
MQCHAR channelName[MQ_CHANNEL_NAME_LENGTH];
MQCHAR queueName[MQ_Q_NAME_LENGTH];
MQCHAR connectionName[MQ_CONN_NAME_LENGTH];
MQLONG ccsid = MQENC_NATIVE;

pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condc = PTHREAD_COND_INITIALIZER;  /* consumer condition variable */
pthread_cond_t condp = PTHREAD_COND_INITIALIZER;  /* producer condition variable */

void freeBuffer()
{
    if (gBuffer != NULL)
        free(gBuffer);
}

void startGetMessage()
{
    gBuffer = (MQMESSAGE *) malloc(sizeof(MQMESSAGE) * BUFFER_SIZE);
    strncpy(cd.ConnectionName, connectionName, MQ_CONN_NAME_LENGTH);
    strncpy(cd.ChannelName, channelName, MQ_CHANNEL_NAME_LENGTH);
    strncpy(od.ObjectName, queueName, MQ_Q_NAME_LENGTH);

    cd.DefReconnect = MQRCN_YES;      /* client automatically reconnection */
    cno.Options |= MQCNO_RECONNECT;  /* reconnect */
    cno.ClientConnPtr = &cd;
    cno.Version = MQCNO_VERSION_2;   /* client connection set version 2 */

    cbd.CallbackFunction = messageConsumer;
    gmo.Options = MQGMO_NO_SYNCPOINT;

    o_options = MQOO_INPUT_AS_Q_DEF      /* open queue for input      */
              | MQOO_FAIL_IF_QUIESCING;  /* but not if MQM stopping   */

    MQHCONN hcon = MQHC_UNUSABLE_HCONN;
    MQHOBJ hobj;
    MQLONG compCode;
    MQLONG reasCode;

    MQCONNX(QMgrName,              /* queue manager          */
            &cno,                  /* connection options     */
            &hcon,                 /* connection handle      */
            &compCode,             /* completion code        */
            &reasCode);            /* reason code            */

    if (compCode == MQCC_FAILED) {
        log_error("MQCONNX ended with reason code %d", reasCode);
        exit(reasCode);
    }

    MQOPEN(hcon,                    /* connection handle            */
           &od,                     /* object descriptor for queue  */
           o_options,               /* open options                 */
           &hobj,                   /* object handle                */
           &compCode,               /* completion code              */
           &reasCode);              /* reason code                  */

    if (compCode == MQCC_FAILED) {
        log_error("MQOPEN of '%.48s' ended with reason code %d",
                &od.ObjectName, reasCode);
        exit(reasCode);
    }

    /****************************************************************/
    /*                                                              */
    /*   Register a consumer                                        */
    /*                                                              */
    /****************************************************************/

    md.Encoding = ccsid;
    MQCB(hcon,
            MQOP_REGISTER,
            &cbd,
            hobj,
            &md,
            &gmo,
            &compCode,
            &reasCode);
    if (compCode == MQCC_FAILED) {
        log_error("MQCB ended with reason code %d", reasCode);
        exit(reasCode);
    }

    /******************************************************************/
    /*                                                                */
    /*  Start consumption of messages                                 */
    /*                                                                */
    /******************************************************************/
    MQCTL(hcon,
            MQOP_START,
            &ctlo,
            &compCode,
            &reasCode);
    if (compCode == MQCC_FAILED) {
        log_error("MQCTL ended with reason code %d", reasCode);
        exit(reasCode);
    }
}

/********************************************************************/
/* FUNCTION: messageConsumer                                        */
/* PURPOSE : Callback function called when messages arrive          */
/********************************************************************/
static void messageConsumer(MQHCONN   hConn,
        MQMD    * pMsgDesc,
        MQGMO   * pGetMsgOpts,
        MQBYTE  * Buffer,
        MQCBC   * pContext)
{
    MQLONG i,max;
    MQLONG length;
    pthread_t tid = pthread_self();

    switch(pContext->CallType)
    {
        case MQCBCT_MSG_REMOVED:
        case MQCBCT_MSG_NOT_REMOVED:
            length = pGetMsgOpts -> ReturnedLength;
            if (pContext->Reason)
                log_info("tid: %u Message Call (%d Bytes) : Reason = %d", (unsigned int)tid, length, pContext->Reason);
            else
                log_info("tid: %u Message Call (%d Bytes) :", (unsigned int)tid, length);

            pthread_mutex_lock(&mtx);
            while (bufferCount == BUFFER_SIZE)
                pthread_cond_wait(&condp, &mtx);

            gBuffer[bufferCount].size = length;
            gBuffer[bufferCount].data = (MQBYTE *) malloc(sizeof(MQBYTE) * (length + 1));
            memcpy(gBuffer[bufferCount].data, Buffer, length);
            gBuffer[bufferCount].data[length] = '\0';
            bufferCount++;

            if (bufferCount > 0)
                pthread_cond_signal(&condc);

            pthread_mutex_unlock(&mtx);
            break;

        case MQCBCT_EVENT_CALL:
            log_error("Event Call : Reason = %d",pContext->Reason);
            break;

        default:
            log_error("Calltype = %d",pContext->CallType);
            break;

    }
}
