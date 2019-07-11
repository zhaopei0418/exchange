#include <stdlib.h>
#include "queue.h"

QueuePtr InitQueue()
{
    QueuePtr queuePtr = (QueuePtr)malloc(sizeof(Queue));
    if (queuePtr != NULL) {
        queuePtr->head = NULL;
        queuePtr->tail = NULL;
        queuePtr->size = 0;
        if (pthread_mutex_init(&queuePtr->qmutex, NULL) != 0) {
            free(queuePtr);
            return NULL;
        }

        if (pthread_cond_init(&queuePtr->qcond, NULL) != 0) {
            free(queuePtr);
            return NULL;
        }
    }
    return queuePtr;
}

void DestroyQueue(QueuePtr queuePtr, void (*dataHandle)(void *))
{
    if (queuePtr == NULL)
        return;
    ClearQueue(queuePtr, dataHandle);
    pthread_mutex_destroy(&queuePtr->qmutex);
    pthread_cond_destroy(&queuePtr->qcond);
    free(queuePtr);
    queuePtr = NULL;
}

void ClearQueue(QueuePtr queuePtr, void (*dataHandle)(void *))
{
    ElementPtr elementPtr = NULL;
    while ((elementPtr = DeQueue(queuePtr)) != NULL) {
        if (elementPtr->data != NULL) {
            if (dataHandle != NULL) {
                dataHandle(elementPtr->data);
            }
        }
        free(elementPtr);
    }
}

int Empty(QueuePtr queuePtr)
{
    if (queuePtr->head == NULL && queuePtr->tail == NULL && queuePtr->size == 0)
        return 1;
    else
        return 0;
}

int Size(QueuePtr queuePtr)
{
    return queuePtr->size;
}

ElementPtr Head(QueuePtr queuePtr)
{
    ElementPtr elementPtr = NULL;
    pthread_mutex_lock(&queuePtr->qmutex);

    if (!Empty(queuePtr))
        elementPtr = queuePtr->head;

    pthread_mutex_unlock(&queuePtr->qmutex);
    return elementPtr;
}

ElementPtr Tail(QueuePtr queuePtr)
{
    ElementPtr elementPtr = NULL;
    pthread_mutex_lock(&queuePtr->qmutex);

    if (!Empty(queuePtr))
        elementPtr = queuePtr->tail;

    pthread_mutex_unlock(&queuePtr->qmutex);
    return elementPtr;
}

ElementPtr EnQueue(QueuePtr queuePtr, ElementPtr elementPtr)
{
    if (elementPtr != NULL) {
        pthread_mutex_lock(&queuePtr->qmutex);

        if (Empty(queuePtr))
            queuePtr->head = elementPtr;
        else
            queuePtr->tail->next = elementPtr;

        queuePtr->tail = elementPtr;
        queuePtr->size++;
        pthread_cond_signal(&queuePtr->qcond);
        pthread_mutex_unlock(&queuePtr->qmutex);
    }
    return elementPtr;
}

ElementPtr DeQueue(QueuePtr queuePtr)
{
    ElementPtr elementPtr = NULL;
    pthread_mutex_lock(&queuePtr->qmutex);

    if (!Empty(queuePtr)) {
        elementPtr = queuePtr->head;
        queuePtr->head = elementPtr->next;
        queuePtr->size--;
        if (queuePtr->size == 0) {
            queuePtr->tail = NULL;
            queuePtr->head = NULL;
        }
    }

    pthread_mutex_unlock(&queuePtr->qmutex);
    return elementPtr;
}

ElementPtr Take(QueuePtr queuePtr)
{
    ElementPtr elementPtr = NULL;
    pthread_mutex_lock(&queuePtr->qmutex);

    while (Empty(queuePtr))
        pthread_cond_wait(&queuePtr->qcond, &queuePtr->qmutex);

    elementPtr = queuePtr->head;
    queuePtr->head = elementPtr->next;
    queuePtr->size--;
    if (queuePtr->size == 0) {
        queuePtr->tail = NULL;
        queuePtr->head = NULL;
    }

    pthread_mutex_unlock(&queuePtr->qmutex);
    return elementPtr;
}
