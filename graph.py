from collections import defaultdict
from needs import *


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def utilsDFS(self,v,visited:set):
        visited.add(v)
        print(v,end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.utilsDFS(v=neighbour,visited=visited)
    def DFS(self,v):
        visited = set()
        self.utilsDFS(v=v,visited=visited)


# graph = Graph()
# graph.addEdge(0,1)
# graph.addEdge(0,2)
# graph.addEdge(0,3)

# graph.addEdge(1,0)

# graph.addEdge(2,0)
# graph.addEdge(2,3)
# graph.addEdge(2,4)

# graph.addEdge(3,0)
# graph.addEdge(3,2)

# graph.addEdge(4,2)

# graph.DFS(v=1)