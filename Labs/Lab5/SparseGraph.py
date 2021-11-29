#
# Created by Yong on 11/21/2021
#

class SGraph:
    
    # Internal class Vertex
    class Vertex:
        def __init__(self, name):
            self.name = name
            self.neighbors = {}
            
    def __init__(self):
        self.vertices = {}
        self.verticesNum = 0
        self.edges = {}
        self.edgesNum = 0
    
    def AddEdge(self, u, v, weight):
        if u in self.vertices.keys() and v in self.vertices.keys():
            self.edges[(u, v)] = weight
            self.edgesNum += 1
        else:
            print("no such vertex (AddEdge)")
        
    def RemoveEdge(self, u, v):
        if (u,v) in self.edges.keys():
            self.edges.pop((u, v))
            self.edgesNum -= 1
            self.RemoveVertex(u)
            self.RemoveVertex(v)
        else:
            print("no such edge (AddEdge)")
        
    def AddVertex(self, v):
        if v not in self.vertices.keys():
            newVertex = self.Vertex(v)
            self.vertices[v] = newVertex
            self.verticesNum += 1
        
    def RemoveVertex(self, v):
        if v in self.vertices.keys():
            self.vertices.pop(v)
            self.verticesNum -= 1
        else:
            print("no such vertex")
            return
        for each in self.edges.keys():
            if v in each:
                self.edges.pop(each)
            
    def IsAdjacent(self, u, v):
        if u in self.vertices.keys() and v in self.vertices.key():
            if (u, v) in self.edges.keys() or (v, u) in self.edges.keys():
                return True
            else:
                return False
        else:
            print("no such vertex")
            return False
        
    def GetEdgeWeight(self, u, v):
        if u in self.vertices.keys() and v in self.vertices.keys():
            if (u, v) in self.edges.keys():
                return self.edges[(u, v)]
        print("no such edge")
        
    def SetEdgeWeight(self, u, v, weight):
        if u in self.vertices.keys() and v in self.vertices.keys():
            if (u, v) in self.edges.keys():
                self.edges[(u, v)] = weight
        print("no such edge")
            
    def GetVertexValue(self):
        print(self.vertices)
        
    def SetVertexValue(self, v, value):
        if v in self.vertices.keys():
            self.vertices[v] = value
        else:
            print("no such vertex")
