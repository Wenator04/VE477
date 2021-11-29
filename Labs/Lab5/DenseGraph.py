#
# Created by Yong on 11/21/2021
#

class DGraph:
    
    # Internal class Vertex
    class Vertex:
        def __init__(self, name):
            self.name = name
            self.neighbors = {}
            
        def AddNeighbor(self, v, weight):
            self.neighbors[v] = weight
            
        def RemoveNeighbor(self, v):
            if v in self.neighbors:
                self.neighbors.pop(v)
            else:
                print("no such neighbor (RemoveNeighbor)")
            
    def __init__(self):
        self.vertices = {}
        self.verticesNum = 0
        
    def AddVertex(self, v):
        if v not in self.vertices:
            newVertex = self.Vertex(v)
            self.vertices[v] = newVertex
            self.verticesNum += 1
        
    def RemoveVertex(self, v):
        if v in self.vertices:
            self.vertices.pop(v)
            self.verticesNum -= 1
        else:
            print("no such vertex (RemoveVertex)")
            
    def AddEdge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].AddNeighbor(v, weight)
        else:
            print("no such vertex (AddEdge)")
        
    def RemoveEdge(self, u, v):
        self.vertices[u].RemoveNeighbor(v)
        
    def IsAdjacent(self, u, v):
        if u in self.vertices and v in self.vertices:
            if u in self.vertices[v].neighbors or v in self.vertices[u].neighbors:
                return True
            else:
                return False
        else:
            print("no such vertex (IsAdjacent)")
            return False
        
    def GetEdgeWeight(self, u, v):
        if u in self.vertices and v in self.vertices:
            return self.vertices[u].neighbors[v]
        else:
            print("no such edge (GetEdgeWeight)")
        
    def SetEdgeWeight(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].neighbors[v] = weight
        else:
            print("no such edge (SetEdgeWeight)")
            
    def GetVertexValue(self):
        print(self.vertices)
        
    def SetVertexValue(self, v, value):
        if v in self.vertices:
            self.vertices[v] = value
        else:
            print("no such vertex (SetVertexValue)")