from collections import deque

class Graph:
    def __init__(self, directed=False):
        """
        Initialize a new directed/undirected graph.
        """
        self.adj_list = {}
        self.is_directed = directed
        print(f'Creating a {"directed" if directed else "undirected"} graph')

    def add_node(self, node):
        """Function to add node into the graph"""
        if node not in self.adj_list:
            self.adj_list[node] = []
    
    def link_nodes(self, node1, node2):
        """Function to link 2 nodes into the graph"""
        if node1 not in self.adj_list:
            print(f"Node {node1} does not exist. Please add it first.")
            return
        if node2 not in self.adj_list:
            print(f"Node {node2} does not exist. Please add it first.")
            return

        self.adj_list[node1].append(node2)
        if not self.is_directed:
            self.adj_list[node2].append(node1)
    
    def remove_node(self, node):
        """Function to remove a node from the graph"""
        if node in self.adj_list:
            for connection in list(self.adj_list[node]):
                self.unlink_nodes(node, connection) 
            del self.adj_list[node]
        else:
            print('Node not found in Graph, cannot remove the node:', node)

    def unlink_nodes(self, parent, connection):
        """Function to remove a node from the graph"""
        if parent in self.adj_list:
            self.adj_list[parent].remove(connection)
        else:
            print(f'Parent node {parent} not found in graph')

        if not self.is_directed and connection in self.adj_list:
            self.adj_list[connection].remove(parent)

    def display(self):
        """Prints the adjacency list of the graph."""
        for vertex, edges in self.adj_list.items():
            print(vertex, ":", edges if len(edges) else None)

class GraphTraversal:
    """Handles graph traversal without depending on Graph implementation."""
    def __init__(self, graph: Graph):
        print('Initialized Graph Traversal for the following graph')
        graph.display()
        self.graph = graph
        self.visited = set()

        
    def bfs(self, start):
        '''Breadth First Traversal for the Graph'''
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in self.visited:
                print(node, end='')
                self.visited.add(node)
                queue.extend(self.graph.adj_list[node])
        self.visited.clear()    
        
    def dfs(self, start):
        '''Depth First Traversal for the Graph'''
        if start not in self.visited:
            print(start, end='')
            self.visited.add(start)
        for neighbour in self.graph.adj_list[start]:
            if neighbour not in self.visited:
                self.dfs(neighbour)

g = Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.link_nodes(1,2)
g.link_nodes(1,4)
g.link_nodes(1,3)
g.link_nodes(2,3)
g.link_nodes(3,4)
g.link_nodes(2,4)
# g.display()
# g.remove_node(1)
# print('After removing node 1')
# g.display()
# g.remove_node(2)
# print('After removing node 2')
# g.display()
# g.remove_node(5)
g.display()
print()
traversal = GraphTraversal(g)
traversal.bfs(2)
print()

g1 = Graph()
g1.add_node(0)
g1.add_node(1)
g1.add_node(2)
g1.add_node(3)
g1.add_node(4)
g1.link_nodes(0,2)
g1.link_nodes(0,3)
g1.link_nodes(0,1)
g1.link_nodes(2,4)
g1.display()
print()
traversal_new = GraphTraversal(g1)
print('BFS Traversal of the Graph')
g1.display()
traversal_new.bfs(0)
print()
print()
print('DFS Traversal of the Graph')
g1.display()
traversal_new.dfs(0)
print()


# g = Graph(True)
# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
# g.add_node(4)
# g.link_nodes(1,2)
# g.link_nodes(2,3)
# g.link_nodes(3,4)
# g.link_nodes(2,4)
# g.display()