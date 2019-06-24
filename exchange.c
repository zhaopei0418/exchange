#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>
#include <ctype.h>
#include <wchar.h>
#include <locale.h>
#include <getopt.h>
#include <unistd.h>
#include <signal.h>
#include <pthread.h>
#include <uuid/uuid.h>
#include <cJSON.h>
#include "log/log.h"
#include "err/error.h"
#include "base64/base64.h"

/* includes for MQ */
#include <cmqc.h>
#include <cmqxc.h>
#define BUFFER_SIZE 20000
#define MAX_PATH 200

/* private function declarations */
static void help(const char *restrict cmdName);
static int parseOption(int argc, char **argv);

typedef struct {
    MQBYTE *data;
    size_t size;
} MQMESSAGE;
MQMESSAGE *gBuffer;
int bufferCount = 0;

void startGetMessage();
void waitUserPress();
void initalThread();
void stopApplication(int signum);
void messageConsumer(MQHCONN hConn, MQMD *pMsgDesc, MQGMO *pGetMsgOpts, MQBYTE *Buffer, MQCBC *pContext);
void writeMessageToFile(MQMESSAGE *message);

pthread_t *threads;
long nprocs = -1;

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
static char *PROJECT_NAME = "exchange";
static char *VERSION_NO = "1.0";
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t condc = PTHREAD_COND_INITIALIZER;  /* consumer condition variable */
static pthread_cond_t condp = PTHREAD_COND_INITIALIZER;  /* producer condition variable */
static FILE *LOGFILE;
static char *logFileName = "exchange.log";

char backupPath[MAX_PATH] = "\0";

static void help(const char *restrict cmdName)
{
    printf("%s %s\n", PROJECT_NAME, VERSION_NO);
    printf("    -x --connname <Connection Name> Connection Name such as 192.168.1.1 or 192.168.1.1(2400)\n");
    printf("    -c --channelname <Channel Name> Server Connection channel(for use by clients)\n");
    printf("    -m --qmname <Queue Manager Name> Queue Manager Name\n");
    printf("    -q --queue <Queue Name> Queue Name local or remote\n");
    printf("    -b --backup <backup path> backup queue message\n");
}

static int parseOption(int argc, char **argv)
{
    char *cmd = argv[0];
    int result = 0;
    if (argc == 1) {
        help(cmd);
        return -1;
    }
    int option_index = 0;
    struct option long_options[] = {
        {"connname",         required_argument, 0, 'x'},
        {"channelname",      required_argument, 0, 'c'},
        {"qmname",           required_argument, 0, 'm'},
        {"queue",            required_argument, 0, 'q'},
        {"backup",           required_argument, 0, 'b'},
        {"help",             no_argument,       0, 'h'}
    };
    while (1) {
        int c;

        c = getopt_long(argc, argv, "x:c:m:q:b:h", long_options, &option_index);
        if (c == -1)
            break;

        switch (c) {
        case 'x':
            strncpy(connectionName, optarg, MQ_CONN_NAME_LENGTH);
            log_info("ConnectionName is: %s", connectionName);
            break;
        case 'c':
            strncpy(channelName, optarg, MQ_CHANNEL_NAME_LENGTH);
            log_info("ChannelName is: %s", channelName);
            break;
        case 'm':
            strncpy(QMgrName, optarg, MQ_Q_MGR_NAME_LENGTH);
            log_info("QmgrName is: %s", QMgrName);
            break;
        case 'q':
            strncpy(queueName, optarg, MQ_Q_NAME_LENGTH);
            log_info("QueueName is: %s", queueName);
            break;
        case 'b':
            strncpy(backupPath, optarg, MAX_PATH);
            log_info("backupPath is: %s", backupPath);
            break;
        default:
            help(cmd);
            break;
        }
    }

    return result;
}

/********************************************************************/
/* FUNCTION: messageConsumer                                        */
/* PURPOSE : Callback function called when messages arrive          */
/********************************************************************/
void messageConsumer(MQHCONN   hConn,
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
            log_info("Event Call : Reason = %d",pContext->Reason);
            break;

        default:
            log_info("Calltype = %d",pContext->CallType);
            break;

    }
}

void stopApplication(int signum)
{
    int rtnVal = 1;
    if (threads != NULL) {
        for (int i = 0; i < nprocs; i++)
            pthread_cancel(threads[i]);
        free(threads);
    }

    if (gBuffer != NULL)
        free(gBuffer);

    log_debug("handle SIGINT signal");
    if (LOGFILE) {
        fclose(LOGFILE);
    }
}

