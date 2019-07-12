#ifndef __MQ_H
#define __MQ_H
#include <pthread.h>
/* includes for MQ */
#include <cmqc.h>
#include <cmqxc.h>
#include "queue/queue.h"
#include "config/config.h"

#define BUFFER_SIZE 20000

typedef struct {
    MQBYTE *data;
    size_t size;
} MQMESSAGE;

typedef struct {
    int qmId;
    MQHCONN hConn;
} MQHCONN_DATA, *MQHCONN_DATA_PTR;

typedef struct {
    char queueName[MQ_Q_NAME_LENGTH];
    QueuePtr hobjQueue;
} MQHOBJ_QUEUE, *MQHOBJ_QUEUE_PTR;

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
extern QueuePtr hconnQueue;

void startGetMessage();
void clean();
void dataHandle(void *data);
int sendMessageToQueue(const MQMESSAGE *message, const char *queue);
int getHobjByQueueName(const char *queueName, MQHOBJ **destHobj);
int setThreadConnection();
int getThreadConnection();
#endif
