#ifndef __MQ_H
#define __MQ_H
#include <pthread.h>
/* includes for MQ */
#include <cmqc.h>
#include <cmqxc.h>

#define BUFFER_SIZE 20000

typedef struct {
    MQBYTE *data;
    size_t size;
} MQMESSAGE;
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

void freeBuffer();
void startGetMessage();
#endif
