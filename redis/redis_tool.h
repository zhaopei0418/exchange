#ifndef __REDIS_TOOL_H
#define __REDIS_TOOL_H
#define HOSTNAME_LENGTH 200

extern char hostname[HOSTNAME_LENGTH];
extern int port;

void initConnectionRedis();
void disconnectRedis();
int lpush(const char *list, const char *value);
int blpop(const char *list, char *dst);

#endif
