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
            self.adj_list[node] = set()
    
    def link_nodes(self, node1, node2):
        """Function to link 2 nodes into the graph"""
        if node1 not in self.adj_list:
            print(f"Node {node1} does not exist. Please add it first.")
            return
        if node2 not in self.adj_list:
            print(f"Node {node2} does not exist. Please add it first.")
            return

        self.adj_list[node1].add(node2)
        if not self.is_directed:
            self.adj_list[node2].add(node1)
    
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
            self.adj_list[parent].discard(connection)  # ✅ Use discard() to avoid errors
        else:
            print(f'Parent node {parent} not found in graph')

        if not self.is_directed and connection in self.adj_list:
            self.adj_list[connection].discard(parent)

    def display(self):
        """Prints the adjacency list of the graph."""
        for vertex, edges in self.adj_list.items():
            print(vertex, ":", edges if len(edges) else None)

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
g.display()
g.remove_node(1)
print('After removing node 1')
g.display()
g.remove_node(2)
print('After removing node 2')
g.display()
g.remove_node(5)
g.display()

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