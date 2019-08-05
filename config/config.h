#ifndef __CONFIG_H
#define __CONFIG_H
#include <cmqc.h>
#include <cmqxc.h>
#include <cJSON.h>

#define DXP_ID_LENGTH 31
#define MAX_QUEUEMANAGER_LENGTH 20
#define MAX_DXP_DISTRIBUTION_LENGTH 50
#define MAX_MSG_TYPE_DISTRIBUTION_LENGTH 50
#define MAX_MSG_TYPE_LENGTH 14

struct DefaultTarget {
    int qmId;
    char queue[MQ_Q_NAME_LENGTH];
};

struct QueueManager {
    int qmId;
    char hostName[MQ_CONN_NAME_LENGTH];
    int port;
    char queueManager[MQ_Q_MGR_NAME_LENGTH];
    char channel[MQ_CHANNEL_NAME_LENGTH];
    MQLONG ccsid;
};

struct DxpIdDistribution {
    char dxpId[DXP_ID_LENGTH];
    int qmId;
    char queue[MQ_Q_NAME_LENGTH];
};

struct MsgTypeDistribution {
    char msgType[MAX_MSG_TYPE_LENGTH];
    int qmId;
    char queue[MQ_Q_NAME_LENGTH];
};

extern struct DefaultTarget defaultTarget;
extern struct QueueManager queueManagers[MAX_QUEUEMANAGER_LENGTH];
extern struct DxpIdDistribution dxpIdDistributions[MAX_DXP_DISTRIBUTION_LENGTH];
extern struct MsgTypeDistribution msgTypeDistributions[MAX_MSG_TYPE_DISTRIBUTION_LENGTH];
extern int queueManagerSize;
extern int dxpIdDistributionSize;
extern cJSON_bool conditionMutualExclusion;

void parseConfig(const char *configPath);
int getQueueByDxpId(const char *dxpId, char *queue);

#endif
