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
#include <stdint.h>
#include <uuid/uuid.h>
#include <cJSON.h>
#include "log/log.h"
#include "err/error.h"
#include "base64/base64.h"
#include "config/config.h"
#ifdef USE_REDIS
#include "redis/redis_tool.h"
#endif
#include "mq.h"
#include "tool/tool.h"

#define MAX_PATH 200

/* private function declarations */
static void help(const char *restrict cmdName);
static int parseOption(int argc, char **argv);

int loglevel = 0;
char configFile[MAX_PATH + 1] = "\0";

pthread_t *threads;
int workThreadCount = 0;
int decode = 0;

void initalThread();
void stopApplication(int signum);
void writeMessageToFile(const MQMESSAGE *message);
void sendMessage(const MQMESSAGE *message);
void exitFunction();


static char *PROJECT_NAME = "exchange";
static char *VERSION_NO = "1.1";
static pthread_mutex_t main_mutex = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t main_cond = PTHREAD_COND_INITIALIZER;  /* main condition variable */
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
    printf("    -d --ccsid <ccsid> ccsid\n");
    printf("    -b --backup <backup path> backup queue message\n");
    printf("    -l --loglevel <loglevel> log level, 0:TRACE(default), 1:DEBUG, 2:INFO, 3:WARN, 4:ERROR, 5:FATAL\n");
    printf("    -f --file <config file path> config file path\n");
#ifdef USE_REDIS
    printf("    -H --hostname <redis host name> redis host name default 127.0.0.1\n");
    printf("    -p --port <redis port> redis port. default 6379\n");
#endif
    printf("    -t --gtcount <thread count> get message thread count, default 1\n");
    printf("    -T --htcount <thread count> handle message thread count, default cpu count\n");
    printf("    -D --decode  <decode data> whether to decode data, 0: not, 1: yes, default: 0\n");
    printf("    -h --help show help menu\n");
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
        {"ccsid",            required_argument, 0, 'd'},
        {"backup",           required_argument, 0, 'b'},
        {"loglevel",         required_argument, 0, 'l'},
        {"file",             required_argument, 0, 'f'},
#ifdef USE_REDIS
        {"hostname",         required_argument, 0, 'H'},
        {"port",             required_argument, 0, 'p'},
#endif
        {"gtcount",          required_argument, 0, 't'},
        {"htcount",          required_argument, 0, 'T'},
        {"decode",           required_argument, 0, 'D'},
        {"help",             no_argument,       0, 'h'}
    };
    while (1) {
        int c;

#ifdef USE_REDIS
        c = getopt_long(argc, argv, "x:c:m:q:d:b:l:f:H:p:t:T:D:h", long_options, &option_index);
#else
        c = getopt_long(argc, argv, "x:c:m:q:d:b:l:f:t:T:D:h", long_options, &option_index);
#endif
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
        case 'd':
            ccsid = atoi(optarg);
            log_info("ccsid is: %d", ccsid);
            break;
        case 'b':
            strncpy(backupPath, optarg, MAX_PATH);
            log_info("backupPath is: %s", backupPath);
            break;
        case 'l':
            loglevel = atoi(optarg);
            log_info("loglevel is: %d", loglevel);
            if (loglevel < 0 && loglevel > 5) {
                log_error("loglevel illegal, only 0 to 5.");
                result = -1;
            }
            break;
        case 'f':
            strncpy(configFile, optarg, MAX_PATH);
            log_info("configFile is: %s", configFile);
            break;
#ifdef USE_REDIS
        case 'H':
            strncpy(hostname, optarg, HOSTNAME_LENGTH);
            log_info("redis hostname is: %s", hostname);
            break;
        case 'p':
            port = atoi(optarg);
            log_info("redis port is: %d", port);
            break;
#endif
        case 't':
            getMessageThreadCount = atoi(optarg);
            log_info("getMessageThreadCount is: %d", getMessageThreadCount);
            break;
        case 'T':
            workThreadCount = atoi(optarg);
            log_info("workThreadCount is: %d", workThreadCount);
            break;
        case 'D':
            decode = atoi(optarg);
            log_info("decode is: %d", decode);
            if (decode != 0 && decode != 1) {
                log_error("decode illegal, only 0 and 1.");
                result = -1;
            }
            break;
        default:
            help(cmd);
            result = -1;
            break;
        }
    }

    return result;
}

void exitFunction()
{
    stopApplication(0);
}

void stopApplication(int signum)
{
    log_debug("handle SIGINT signal");
    int rtnVal = 1;
    if (threads != NULL) {
        for (int i = 0; i < workThreadCount; i++)
            pthread_cancel(threads[i]);
        free(threads);
    }

    clean();

    if (LOGFILE) {
        fclose(LOGFILE);
    }

#ifdef USE_REDIS
    disconnectRedis();
#endif
    _exit(0);
}

void *workThread(void *arg)
{
    pthread_t tid = pthread_self();
    MQMESSAGE message;
    while (1) {
        pthread_mutex_lock(&mtx);
        while (bufferCount <= 0)
            pthread_cond_wait(&condc, &mtx);

        message.data = gBuffer[--bufferCount].data;
        message.size = gBuffer[bufferCount].size;
        gBuffer[bufferCount].data = NULL;
        gBuffer[bufferCount].size = 0;

        if (bufferCount <= 0)
            pthread_cond_signal(&condp);

        pthread_mutex_unlock(&mtx);
        log_info("thread: %u, message (%u Bytes) :", (unsigned int)tid, message.size);

        if (message.data != NULL) {
            log_info("thread: %u, message is: [%s]", (unsigned int)tid, message.data);
            if (strlen(configFile) > 0)
                sendMessage(&message);

            if (strlen(backupPath) > 0)
                writeMessageToFile(&message);
            free(message.data);
        } else {
            log_info("thread: %u, no data.", (unsigned int)tid);
        }

        message.data = NULL;
        message.size = 0;
    }
}

