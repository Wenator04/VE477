//Minimum spanning tree
//Kruskal and Prim

#ifndef MST_H
#define MST_H

#include <stdio.h>
#include <stdlib.h>

typedef struct edge
{
    int v1,v2;
    int weight;
} Edge;

typedef struct mst
{
    int v1, v2;
} MST;

//Global variable for convenience operations
Edge *graph;
int *UnionFind;
MST *solution;

void UnionFindInitial(int eSize);
//EFFECT: intialize the union-find data structure

void Union(int v1, int v2);
//EFFECT: link the root of the tree containing v1 to the root of the tree containing v2 (or the other way around)

int Find(int v);
//EFFECT: find the root of the tree for vertex v
//RETURN: return the integer representing the root

int Kruskal(int eSize);
//EFFECT: run Kruskal algorithm to get MST
//RETURN: the number of vertexes in the MST

int Prim(int eSize, int vSize);
//EFFECT: run Prim algorithm to get MST
//RETURN: the number of vertexes in the MST

#endif