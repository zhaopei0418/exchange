#ifndef __MQ_H
#define __MQ_H
#include <pthread.h>
/* includes for MQ */
#include <cmqc.h>
#include <cmqxc.h>
#include "queue/queue.h"

#define BUFFER_SIZE 20000

typedef struct {
    MQBYTE *data;
    size_t size;
} MQMESSAGE;

typedef struct {
    int qmId;
    MQHCONN hConn;
} MQHCONN_DATA, *MQHCONN_DATA_PTR;

extern MQMESSAGE *gBuffer;
extern int bufferCount;

extern MQCHAR QMgrName[MQ_Q_MGR_NAME_LENGTH];   /* queue manager name            */
extern MQCHAR channelName[MQ_CHANNEL_NAME_LENGTH];
extern MQCHAR queueName[MQ_Q_NAME_LENGTH];
extern MQCHAR connectionName[MQ_CONN_NAME_LENGTH];
extern MQLONG ccsid;

extern pthread_mutex_t mtx;
extern pthread_cond_t condc;
extern pthread_cond_t condp;

extern int getMessageThreadCount;
extern int workThreadCount;

static void freeBuffer();
static void freeHcon();
static void enHconnQueue(MQHCONN hConn, int qmId);
void startGetMessage();
void clean();
#endif
