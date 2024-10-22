from collections import deque

class Graph:

    def __init__(self, gdict= None):
        if gdict is None:
            gdict= {}
        else:
            self.gdict= gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


custom_dict= {
                'a': ['b', 'c'],
                'b': ['a', 'd', 'e'],
                'c': ['a', 'e'],
                'd': ['b', 'e', 'f'],
                'e': ['b', 'd'],
                'f': ['d', 'e']
            }

# graph= Graph(custom_dict)
# print(graph.gdict)
# graph.addEdge('e', 'c')
# print(graph.gdict)


class Graph1:

    def __init__(self):
        self.adjancency_list= {}

    def addVertex(self, vertex):
        if vertex not in self.adjancency_list.keys():
            self.adjancency_list[vertex]= []
            return True
        return False
    
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjancency_list.keys() or vertex2 in self.adjancency_list.keys():
            self.adjancency_list[vertex1].append(vertex2)
            self.adjancency_list[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjancency_list.keys() or vertex2 in self.adjancency_list.keys():
            self.adjancency_list[vertex1].remove(vertex2)
            self.adjancency_list[vertex2].remove(vertex1)
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjancency_list.keys():
            for other_vertex in self.adjancency_list[vertex]:
                self.adjancency_list[other_vertex].remove(vertex)
            del self.adjancency_list[vertex]
            return True
        return False

    def printGraph(self):
        for vertex in self.adjancency_list:
            print(vertex, ":", self.adjancency_list[vertex])

    def bfs(self, vertex):
        visited= set()
        visited.add(vertex)
        queue= deque([vertex])
        
        while queue:
            current_vertex= queue.popleft()
            print(current_vertex)
            
            for adjacent_vertex in self.adjancency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs(self, vertex):
        visited= set()
        stack= [vertex]
        while stack:
            current_vertex= stack.pop()
            
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            
            for adjancency_vertex in self.adjancency_list[current_vertex]:
                if adjancency_vertex not in visited:
                    stack.append(adjancency_vertex)


custom_graph= Graph1()
custom_graph.addVertex("A")
custom_graph.addVertex("B")
custom_graph.addVertex("C")
custom_graph.addVertex("D")
custom_graph.addVertex("E")
custom_graph.addEdge("A", "B")
custom_graph.addEdge("A", "C")
custom_graph.addEdge("B", "E")
custom_graph.addEdge("C", "D")
custom_graph.addEdge("D", "E")
# custom_graph.removeEdge("B","C")
custom_graph.printGraph()
print('-------BFS----')
custom_graph.bfs("A")
print('-------DFS----')
custom_graph.dfs("A")
# print("After Remvove Vertex")
# custom_graph.removeVertex("A")
# custom_graph.printGraph()
