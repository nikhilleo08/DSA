class Graph:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed
    
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
        if not self.directed and v1 not in self.graph[v2]:
            self.graph[v2].append(v1)
    
    def remove_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph[v1]:
            self.graph[v1].remove(v2)
        if not self.directerd and v2 in self.graph and v1 in self.graph[v2]:
            self.graph[v2].remove(v1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbour in self.graph[vertex]:
                self.graph[neighbour].remove(vertex)
            del self.graph[vertex]

        # Remove incoming edges to this vertex (only needed for directed graphs)
        for v in self.graph:
            if vertex in self.graph[v]:
                self.graph[v].remove(vertex)

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")


g = Graph(directed=False)
g.add_edge("A", "B")
g.add_edge("B", "C")
g.print_graph()


g = Graph(directed=True)
g.add_edge("A", "B")
g.add_edge("B", "C")
g.print_graph()
