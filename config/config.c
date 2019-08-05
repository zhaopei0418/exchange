#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include "config.h"
#include "../log/log.h"


struct DefaultTarget defaultTarget;
struct QueueManager queueManagers[MAX_QUEUEMANAGER_LENGTH];
struct DxpIdDistribution dxpIdDistributions[MAX_DXP_DISTRIBUTION_LENGTH];
struct MsgTypeDistribution msgTypeDistributions[MAX_MSG_TYPE_DISTRIBUTION_LENGTH];
int queueManagerSize = 0;
int dxpIdDistributionSize = 0;
cJSON_bool conditionMutualExclusion = cJSON_True;

static cJSON *readConfig(const char *configPath);
static int getFileSize(const char *filePath);

static cJSON *readConfig(const char *configPath)
{
    int fileSize = getFileSize(configPath);
    if (fileSize == -1) {
        log_error("get file size error.");
        return NULL;
    }
    int fd;
    int count = 0;
    int num = 0;
    unsigned char buf;
    unsigned char *jsonData = (unsigned char *) malloc(sizeof(unsigned char) * fileSize);
    cJSON *configJson = NULL;
    if ((fd = open(configPath, O_RDONLY)) == -1) {
        log_error("open config file error.");
        goto end;
    }

    while ((num = read(fd, &buf, 1)) > 0)
        jsonData[count++] = buf;

    if (count == 0)
        goto end;
    configJson = cJSON_Parse((const char *)jsonData);
    if (configJson == NULL) {
        const char *errorPtr = cJSON_GetErrorPtr();
        if (errorPtr != NULL)
            log_error("cjson parse error: %s", errorPtr);
        goto end;
    }


end:
    if (jsonData != NULL)
        free(jsonData);
    return configJson;
}

static int getFileSize(const char *filePath)
{
    struct stat statbuf;
    if (stat(filePath, &statbuf) == -1) {
        log_error("stat error.");
        return -1;
    }
    return statbuf.st_size;
}

void parseConfig(const char *configPath)
{
    cJSON *configJson = readConfig(configPath);
    if (configJson == NULL)
        goto end;

    const cJSON *jsonDefaultTarget = NULL;
    const cJSON *qm = NULL;
    const cJSON *jsonQueueManagers = NULL;
    const cJSON *dxpIdDist = NULL;
    const cJSON *jsonDxpIdDistributions = NULL;

    jsonDefaultTarget = cJSON_GetObjectItemCaseSensitive(configJson, "defaultTarget");
    if (jsonDefaultTarget != NULL) {
        cJSON *qmId = cJSON_GetObjectItemCaseSensitive(jsonDefaultTarget, "qmId");
        cJSON *queue = cJSON_GetObjectItemCaseSensitive(jsonDefaultTarget, "queue");

        if (cJSON_IsNumber(qmId))
            defaultTarget.qmId = qmId->valuedouble;

        if (cJSON_IsString(queue) && queue->valuestring != NULL)
            strncpy(defaultTarget.queue, queue->valuestring, MQ_Q_NAME_LENGTH);
    }

    jsonQueueManagers = cJSON_GetObjectItemCaseSensitive(configJson, "queueManagers");
    cJSON_ArrayForEach(qm, jsonQueueManagers) {
        cJSON *qmId = cJSON_GetObjectItemCaseSensitive(qm, "qmId");
        cJSON *hostName = cJSON_GetObjectItemCaseSensitive(qm, "hostName");
        cJSON *port = cJSON_GetObjectItemCaseSensitive(qm, "port");
        cJSON *queueManager = cJSON_GetObjectItemCaseSensitive(qm, "queueManager");
        cJSON *channel = cJSON_GetObjectItemCaseSensitive(qm, "channel");
        cJSON *ccsid = cJSON_GetObjectItemCaseSensitive(qm, "ccsid");

        if (cJSON_IsNumber(qmId))
            queueManagers[queueManagerSize].qmId = qmId->valuedouble;

        if (cJSON_IsString(hostName) && hostName->valuestring != NULL)
            strncpy(queueManagers[queueManagerSize].hostName, hostName->valuestring, MQ_CONN_NAME_LENGTH);

        if (cJSON_IsNumber(port))
            queueManagers[queueManagerSize].port = port->valuedouble;

        if (cJSON_IsString(queueManager) && queueManager->valuestring != NULL)
            strncpy(queueManagers[queueManagerSize].queueManager, queueManager->valuestring, MQ_Q_MGR_NAME_LENGTH);

        if (cJSON_IsString(channel) && channel->valuestring != NULL)
            strncpy(queueManagers[queueManagerSize].channel, channel->valuestring, MQ_CHANNEL_NAME_LENGTH);

        if (cJSON_IsNumber(ccsid))
            queueManagers[queueManagerSize].ccsid = ccsid->valuedouble;

        queueManagerSize++;
    }

    jsonDxpIdDistributions = cJSON_GetObjectItemCaseSensitive(configJson, "dxpIdDistribution");
    cJSON_ArrayForEach(dxpIdDist, jsonDxpIdDistributions) {
        cJSON *dxpId = cJSON_GetObjectItemCaseSensitive(dxpIdDist, "dxpId");
        cJSON *qmId = cJSON_GetObjectItemCaseSensitive(dxpIdDist, "qmId");
        cJSON *queue = cJSON_GetObjectItemCaseSensitive(dxpIdDist, "queue");

        if (cJSON_IsString(dxpId) && dxpId->valuestring != NULL)
            strncpy(dxpIdDistributions[dxpIdDistributionSize].dxpId, dxpId->valuestring, MAX_DXP_DISTRIBUTION_LENGTH);

        if (cJSON_IsNumber(qmId))
            dxpIdDistributions[dxpIdDistributionSize].qmId = qmId->valuedouble;

        if (cJSON_IsString(queue) && queue->valuestring != NULL)
            strncpy(dxpIdDistributions[dxpIdDistributionSize].queue, queue->valuestring, MQ_Q_NAME_LENGTH);

        dxpIdDistributionSize++;
    }
end:
    cJSON_Delete(configJson);
}

int getQueueByDxpId(const char *dxpId, char *queue)
{
    if (dxpId == NULL || queue == NULL)
        return -1;
    for (int i = 0; i < dxpIdDistributionSize; i++) {
        if (strncmp(dxpId, dxpIdDistributions[i].dxpId, DXP_ID_LENGTH) == 0) {
            strncpy(queue, dxpIdDistributions[i].queue, MQ_Q_NAME_LENGTH);
            return 0;
        }
    }
    return -1;
}
