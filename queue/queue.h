#ifndef __QUEUE_H
#define __QUEUE_H
#include <pthread.h>

typedef void * data_t;
typedef struct Element * ElementPtr;
typedef struct Element {
    data_t data;
    ElementPtr next;
} Element;

typedef struct {
    ElementPtr head;
    ElementPtr tail;
    int size;
    pthread_mutex_t qmutex;
    pthread_cond_t qcond;
} Queue, *QueuePtr;

QueuePtr InitQueue();
void DestroyQueue(QueuePtr queuePtr, void (*dataHandle)(void *));
void ClearQueue(QueuePtr queuePtr, void (*dataHandle)(void *));
int Empty(QueuePtr queuePtr);
int Size(QueuePtr queuePtr);
ElementPtr Head(QueuePtr queuePtr);
ElementPtr Tail(QueuePtr queuePtr);
ElementPtr EnQueue(QueuePtr queuePtr, ElementPtr elementPtr);
ElementPtr DeQueue(QueuePtr queuePtr);
ElementPtr Take(QueuePtr queuePtr);

#endif
