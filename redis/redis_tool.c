#include <stdlib.h>
#include <string.h>
#include <hiredis/hiredis.h>
#include "../log/log.h"
#include "redis_tool.h"

char hostname[HOSTNAME_LENGTH] = "127.0.0.1";
int port = 6379;
redisContext *rc;

void initConnectionRedis()
{
    struct timeval timeout = {3, 0};
    rc = redisConnectWithTimeout(hostname, port, timeout);

    if (rc == NULL || rc->err) {
        if (rc) {
            log_error("connection error %s", rc->errstr);
            redisFree(rc);
        } else {
            log_error("connection error: can't allocate redis context");
        }
        exit(1);
    }

    redisReply *reply;

    reply = redisCommand(rc, "PING");
    log_info("PING: %s", reply->str);
    freeReplyObject(reply);

    reply = redisCommand(rc, "SET %s %s", "foo", "hello world");
    log_info("SET: %s", reply->str);
    freeReplyObject(reply);
}

void disconnectRedis()
{
    if (rc != NULL)
        redisFree(rc);
}

int lpush(const char *list, const char *value)
{
    redisReply *reply;
    reply = redisCommand(rc, "LPUSH %s %s", list, value);
    log_info("LPUSH: %lld", reply->integer);
    return 0;
}

int blpop(const char *list, char *dst)
{
    redisReply *reply;
    reply = redisCommand(rc, "BLPOP %s 0", list);
    if (reply->type == REDIS_REPLY_ARRAY) {
        if (dst != NULL)
            strcpy(dst, reply->element[1]->str);
        for (int i = 0; i < reply->elements; i++)
            log_info("%u %s", i, reply->element[i]->str);
    }
    return 0;
}
