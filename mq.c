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
MQGMO   gmo = {MQGMO_DEFAULT};                /* get message options           */
MQCBD   cbd = {MQCBD_DEFAULT};                /* callback description          */
MQCTLO ctlo = {MQCTLO_DEFAULT};               /* control options               */

MQLONG o_options;             /* MQOPEN options                */
MQCHAR channelName[MQ_CHANNEL_NAME_LENGTH];
MQCHAR queueName[MQ_Q_NAME_LENGTH];
MQCHAR connectionName[MQ_CONN_NAME_LENGTH];
MQLONG ccsid = MQENC_NATIVE;
MQHCONN *phcon;

pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condc = PTHREAD_COND_INITIALIZER;  /* consumer condition variable */
pthread_cond_t condp = PTHREAD_COND_INITIALIZER;  /* producer condition variable */

QueuePtr hconnQueue = NULL;
MQHOBJ_QUEUE_PTR hobjQueueQueue = NULL;

int getMessageThreadCount = 1;
int hobjQueueSize = 0;

static pthread_key_t hconnKey;

static void freeBuffer();
static void freeHcon();
/* static void enHconnQueue(MQHCONN hConn, int qmId); */
/* static void initConnQueue(); */
/* static void initHobjQueue(); */
/* static void enHobjQueue(const char *queueName, MQHOBJ hobj, MQHOBJ *phobj); */
static MQHCONN getConnection();
static void freeThreadConnection(void *phconn);

void clean()
{
    freeBuffer();
    freeHcon();
    if (hconnQueue != NULL)
        DestroyQueue(hconnQueue, dataHandle);
}

static void freeBuffer()
{
    if (gBuffer != NULL)
        free(gBuffer);
}

static void freeHcon()
{
    if (phcon != NULL) {
        MQLONG compCode;
        MQLONG reasCode;
        for (int i = 0; i < getMessageThreadCount; i++) {
            MQDISC(phcon + i, &compCode, &reasCode);
            if (compCode == MQCC_FAILED) {
                log_error("MQDISC failed.");
            } else {
                log_info("MQDISC successful.");
            }
        }
        /* MQHCONN_DATA_PTR hconnPtr = NULL; */
        /* ElementPtr elementPtr = NULL; */
        /* while ((elementPtr = DeQueue(hconnQueue)) != NULL) { */
        /*     hconnPtr = (MQHCONN_DATA_PTR)elementPtr->data; */
        /*     MQDISC(&hconnPtr->hConn, &compCode, &reasCode); */
        /*     if (compCode == MQCC_FAILED) { */
        /*         log_error("hconnPtr: %p MQDISC failed.", hconnPtr); */
        /*     } else { */
        /*         log_info(" hconnPtr: %p MQDISC successful.", hconnPtr); */
        /*     } */
        /*     free(hconnPtr); */
        /*     free(elementPtr); */
        /* } */
        free(phcon);
    }
}

static void freeThreadConnection(void *phconn)
{
    if (phconn != NULL) {
        MQLONG compCode;
        MQLONG reasCode;
        MQDISC(phconn, &compCode, &reasCode);
        if (compCode == MQCC_FAILED) {
            log_error("free thread connection MQDISC failed.");
        } else {
            log_info("free thread connection %p MQDISC successful.", phconn);
        }
        free(phconn);
    }
}

