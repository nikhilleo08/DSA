# What Is a Graph?

## Definition
- A Graph is a data structure made up of:
    - Nodes (aka vertices): entities or data points.
    - Edges: connections (or relationships) between those nodes.
- Think of a graph as a network of connections — like cities connected by roads, or users connected in a social network.

## Real-World Examples

| Real-World System    | Nodes Represent    | Edges Represent                     |
| -------------------- | ------------------ | ----------------------------------- |
| Google Maps          | Locations (cities) | Roads (can have weights = distance) |
| Facebook/LinkedIn    | Users              | Friendships / Connections           |
| Web Page Crawler     | Webpages           | Links between them                  |
| Git Commits          | Commits            | Parent-child history                |
| Package Dependencies | Software Packages  | Dependencies (A depends on B)       |

## Types of Graphs
Understanding the types of graphs helps you choose the right algorithm or implementation.
- Directed vs Undirected
    - Undirected: Edge goes both ways.
        - eg. Facebook friendship (A ↔ B)
    - Directed: Edge has a direction.
        - ef. Twitter follow (A → B)
- Weighted vs Unweighted
    - Unweighted: All edges are equal.
    - Weighted: Each edge has a value (distance, cost, time, etc.)
- Cyclic vs Acyclic
    - Cyclic: A cycle exists (you can go in a loop).
    - Acyclic: No cycles.
- Connected vs Disconnected
    - Connected: All nodes are reachable.
    - Disconnected: Some nodes are isolated.
- Sparse vs Dense
    - Sparse: Very few edges (e.g., tree).
    - Dense: Lots of edges (almost every node is connected to every other).

## Why Are Graphs Tricky?
- No strict structure (unlike trees or arrays).
- Multiple valid representations (adjacency list, matrix, etc.).
- Paths, cycles, weights, and directions all add complexity.

## Summary So Far
- ✅ Graph = Nodes + Edges
- ✅ Can be directed/undirected, weighted/unweighted
- ✅ Used in maps, social networks, web crawlers, Git, etc.

# Visualizing Graph Types
## A. Undirected Graph
```markdown
A ----- B
|       |
|       |
C ----- D
```
Edges are bidirectional — if you can go from A to B, you can also go from B to A.

## B. Directed Graph
```markdown
A → B → C
↑       ↓
← ← ← ← D
```
Edges are unidirectional — A can go to B, but not vice versa unless a reverse edge exists.

## C. Weighted Graph
```markdown
A --2-- B
|      /
4     1
|   /
C
```
- Each edge has a weight (like distance, time, or cost).
- E.g., going from A to B costs 2.

## D. Cyclic Graph
```markdown
A → B → C
↑     ↓
← ← ←
```
You can go in a loop (cycle: A → B → C → A).

## E. Acyclic Graph (DAG)
```markdown
A → B → D
    ↓
    C
```
- There are no cycles — you can’t return to a previously visited node.
- Very useful in task scheduling.

## Summary
- Visuals help you intuitively grasp direction, weight, and cycles.
- Always identify the type of graph before solving a problem.

# Graph Representations
There are 3 common ways to represent graphs in code:
| Representation       | Space    | When to Use                 |
| -------------------- | -------- | --------------------------- |
| **Adjacency List**   | O(V + E) | Sparse graphs (most common) |
| **Adjacency Matrix** | O(V²)    | Dense graphs                |
| **Edge List**        | O(E)     | Simple storage of all edges |

Let’s go through them one by one with examples.

## Adjacency List
Stores a dictionary or map of each node → its neighbors.

Example:
Undirected graph:
```markdown
A -- B
|    
C
```

Representation in Python

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
```

- Efficient for traversal
- Easy to add/remove edges
- Best for interviews

## Adjacency Matrix
- Stores a 2D grid (V x V).
- Value is 1 (or weight) if edge exists.
Same graph: 
```python
   A  B  C
A [0, 1, 1]
B [1, 0, 0]
C [1, 0, 0]
```
- Faster edge lookup: O(1)
- Wastes space if graph is sparse


## Edge List
- Just store edges as a list of pairs (or triplets if weighted):
```python
edges = [
    ('A', 'B'),
    ('A', 'C')
]
```
- Very compact
- No fast lookups
- Great for algorithms like Kruskal’s

## Summary of Representations
| Representation   | Pros                         | Cons               |
| ---------------- | ---------------------------- | ------------------ |
| Adjacency List   | Space efficient, easy to use | Slower edge lookup |
| Adjacency Matrix | Fast edge check (O(1))       | O(V²) space        |
| Edge List        | Compact, algorithm friendly  | No fast traversal  |
