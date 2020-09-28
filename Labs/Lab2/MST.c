#include "MST.h"

void UnionFindInitial(int eSize)
{
    for (int i = 0; i < eSize; i++)
    {
        UnionFind[i] = -1 * eSize;
    }
}

void Union(int v1, int v2)
{
    int root1 = Find(v1);
    int root2 = Find(v2);
    if (root1 > root2)
    {
        UnionFind[root2] += UnionFind[root1];
        UnionFind[root1] = root2;
    }
    else
    {
        UnionFind[root1] += UnionFind[root2];
        UnionFind[root2] = root1;
    }
    
}

int Find(int v)
{
    if (UnionFind[v] < 0)
    {
        return v;
    }
    UnionFind[v] = Find(UnionFind[v]);
    return UnionFind[v];
}

int Kruskal(int eSize)
{
    int v1, v2;
    UnionFindInitial(eSize);
    int count = 0;
    for (int i = 0; i < eSize; i++)
    {
        v1 = graph[i].v1;
        v2 = graph[i].v2;
        if (Find(v1) != Find(v2))
        {
            solution[count].v1 = graph[i].v1;
            solution[count].v2 = graph[i].v2;
            Union(v1, v2);
            count++;
        }
    }
    return count;
}

int sum(const int *array, int length)
{
    int sum = 0;
    for (int i =0; i < length; i++)
    {
        sum += array[i];
    }
    return sum;
}

int Prim(int eSize, int vSize)
{
    int count = 0;
    int *edgeKeys = malloc(sizeof(int) * eSize);
    int i;
    for (i = 0; i < eSize; i++)
    {
        edgeKeys[i] = 0;
    }
    int *vertexKeys = malloc(sizeof(int) * vSize);
    for (i = 0; i < vSize; i++)
    {
        vertexKeys[i] = 0;
    }
    i = 0;
    while (i > -1)
    {
        if (edgeKeys[i] == 1)
        {
            i++;
            i = i % eSize;
            continue;
        }
        if (vertexKeys[graph[i].v1] + vertexKeys[graph[i].v2] == 2)
        {
            i++;
            i = i % eSize;
            continue;
        }
        if (i == 0 || vertexKeys[graph[i].v1] + vertexKeys[graph[i].v2] == 1)
        {
            vertexKeys[graph[i].v1] = 1;
            vertexKeys[graph[i].v2] = 1;
            edgeKeys[i] = 1;
            solution[count].v1 = graph[i].v1;
            solution[count].v2 = graph[i].v2;
            count++;
            i = 0;
        }
        int j = 0;
        for (j = 0; j < vSize; j++)
        {
            if (vertexKeys[j] == 0)
            {
                break;
            }
        }
        if (j == vSize)
        {
            break;
        }
    }
    free(edgeKeys);
    free(vertexKeys);
    return count;
}