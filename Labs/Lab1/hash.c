// define your only data structure here, you may define hashtable, buckets, elements, etc...
#include "hash.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int key;
    int value;
    struct node *next;
} Node;

typedef struct singleList
{
    Node *head;
    struct singleList *next;
} SList;

typedef struct hash
{
    SList *head;
} Hash;

void *initializer(int size)
{
    size = size / 3;
    Hash *initial = (Hash *)malloc(sizeof(Hash));
    initial->head = (SList *)malloc(sizeof(SList));
    SList *iList = initial->head;
    for (int i = 0; i < size; i++)
    {
        iList->head = (Node *)malloc(sizeof(Node));
        iList->head->next = NULL;
        if (i < size - 1)
        {
            iList->next = (SList *)malloc(sizeof(SList));
            iList = iList->next;
        }
        else iList->next = NULL;
    }
    return initial;
}

void insert(void* hashtable, int size, int key, int value)
{
    size = size / 3;
    Hash *hashT = hashtable;
    int bucket = key % size;
    SList *iList = hashT->head;
    for (int i = 0; i < bucket; i++)
        iList = iList->next;
    Node *iNode = iList->head;
    while (iNode->next != NULL)
    {
        iNode = iNode->next;
        if (iNode->key == key)
        {
            iNode->value = value;
            return;
        }
    }
    Node *new = (Node *)malloc(sizeof(Node));
    new->next = NULL;
    new->key = key;
    new->value = value;
    iNode->next = new;
}

void delete(void* hashtable, int size, int key)
{
    size = size / 3;
    Hash *hashT = hashtable;
    int bucket = key % size;
    SList *dList = hashT->head;
    for (int i = 0; i < bucket; i++)
        dList = dList->next;
    Node *dNode = dList->head;
    while (dNode->next != NULL)
    {
        if (dNode->next->key == key)
        {
            Node *temp = dNode->next;
            dNode->next = temp->next;
            free(temp);
            break;
        }
        dNode = dNode->next;
    }
}

void* search(void* hashtable, int size, int key)
{
    size = size / 3;
    Hash *hashT = hashtable;
    int bucket = key % size;
    SList *sList = hashT->head;
    for (int i = 0; i < bucket; i++)
        sList = sList->next;
    Node *sNode = sList->head;
    while (sNode->next != NULL)
    {
        sNode = sNode->next;
        if (sNode->key == key)
            return sNode;
    }
    return NULL;
}

int getValue(void* element)
{
    Node *vNode = element;
    return vNode->value;
}

void freeHashtable(void* hashtable, int size)
{
    size = size / 3;
    Hash *hashT = hashtable;
    SList *fList = hashT->head;
    SList *listTemp;
    Node *fNode, *nodeTemp;
    for(int i = 0; i < size; i++)
    {
        fNode = fList->head;
        while (fNode != NULL)
        {
            nodeTemp = fNode->next;
            free(fNode);
            fNode = nodeTemp;
        }
        listTemp = fList->next;
        free(fList);
        fList = listTemp;
    }
    free(hashT);
}


