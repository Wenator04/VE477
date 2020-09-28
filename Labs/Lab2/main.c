//VE477 Lab2 Kruskal and Prim
//Li Yong
//liyong1010@sjtu.edu.cn

#include <stdio.h>
#include <stdlib.h>
#include "MST.h"

void read(int eSize);
//EFFECT: read the edges in particular form

void print(int nodeNum);
//EFFECT: print the MST in particular form

int EdgeCompar(const void *a, const void *b);
//EFFECT: compar function for qsort of Edge

int MSTCompar(const void *a, const void *b);
//EFFECT: compar function for qsort of MST

void read(int eSize)
{
    graph = malloc(sizeof(Edge) * eSize);
    int v1, v2;
    for (int i = 0; i < eSize; i++)
    {
        scanf("%d %d %d", &v1, &v2, &graph[i].weight);
        if (v1 < v2)
        {
            graph[i].v1 = v1;
            graph[i].v2 = v2;
        }
        else
        {
            graph[i].v1 = v2;
            graph[i].v2 = v1;
        }
        
    }
}

void print(int edgeNum)
{
    for (int i = 0; i < edgeNum; i++)
    {
        printf("%d--%d\n", solution[i].v1, solution[i].v2);
    }
}

int EdgeCompar(const void *a, const void *b)
{
    Edge *edge1 = (Edge *)a;
    Edge *edge2 = (Edge *)b;
    return edge1->weight - edge2->weight;
}

int MSTCompar(const void *a, const void *b)
{
    MST *mst1 = (MST *)a;
    MST *mst2 = (MST *)b;
    if (mst1->v1 == mst2->v1)
    {
        return mst1->v2 - mst2->v2;
    }
    else
    {
        return mst1->v1 - mst2->v1;
    }
}

int main()
{
    int eSize = 0;
    int vSize = 0;
    scanf("%d", &eSize);
    scanf("%d", &vSize);
    read(eSize);
    UnionFind = malloc(sizeof(int) * 500);
    solution = malloc(sizeof(MST) * eSize);
    qsort(graph, eSize, sizeof(Edge), EdgeCompar);
    int edgeNum = Kruskal(eSize);
    //int edgeNum = Prim(eSize, vSize);
    qsort(solution, edgeNum, sizeof(MST), MSTCompar);
    print(edgeNum);
    free(graph);
    free(solution);
    free(UnionFind);
}