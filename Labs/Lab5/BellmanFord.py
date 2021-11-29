#
# Created by Yong on 11/25/2021
#

from SparseGraph import SGraph

if __name__ == "__main__":
    graph = SGraph()
    size = input()
    for i in range(int(size)):
        u, v, weight = input().split()
        graph.AddVertex(u)
        graph.AddVertex(v)
        graph.AddEdge(u, v, float(weight))
    src = input().strip()
    tar = input().strip()
    
    dist = {}
    prev = {}
    for node in graph.vertices:
        if node == src:
            dist[node] = 0.0
            prev[node] = None
        else:
            dist[node] = float('inf')
            prev[node] = None
    for i in range(graph.edgesNum - 1):
        for edge, weight in graph.edges.items():
            tmp = dist[edge[0]] + weight
            if tmp < dist[edge[1]]:
                dist[edge[1]] = tmp
                prev[edge[1]] = edge[0]
                
    result = [tar]
    while tar != src:
        tar = prev[tar]
        result.insert(0, tar)
    print(result)