void startGetMessage()
{
    gBuffer = (MQMESSAGE *) malloc(sizeof(MQMESSAGE) * BUFFER_SIZE);
    /* initConnQueue(); */
    pthread_key_create(&hconnKey, freeThreadConnection);
    /* initHobjQueue(); */


    cbd.CallbackFunction = messageConsumer;
    gmo.Options = MQGMO_NO_SYNCPOINT;

    o_options = MQOO_INPUT_AS_Q_DEF      /* open queue for input      */
              | MQOO_FAIL_IF_QUIESCING;  /* but not if MQM stopping   */

    log_info("getMessageThreadCount is: %d", getMessageThreadCount);
    phcon = (MQHCONN *) malloc(sizeof(MQHCONN *) * getMessageThreadCount);
    if (phcon == NULL) {
        log_error("malloc error.");
        exit(1);
    }
    for (int i = 0; i < getMessageThreadCount; i++) {
        MQCNO   cno = {MQCNO_DEFAULT};                /* connection description        */
        MQCD     cd = {MQCD_CLIENT_CONN_DEFAULT};     /* client connection description */

        strncpy(cd.ConnectionName, connectionName, MQ_CONN_NAME_LENGTH);
        strncpy(cd.ChannelName, channelName, MQ_CHANNEL_NAME_LENGTH);
        cd.DefReconnect = MQRCN_YES;      /* client automatically reconnection */

        cno.Options |= MQCNO_RECONNECT;  /* reconnect */
        cno.Options |= MQCNO_HANDLE_SHARE_BLOCK;
        cno.ClientConnPtr = &cd;
        cno.Version = MQCNO_VERSION_2;   /* client connection set version 2 */

        MQOD     od = {MQOD_DEFAULT};                 /* object description            */
        strncpy(od.ObjectName, queueName, MQ_Q_NAME_LENGTH);
        MQMD     md = {MQMD_DEFAULT};                 /* message description           */

        MQHCONN *hcon = phcon + i;
        log_info("hcon %p", hcon);

        MQHOBJ hobj;
        MQLONG compCode;
        MQLONG reasCode;

        MQCONNX(QMgrName,              /* queue manager          */
                &cno,                  /* connection options     */
                hcon,                  /* connection handle      */
                &compCode,             /* completion code        */
                &reasCode);            /* reason code            */

        if (compCode == MQCC_FAILED) {
            log_error("MQCONNX ended with reason code %d", reasCode);
            exit(reasCode);
        }

        MQOPEN(*hcon,                    /* connection handle            */
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
        MQCB(*hcon,
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
        MQCTL(*hcon,
                MQOP_START,
                &ctlo,
                &compCode,
                &reasCode);
        if (compCode == MQCC_FAILED) {
            log_error("MQCTL ended with reason code %d", reasCode);
            exit(reasCode);
        }
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
            log_error("tid: %u Event Call : Reason = %d", (unsigned int) tid, pContext->Reason);
            break;

        default:
            log_error("tid: %u Calltype = %d", (unsigned int) tid, pContext->CallType);
            break;

    }
}

/* static void initConnQueue() */
/* { */
/*     hconnQueue = InitQueue(); */
/*     if (hconnQueue == NULL) { */
/*         log_error("init queue error."); */
/*         exit(1); */
/*     } */

/*     cbd.CallbackFunction = messageConsumer; */
/*     gmo.Options = MQGMO_NO_SYNCPOINT; */

/*     o_options = MQOO_INPUT_AS_Q_DEF      /1* open queue for input      *1/ */
/*               | MQOO_FAIL_IF_QUIESCING;  /1* but not if MQM stopping   *1/ */

/*     log_info("workThreadCount is: %d", workThreadCount); */
/*     int hconnQueueSize = (int)(workThreadCount * 1.25); */
/*     log_info("hconnQueueSize is: %d", hconnQueueSize); */
/*     for (int i = 0; i < hconnQueueSize; i++) { */
/*         MQCNO   cno = {MQCNO_DEFAULT};                /1* connection description        *1/ */
/*         MQCD     cd = {MQCD_CLIENT_CONN_DEFAULT};     /1* client connection description *1/ */

/*         strncpy(cd.ConnectionName, connectionName, MQ_CONN_NAME_LENGTH); */
/*         strncpy(cd.ChannelName, channelName, MQ_CHANNEL_NAME_LENGTH); */
/*         cd.DefReconnect = MQRCN_YES;      /1* client automatically reconnection *1/ */

/*         cno.Options |= MQCNO_RECONNECT;  /1* reconnect *1/ */
/*         cno.Options |= MQCNO_HANDLE_SHARE_BLOCK; */
/*         cno.ClientConnPtr = &cd; */
/*         cno.Version = MQCNO_VERSION_2;   /1* client connection set version 2 *1/ */

/*         MQOD     od = {MQOD_DEFAULT};                 /1* object description            *1/ */
/*         strncpy(od.ObjectName, queueName, MQ_Q_NAME_LENGTH); */

/*         MQHCONN *hcon = (MQHCONN *) malloc(sizeof(MQHCONN)); */
/*         log_info("hcon %p", hcon); */

/*         MQLONG compCode; */
/*         MQLONG reasCode; */

/*         MQCONNX(QMgrName,              /1* queue manager          *1/ */
/*                 &cno,                  /1* connection options     *1/ */
/*                 hcon,                  /1* connection handle      *1/ */
/*                 &compCode,             /1* completion code        *1/ */
/*                 &reasCode);            /1* reason code            *1/ */

/*         if (compCode == MQCC_FAILED) { */
/*             log_error("MQCONNX ended with reason code %d", reasCode); */
/*             exit(reasCode); */
/*         } */
/*         enHconnQueue(*hcon, 0); */
/*     } */
/* } */

int setThreadConnection()
{
    MQHCONN *phconn = (MQHCONN *)malloc(sizeof(MQHCONN));
    if (phconn == NULL) {
        log_error("malloc phconn error.");
        return -1;
    }

    *phconn = getConnection();
    if (*phconn == -1) {
        log_error("get connection error.");
        free(phconn);
        return -1;
    }

    if (pthread_setspecific(hconnKey, phconn) != 0) {
        log_error("setspecific error.");
        free(phconn);
        return -1;
    }

    log_info("setspecific connection successful.");
    return 0;
}

MQHCONN getThreadConnection()
{
    MQHCONN result;
    MQHCONN *phconn = (MQHCONN *)pthread_getspecific(hconnKey);
    if (phconn != NULL) {
        log_info("getspecific connection successful.");
        result = *phconn;
    } else {
        log_error("no found specific connection.");
        result = getConnection();
    }

    return result;
}

static MQHCONN getConnection()
{
    MQCNO   cno = {MQCNO_DEFAULT};                /* connection description        */
    MQCD     cd = {MQCD_CLIENT_CONN_DEFAULT};     /* client connection description */

    strncpy(cd.ConnectionName, connectionName, MQ_CONN_NAME_LENGTH);
    strncpy(cd.ChannelName, channelName, MQ_CHANNEL_NAME_LENGTH);
    cd.DefReconnect = MQRCN_YES;      /* client automatically reconnection */

    cno.Options |= MQCNO_RECONNECT;  /* reconnect */
    cno.Options |= MQCNO_HANDLE_SHARE_BLOCK;
    cno.ClientConnPtr = &cd;
    cno.Version = MQCNO_VERSION_2;   /* client connection set version 2 */

    MQHCONN hcon;

    MQLONG compCode;
    MQLONG reasCode;

    MQCONNX(QMgrName,              /* queue manager          */
            &cno,                  /* connection options     */
            &hcon,                  /* connection handle      */
            &compCode,             /* completion code        */
            &reasCode);            /* reason code            */

    if (compCode == MQCC_FAILED) {
        log_error("getConnection MQCONNX ended with reason code %d", reasCode);
        return -1;
    }

    return hcon;
}


/* static void enHconnQueue(MQHCONN hConn, int qmId) */
/* { */
/*     MQHCONN_DATA_PTR hconnPtr = (MQHCONN_DATA_PTR)malloc(sizeof(MQHCONN_DATA)); */
/*     if (hconnPtr == NULL) { */
/*         log_error("malloc hconnptr error."); */
/*         exit(1); */
/*     } */
/*     hconnPtr->qmId = 0; */
/*     hconnPtr->hConn = hConn; */
/*     ElementPtr elementPtr = (ElementPtr)malloc(sizeof(Element)); */
/*     if (elementPtr == NULL) { */
/*         log_error("malloc elementPtr error."); */
/*         exit(1); */
/*     } */
/*     elementPtr->data = (data_t)hconnPtr; */
/*     elementPtr->next = NULL; */
/*     EnQueue(hconnQueue, elementPtr); */
/* } */

void dataHandle(void *data)
{
    if (data == NULL)
        return;
    MQLONG compCode;
    MQLONG reasCode;
    MQHCONN_DATA_PTR hconnPtr = (MQHCONN_DATA_PTR)data;
    MQDISC(&hconnPtr->hConn, &compCode, &reasCode);
    if (compCode == MQCC_FAILED) {
        log_error("datahandle hconnPtr: %p MQDISC failed.", hconnPtr);
    } else {
        log_info("dataHandle hconnPtr: %p MQDISC successful.", hconnPtr);
    }
    free(hconnPtr);
}

int sendMessageToQueue(const MQMESSAGE *message, const char *queue)
{
    MQMD     md = {MQMD_DEFAULT};                 /* message description           */
    MQPMO   pmo = {MQPMO_DEFAULT};                /* put message options           */
    MQOD     od = {MQOD_DEFAULT};                 /* object description            */
    strncpy(od.ObjectName, queue, MQ_Q_NAME_LENGTH);
    MQLONG out_options = MQOO_OUTPUT | MQOO_FAIL_IF_QUIESCING;      /* MQOPEN options                */
    MQLONG close_options = MQCO_NONE;
    MQHOBJ hobj;
    /* MQHOBJ *hobjPtr = NULL; */
    MQLONG compCode;
    MQLONG reasCode;
    MQHCONN hconn = getThreadConnection();

    /* MQHCONN_DATA_PTR hconnPtr = NULL; */
    /* ElementPtr elementPtr = NULL; */
    /* while ((elementPtr = DeQueue(hconnQueue)) != NULL) { */
    /*     hconnPtr = (MQHCONN_DATA_PTR)elementPtr->data; */
    /*     log_info("sendMessageToQueue hconnPtr: %p, hconn: %ld, hconnQueue size: %d", hconnPtr, hconnPtr->hConn, Size(hconnQueue)); */
    /*     break; */
    /* } */

    /* if (getHobjByQueueName(queue, &hobjPtr) == -1) { */
        MQOPEN(hconn,          /* connection handle            */
                &od,                     /* object descriptor for queue  */
                out_options,             /* open options                 */
                &hobj,                   /* object handle                */
                &compCode,               /* completion code              */
                &reasCode);              /* reason code                  */

        if (compCode == MQCC_FAILED) {
            log_error("MQOPEN of '%.48s' ended with reason code %d",
                    &od.ObjectName, reasCode);
            /* EnQueue(hconnQueue, elementPtr); */
            return -1;
        }
    /* } else { */
    /*     hobj = *hobjPtr; */
    /* } */

    memcpy(md.Format, MQFMT_STRING, (size_t)MQ_FORMAT_LENGTH);  /* character string format */
    memcpy(md.MsgId, MQMI_NONE, sizeof(md.MsgId));  /* reset MsgId to get a new one. */
    md.Encoding = ccsid;
    pmo.Options = MQPMO_NO_SYNCPOINT | MQPMO_FAIL_IF_QUIESCING;  /* put message options */

    MQPUT(hconn,               /* connection handle             */
            hobj,                        /* object handle                 */
            &md,                         /* message descriptor            */
            &pmo,                        /* put message options (datagram)*/
            message->size,               /* message length                */
            message->data,               /* message buffer                */
            &compCode,                   /* completion code               */
            &reasCode                    /* reason code                   */
         );

    if (compCode == MQCC_FAILED) {
        log_error("MQPUT of '%.48s' ended with reason code %d",
                &od.ObjectName, reasCode);
        /* if (hobjPtr == NULL) { */
        /*     enHobjQueue(queue, hobj, NULL); */
        /* } else { */
        /*     enHobjQueue(queue, hobj, hobjPtr); */
        /* } */
        MQCLOSE(hconn,       /* connection handle    */
                &hobj,                 /* object handle        */
                close_options,         /* close options        */
                &compCode,             /* completion code      */
                &reasCode);            /* reason code          */
        if (compCode == MQCC_FAILED) {
            log_error("MQCLOSE of '%.48s' ended with reason code %d",
                    &od.ObjectName, reasCode);
        } else {
            log_info("close queue %s successful.", queue);
        }
        /* EnQueue(hconnQueue, elementPtr); */
        return -1;
    }
    log_info("send message to queue %s successful.", queue);

    /* if (hobjPtr == NULL) { */
    /*     enHobjQueue(queue, hobj, NULL); */
    /* } else { */
    /*     enHobjQueue(queue, hobj, hobjPtr); */
    /* } */
    MQCLOSE(hconn,       /* connection handle    */
            &hobj,                 /* object handle        */
            close_options,         /* close options        */
            &compCode,             /* completion code      */
            &reasCode);            /* reason code          */
    if (compCode == MQCC_FAILED) {
        log_error("MQCLOSE of '%.48s' ended with reason code %d",
                &od.ObjectName, reasCode);
    } else {
        log_info("close queue %s successful.", queue);
    }
    /* EnQueue(hconnQueue, elementPtr); */
    /* log_info("sendMessageToQueue hconnQueue size: %d", Size(hconnQueue)); */
    return 0;
}

/* static void initHobjQueue() */
/* { */
/*     if (dxpIdDistributionSize > 0) { */
/*         if (strlen(defaultTarget.queue) > 0) { */
/*             hobjQueueSize = dxpIdDistributionSize + 1; */
/*         } else { */
/*             hobjQueueSize = dxpIdDistributionSize; */
/*         } */
/*     } else { */
/*         if (strlen(defaultTarget.queue) > 0) { */
/*             hobjQueueSize = 1; */
/*         } */
/*     } */
/*     if (hobjQueueSize <= 0) */
/*         return; */

/*     hobjQueueQueue = (MQHOBJ_QUEUE_PTR)malloc(sizeof(MQHOBJ_QUEUE) * hobjQueueSize); */

/*     if (hobjQueueQueue == NULL) { */
/*         log_error("init hobj queue error."); */
/*         exit(1); */
/*     } */
/*     for (int i = 0; i < dxpIdDistributionSize; i++) { */
/*         log_info("[%d] dxpIdDistribution dxpId: %s", i, dxpIdDistributions[i].dxpId); */
/*         log_info("[%d] dxpIdDistribution qmId: %d", i, dxpIdDistributions[i].qmId); */
/*         log_info("[%d] dxpIdDistribution queue: %s", i, dxpIdDistributions[i].queue); */
/*         hobjQueueQueue[i].hobjQueue = InitQueue(); */
/*         if (hobjQueueQueue[i].hobjQueue == NULL) { */
/*             log_error("dxp init hobj queue error."); */
/*             exit(1); */
/*         } */
/*         strncpy(hobjQueueQueue[i].queueName, dxpIdDistributions[i].queue, MQ_Q_NAME_LENGTH); */
/*     } */

/*     if (strlen(defaultTarget.queue) > 0) { */
/*         hobjQueueQueue[dxpIdDistributionSize].hobjQueue = InitQueue(); */
/*         if (hobjQueueQueue[dxpIdDistributionSize].hobjQueue == NULL) { */
/*             log_error("dxp init hobj queue error."); */
/*             exit(1); */
/*         } */
/*         strncpy(hobjQueueQueue[dxpIdDistributionSize].queueName, defaultTarget.queue, MQ_Q_NAME_LENGTH); */
/*     } */
/*     log_info("init hobj queue queue completion, size is %d", hobjQueueSize); */
/* } */


/* static void enHobjQueue(const char *queueName, MQHOBJ hobj, MQHOBJ *phobj) */
/* { */
/*     ElementPtr elementPtr = (ElementPtr)malloc(sizeof(Element)); */
/*     if (elementPtr == NULL) { */
/*         log_error("malloc elementPtr error."); */
/*         return; */
/*     } */
/*     MQHOBJ *hobjPtr = NULL; */
/*     if (phobj == NULL) { */
/*         hobjPtr = (MQHOBJ *)malloc(sizeof(MQHOBJ)); */
/*         if (hobjPtr == NULL) { */
/*             log_error("malloc hobjPtr error."); */
/*             return; */
/*         } */
/*     } else { */
/*         hobjPtr = phobj; */
/*     } */
/*     elementPtr->data = (data_t)hobjPtr; */
/*     elementPtr->next = NULL; */
/*     QueuePtr hobjQueue = NULL; */

/*     log_info("hobj queue hobjQueueSize is %d, hobjQueueQueue is %p", hobjQueueSize, hobjQueueQueue); */
/*     for (int i = 0; i < hobjQueueSize; i++) { */
/*         if (strncmp(hobjQueueQueue[i].queueName, queueName, MQ_Q_NAME_LENGTH) == 0) { */
/*             hobjQueue = hobjQueueQueue[i].hobjQueue; */
/*             break; */
/*         } */
/*     } */
/*     if (hobjQueue == NULL) */
/*         return; */
/*     EnQueue(hobjQueue, elementPtr); */
/*     log_info("queue %s hobjQueueSize is %d", queueName, Size(hobjQueue)); */
/* } */

int getHobjByQueueName(const char *queueName, MQHOBJ **destHobj)
{
    if (queueName == NULL || destHobj == NULL)
        return -1;

    QueuePtr hobjQueue = NULL;

    for (int i = 0; i < hobjQueueSize; i++) {
        if (strncmp(hobjQueueQueue[i].queueName, queueName, MQ_Q_NAME_LENGTH) == 0) {
            hobjQueue = hobjQueueQueue[i].hobjQueue;
            break;
        }
    }

    if (hobjQueue == NULL)
        return -1;

    ElementPtr elementPtr = DeQueue(hobjQueue);
    log_info("dequeue %s hobjQueueSize is %d", queueName, Size(hobjQueue));
    if (elementPtr == NULL || elementPtr->data == NULL)
        return -1;

    *destHobj = (MQHOBJ *)elementPtr->data;
    return 0;
}
