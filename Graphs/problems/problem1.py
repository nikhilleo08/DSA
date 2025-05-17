# Shortest Path from Source to Destination (Unweighted Graph)

# Problem Statement:
# Given an unweighted graph and a start and end node, find the length of the shortest path between them.
from collections import defaultdict, deque

def generate_graph(edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def get_distance(graph, source, dest):
    q = deque()
    visited = set()
    
    q.append([source, 0])
    visited.add(source)

    while q:
        node, dist = q.popleft()
        
        if node == dest:
            return dist

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append([neighbour, dist+1])
    return -1
            


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
print(get_distance(graph, 'A', 'F')) # 3
print(get_distance(graph, 'B', 'C')) # 2
print(get_distance(graph, 'D', 'E')) # 1
print(get_distance(graph, 'B', 'F')) # 2
print(get_distance(graph, 'D', 'C')) # 2

# A-----------B----------D
# |                     *|
# |                   *  |
# |                 *    |
# |               *      |   
# |             *        | 
# C-----------E----------F