void startGetMessage()
{
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

void *workThread(void *arg)
{
    pthread_t tid = pthread_self();
    MQMESSAGE message;
    while (1) {
        pthread_mutex_lock(&mtx);
        while (bufferCount <= 0)
            pthread_cond_wait(&condc, &mtx);

        message = gBuffer[--bufferCount];

        if (bufferCount <= 0)
            pthread_cond_signal(&condp);

        pthread_mutex_unlock(&mtx);
        log_info("workThread: %u, message (%u Bytes) :", (unsigned int)tid, message.size);

        if (message.data != NULL) {
            log_info("thread: %u, message is: [%s]", (unsigned int)tid, message.data);
            if (strlen(backupPath) > 0)
                writeMessageToFile(&message);
            free(message.data);
        } else {
            log_info("thread: %u, no data.", (unsigned int)tid);
        }
        message.size = 0;
    }
}

char* mergePath(char *dstpath, const char *filePrefix, const char *uuid, const char *fileExt)
{
    strcat(dstpath, "/");
    strcat(dstpath, filePrefix);
    strcat(dstpath, uuid);
    strcat(dstpath, fileExt);
    return dstpath;
}

int notExistsCreateDir(const char *dir)
{
    if (access(dir, R_OK) != 0) {
        if (mkdir(dir, 0755) == -1) {
            log_error("mkdir %s error.", dir);
            return -1;
        }
    }

    return 0;
}

void writeMessageToFile(MQMESSAGE *message)
{
    uuid_t uuid;
    char uuidStr[36];
    char *filePrefix = "FILE_BACKUP_";
    char *tmpFileExt = ".writing";
    char *fileExt = ".xml";
    char tmpFilePath[MAX_PATH];
    char filePath[MAX_PATH];
    FILE *tmpfp;

    uuid_generate(uuid);
    uuid_unparse(uuid, uuidStr);
    pthread_t tid = pthread_self();

    if (notExistsCreateDir(backupPath) == -1)
        return;

    strcpy(tmpFilePath, backupPath);
    strcpy(filePath, backupPath);

    mergePath(tmpFilePath, filePrefix, uuidStr, tmpFileExt);
    mergePath(filePath, filePrefix, uuidStr, fileExt);
    log_info("thread: %u, tmpFilePath: %s, filePath: %s", (unsigned int)tid, tmpFilePath, filePath);

    tmpfp = fopen(tmpFilePath, "w");
    if (tmpfp == NULL) {
        log_error("fopen error.");
        return;
    }

    char *dataStart = "<Data>";
    char *dataEnd = "</Data>";

    char *dataStartPos = strstr(message->data, "<Data>");
    char *dataEndPos = strstr(message->data, "</Data>");

    if (dataStartPos && dataEndPos && dataEndPos > dataStartPos) {
        *dataEndPos = '\0';
        setlocale(LC_ALL, "en_US.utf8");
        size_t dataLength = (dataEndPos - dataStartPos) * 3 / 4;
        char *startPos = dataStartPos + strlen(dataStart);
        log_info("data is %s", startPos);
        char *odata = (char *)malloc(sizeof(char) * dataLength);
        size_t bytes = base64_decode(startPos, odata);
        odata[bytes] = '\0';
        log_info("bytes is %u", bytes);
        log_info("odata is %s", odata);
        fprintf(tmpfp, "%s", odata);
        free(odata);
    } else {
        for (int i = 0; i < message->size; i++)
            fputc(message->data[i], tmpfp);
    }

    fclose(tmpfp);

    if (rename(tmpFilePath, filePath) == -1)
        log_error("thread: %u, rename error.", (unsigned int)tid);
    else
        log_info("thread: %u, rename %s -> %s success.", (unsigned int)tid, tmpFilePath, filePath);
}

void initalThread()
{
    log_info("nprocs is %d", nprocs);
    threads = (pthread_t *) malloc(sizeof(pthread_t) * nprocs);
    for (int i = 0; i < nprocs; i++) {
        pthread_create(threads + i, NULL, workThread, NULL);
    }
}

void waitUserPress()
{
    /******************************************************************/
    /*                                                                */
    /*  Wait for the user to press enter                              */
    /*                                                                */
    /******************************************************************/
    {
        char buffer[10];
        const char *quit = "quit";
        log_info("Press quit to end");
waitInput:
        fgets(buffer, sizeof(buffer), stdin);
        if (strcmp(quit, buffer) != 0)
            goto waitInput;
    }
}

int main(int argc, char **argv)
{
    LOGFILE = fopen(logFileName, "a");
    if (!LOGFILE) {
            LOGFILE = fopen(logFileName, "w");
            if (!LOGFILE) {
                err_sys("File opening failed");
            }

    }
    log_set_fp(LOGFILE);

    if (parseOption(argc, argv) < 0) {
        log_info("parse option error.");
        exit(1);
    }

    nprocs = sysconf(_SC_NPROCESSORS_ONLN);
    if (nprocs == -1) {
        log_info("get processors error.");
        exit(1);
    }

    signal(SIGINT, stopApplication);
    signal(SIGQUIT, stopApplication);

    gBuffer = (MQMESSAGE *) malloc(sizeof(MQMESSAGE) * BUFFER_SIZE);
    initalThread();
    startGetMessage();
    waitUserPress();

    stopApplication(SIGINT);

    exit(0);
}
