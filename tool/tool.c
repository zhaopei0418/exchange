#include "tool.h"
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include "../log/log.h"

char *mergePath(char *dstpath, const char *filePrefix, const char *uuid, const char *fileExt)
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
