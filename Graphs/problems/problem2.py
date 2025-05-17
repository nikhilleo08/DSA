# Finding the Actual Shortest Path
# This builds on your previous solution and helps you understand how BFS keeps track of the path as it explores the graph.

# Goal:
# Instead of just returning the number of steps, we’ll return the full shortest path from source to destination.


# A-----------B----------D
# |                     *|
# |                   *  |
# |                 *    |
# |               *      |   
# |             *        | 
# C-----------E----------F

# A => F: [[A,B,D,F], [A,C,E,F]]
# A => B: [[A, B], [A,C,E,D,B], [A,C,E,F,D,B]]

from collections import defaultdict, deque

def generate_graph(edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def shortest_path_graph(graph, source, target):
    q = deque()
    visited = set()
    parent = { source: None }
    
    q.append(source)
    visited.add(source)
    
    while q:
        popped = q.popleft()
        
        if popped == target:
            break
            
        for neighbour in graph[popped]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = popped
                q.append(neighbour)
    
    if target not in parent:
        return None
    
    res = []
    current = target
    while current is not None:
        res.append(current)
        current = parent[current]
    return res[::-1]


edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "E"),
    ("D", "F"),
    ("E", "F")
]

graph = generate_graph(edges)
print(shortest_path_graph(graph, 'A', 'F')) # 3
print(shortest_path_graph(graph, 'B', 'C')) # 2
print(shortest_path_graph(graph, 'D', 'E')) # 1
print(shortest_path_graph(graph, 'B', 'F')) # 2
print(shortest_path_graph(graph, 'D', 'C')) # 2
