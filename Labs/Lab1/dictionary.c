// define your only data structure here, you may define dictionary, elements, etc...

#include "dictionary.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int key;
    int value;
    struct node *prev;
    struct node *next;
}Node;

typedef struct doubleList
{
    Node *head;
    Node *tail;
}DList;

void *initializer()
{
    DList *list;
    list = (DList *)malloc(sizeof(DList));
    list->head = (Node *)malloc(sizeof(Node));
    list->tail = (Node *)malloc(sizeof(Node));
    list->head->next = list->tail;
    list->head->prev = NULL;
    list->tail->prev = list->head;
    list->tail->next = NULL;
    return list;
}

void *search(void *dictionary, int key)
{
    DList *dict = dictionary;
    Node *sNode = dict->head->next;
    while (sNode != dict->tail)
    {
        if (sNode->key == key)
            return sNode;
        else if (sNode->key < key)
            sNode = sNode->next;
        else break;
    }
    return NULL;
}

void insert(void *dictionary, int key, int value)
{
    DList *dict = dictionary;
    Node *iNode = dict->head;
    while (iNode != dict->tail)
    {
        iNode = iNode->next;
        if (iNode->key == key)
        {
            iNode->value = value;
            break;
        }
        if (iNode->key > key || iNode == dict->tail)
        {
            Node *new = (Node *)malloc(sizeof(Node));
            new->prev = iNode->prev;
            new->next = iNode;
            iNode->prev = new;
            new->prev->next = new;
            new->key = key;
            new->value = value;
            break;
        }
    }
}

void delete(void *dictionary, int key)
{
    Node *dNode = search(dictionary, key);
    if (dNode != NULL)
    {
        Node *temp = dNode;
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        free(temp);
    }
}

void *minimum(void *dictionary)
{
    DList *dict = dictionary;
    if (dict->head->next != dict->tail)
        return dict->head->next;
    return NULL;
}

void *maximum(void *dictionary)
{
    DList *dict = dictionary;
    if (dict->head->next != dict->tail)
        return dict->tail->prev;
    return NULL;
}

void *predecessor(void *dictionary, int key)
{
    DList *dict = dictionary;
    Node *pNode = search(dictionary, key);
    if (pNode != NULL)
        if (pNode->prev != dict->head)
            return pNode->prev;
    return NULL;
}

void *successor(void *dictionary, int key)
{
    DList *dict = dictionary;
    Node *sNode = search(dictionary, key);
    if (sNode != NULL)
        if (sNode->next != dict->tail)
            return sNode->next;
    return NULL;
}


int getkey(void *element)
{
    Node *kNode = element;
    return kNode->key;
}

int getvalue(void *element)
{
    Node *vNode = element;
    return vNode->value;
}

void free_dict(void *dictionary)
{
    DList *dict = dictionary;
    Node *fNode = dict->head;
    Node *temp;
    while (fNode != NULL)
    {
        temp = fNode;
        fNode = fNode->next;
        free(temp);
    }
    free(dict);
}