void sendMessage(const MQMESSAGE *message)
{
    char *dataStart = "<ReceiverId>";
    char *dataEnd = "</ReceiverId>";

    char *dataStartPos = strstr(message->data, dataStart);
    char *dataEndPos = strstr(message->data, dataEnd);
    char queue[MQ_Q_NAME_LENGTH];

    if (dataStartPos && dataEndPos && dataEndPos > dataStartPos) {
        *dataEndPos = '\0';
        char *startPos = dataStartPos + strlen(dataStart);
        log_info("dxpId is %s", startPos);
        if (getQueueByDxpId(startPos, queue) == -1) {
            log_error("dxpId: %s no corresponding queue was found, use default queue %s", startPos, defaultTarget.queue);
            strncpy(queue, defaultTarget.queue, MQ_Q_NAME_LENGTH);
        }
        *dataEndPos = '<';
    }
    log_info("send to queue %s", queue);
    while (hconnQueue == NULL) {

    }
    sendMessageToQueue(message, queue);
}

void writeMessageToFile(const MQMESSAGE *message)
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

    if (decode) {
        char *dataStart = "<Data>";
        char *dataEnd = "</Data>";

        char *dataStartPos = strstr(message->data, dataStart);
        char *dataEndPos = strstr(message->data, dataEnd);

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
            fprintf(tmpfp, "%s", message->data);
        }
    } else {
        fprintf(tmpfp, "%s", message->data);
    }

    fclose(tmpfp);

    if (rename(tmpFilePath, filePath) == -1)
        log_error("thread: %u, rename error.", (unsigned int)tid);
    else
        log_info("thread: %u, rename %s -> %s success.", (unsigned int)tid, tmpFilePath, filePath);
}

void initalThread()
{
    log_info("workThreadCount is %d", workThreadCount);
    threads = (pthread_t *) malloc(sizeof(pthread_t) * workThreadCount);
    for (int i = 0; i < workThreadCount; i++) {
        pthread_create(threads + i, NULL, workThread, NULL);
    }
}

int main(int argc, char **argv)
{
    atexit(exitFunction);
    LOGFILE = fopen(logFileName, "a");
    if (!LOGFILE) {
            LOGFILE = fopen(logFileName, "w");
            if (!LOGFILE) {
                err_sys("File opening failed");
            }

    }
    log_set_fp(LOGFILE);

    if (parseOption(argc, argv) < 0) {
        exit(1);
    }
    log_set_level(loglevel);

    if (strlen(configFile) > 0) {
        parseConfig(configFile);
        log_info("config file content: ");
        log_info("defaultTarget qmId: %d", defaultTarget.qmId);
        log_info("defaultTarget queue: %s", defaultTarget.queue);
        log_info("queueManagerSize is: %d", queueManagerSize);
        for (int i = 0; i < queueManagerSize; i++) {
            log_info("[%d] queueManager qmId: %d", i, queueManagers[i].qmId);
            log_info("[%d] queueManager hostName: %s", i, queueManagers[i].hostName);
            log_info("[%d] queueManager port: %d", i, queueManagers[i].port);
            log_info("[%d] queueManager queueManager: %s", i, queueManagers[i].queueManager);
            log_info("[%d] queueManager channel: %s", i, queueManagers[i].channel);
            log_info("[%d] queueManager ccsid: %d", i, queueManagers[i].ccsid);
        }

        log_info("dxpIdDistributionSize is: %d", dxpIdDistributionSize);
        for (int i = 0; i < dxpIdDistributionSize; i++) {
            log_info("[%d] dxpIdDistribution dxpId: %s", i, dxpIdDistributions[i].dxpId);
            log_info("[%d] dxpIdDistribution qmId: %d", i, dxpIdDistributions[i].qmId);
            log_info("[%d] dxpIdDistribution queue: %s", i, dxpIdDistributions[i].queue);
        }
    }

    if (workThreadCount == 0) {
        long nprocs = sysconf(_SC_NPROCESSORS_ONLN);
        if (nprocs == -1) {
            log_info("get processors error.");
            exit(1);
        }
        workThreadCount = (int) nprocs;
    }

    signal(SIGINT, stopApplication);
    signal(SIGQUIT, stopApplication);

    /* initConnectionRedis(); */
    /* char testFuncPtr[20]; */
    /* sprintf(testFuncPtr, "%lld", testFunction); */
    /* log_info("testFuncPtr is: %s", testFuncPtr); */
    /* lpush("pfunc", testFuncPtr); */
    /* char dstTestFuncPtr[20]; */
    /* blpop("pfunc", dstTestFuncPtr); */
    /* log_info("dstTestFuncPtr is: %s", dstTestFuncPtr); */
    /* uintptr_t testFuncP = atoll(dstTestFuncPtr); */
    /* log_info("testFuncP is: %x, %lld", testFuncP, testFuncP); */
    /* ((void (*) ()) testFuncP)(); */

    initalThread();
    startGetMessage();
    pthread_mutex_lock(&main_mutex);
    pthread_cond_wait(&main_cond, &main_mutex);
    pthread_mutex_unlock(&main_mutex);

    stopApplication(SIGINT);

    exit(0);
}
