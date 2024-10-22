"""
Dijkstras Algorithm for Single Source Shortest Path Problem.
"""

import heapq

class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight= weight
        self.start_vertex= start_vertex
        self.target_vertex= target_vertex

class Node:

    def __init__(self, name):
        self.name= name
        self.visited= False
        # previous node to come to this node
        self.predecessor= None
        self.neighbours= []
        self.min_distance= float('inf') 

    def __lt__(self, otherNode):
        return self.min_distance < otherNode.min_distance
    
    def addEdge(self, weight, destination_vertex):
        edge= Edge(weight, self, destination_vertex)
        self.neighbours.append(edge)

class Dijkstras:

    def __init__(self):
        self.heap= []

    def calculate(self, start_vertex):
        start_vertex.min_distance= 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            # pop element with lowest distance
            actual_vertex= heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbours
            for edge in actual_vertex.neighbours:
                start= edge.start_vertex
                target= edge.target_vertex
                new_distance= start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance= new_distance
                    target.predecessor= start
                    # update the heap
                    heapq.heappush(self.heap, target)
            
            actual_vertex.visited= True

    def getShortestPath(self, vertex):
        print(f"The Shortest path to the vertex: {vertex.min_distance}")
        actual_vertex= vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end= " ")
            actual_vertex= actual_vertex.predecessor

# Step 1: Create Nodes

nodeA= Node('A')
nodeB= Node('B')
nodeC= Node('C')
nodeD= Node('D')
nodeE= Node('E')
nodeF= Node('F')
nodeG= Node('G')
nodeH= Node('H')

# Step 2: Create edges to created nodes.

nodeA.addEdge(6, nodeB)
nodeA.addEdge(10, nodeC)
nodeA.addEdge(9, nodeD)

nodeB.addEdge(5, nodeD)
nodeB.addEdge(16, nodeE)
nodeB.addEdge(13, nodeF)

nodeC.addEdge(6, nodeD)
nodeC.addEdge(21, nodeG)
nodeC.addEdge(5, nodeH)

nodeD.addEdge(8, nodeF)
nodeD.addEdge(7, nodeH)

nodeE.addEdge(10, nodeG)

nodeF.addEdge(4, nodeE)
nodeF.addEdge(12, nodeG)

nodeH.addEdge(2, nodeF)
nodeH.addEdge(14, nodeG)

algorithm= Dijkstras()
algorithm.calculate(nodeA)
algorithm.getShortestPath(nodeE)
