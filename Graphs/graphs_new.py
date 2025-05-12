class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)
        
        if v2 not in self.graph[v1]:
            self.graph[v1].append(v2)
        if v1 not in self.graph[v2]:
            self.graph[v2].append(v1)
    
    def remove_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph[v1]:
            self.graph[v1].remove(v2)
        if v2 in self.graph and v1 in self.graph[v2]:
            self.graph[v2].remove(v1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbour in self.graph[vertex]:
                self.graph[neighbour].remove(vertex)
            del self.graph[vertex]

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")


graph = Graph()
graph.add_vertex('A')    
graph.add_vertex('B')    
graph.add_vertex('C')
graph.print_graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.print_graph()
print('NEW GRAPH')
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
print('Before removing edge from "C" to "A"')
g.print_graph()
g.remove_edge('C','A')
print('After removing edge from "C" to "A"')
g.print_graph()
graph.print_graph()
graph.remove_vertex('C')
graph.print_graph()