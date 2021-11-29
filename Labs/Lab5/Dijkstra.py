#
# Created by Yong on 11/22/2021
#

from FibonacciHeap import FibHeap
from DenseGraph import DGraph

if __name__ == "__main__":
    graph = DGraph()
    size = input()
    for i in range(int(size)):
        u, v, weight = input().split()
        graph.AddVertex(u)
        graph.AddVertex(v)
        graph.AddEdge(u, v, float(weight))
    src = input().strip()
    tar = input().strip()
    
    fibHeap = FibHeap()
    heapNodeIndex = {}
    dist = {}
    prev = {}
    visited = {}
    for node in graph.vertices:
        if node == src:
            dist[node] = 0.0
            prev[node] = None
            visited[node] = True
            heapNodeIndex[node] = fibHeap.insert(0.0, node)
        else:
            dist[node] = float('inf')
            prev[node] = None
            visited[node] = False
            heapNodeIndex[node] = fibHeap.insert(float('inf'), node)
          
    node = src
    while node != tar:
        node = fibHeap.extractMin().value
        print("======")
        print(node)
        visited[node] = True
        for neighbor in graph.vertices[node].neighbors:
            print(neighbor)
            if visited[neighbor]:
                continue
            tmp = dist[node] + graph.GetEdgeWeight(node, neighbor)
            if tmp < dist[neighbor]:
                dist[neighbor] = tmp
                prev[neighbor] = node
                fibHeap.decreaseKey(heapNodeIndex[neighbor], tmp)
        
    result = [tar]
    while tar != src:
        tar = prev[tar]
        result.insert(0, tar)
    print(result)
                

    