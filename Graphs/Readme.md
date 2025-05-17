# Graphs in Python

## What is Graph Data Structure?
Graph is a non-linear data structure consisting of vertices and edges. The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(V, E).

Imagine a game of football as a web of connections, where players are the nodes and their interactions on the field are the edges. This web of connections is exactly what a graph data structure represents, and it’s the key to unlocking insights into team performance and player dynamics in sports.

![alt text](./assets/image.png)

## Components of Graph Data Structure
- **Vertices**: Vertices are the fundamental units of the graph. Sometimes, vertices are also known as vertex or nodes. Every node/vertex can be labeled or unlabelled.

- **Edges**: Edges are drawn or used to connect two nodes of the graph. It can be ordered pair of nodes in a directed graph. Edges can connect any two nodes in any possible way. There are no rules. Sometimes, edges are also known as arcs. Every edge can be labelled/unlabelled.

## Types Of Graphs in Data Structure and Algorithms
- **Null Graph**
    - A graph is known as a null graph if there are no edges in the graph.
- **Trivial Graph**
    - Graph having only a single vertex, it is also the smallest graph possible.

![alt text](./assets/image-1.png)

- Undirected Graph
    - A graph in which edges do not have any direction. That is the nodes are unordered pairs in the definition of every edge. 

- Directed Graph
    - A graph in which edge has direction. That is the nodes are ordered pairs in the definition of every edge.

![alt text](./assets/image-2.png)

- Connected Graph
    - The graph in which from one node we can visit any other node in the graph is known as a connected graph. 

- Disconnected Graph
    - The graph in which at least one node is not reachable from a node is known as a disconnected graph.

![alt text](./assets/image-3.png)

- Regular Graph
    - The graph in which the degree of every vertex is equal to K is called K regular graph.

- Complete Graph
    - The graph in which from each node there is an edge to each other node.

![alt text](./assets/image-4.png)

- Cycle Graph
    - The graph in which the graph is a cycle in itself, the minimum value of degree of each vertex is 2. 

- Cyclic Graph
    - A graph containing at least one cycle is known as a Cyclic graph.

![alt text](./assets/image-5.png)

- Directed Acyclic Graph
    - A Directed Graph that does not contain any cycle. 

- Bipartite Graph
    - A graph in which vertex can be divided into two sets such that vertex in each set does not contain any edge between them.

![alt text](./assets/image-6.png)

- Weighted Graph
    - A graph in which the edges are already specified with suitable weight is known as a weighted graph. 
    - Weighted graphs can be further classified as directed weighted graphs and undirected weighted graphs. 


## Representation of Graph Data Structure:
There are multiple ways to store a graph: The following are the most common representations.

1) Adjacency Matrix
2) Adjacency List

### Adjacency Matrix Representation of Graph Data Structure:
In this method, the graph is stored in the form of the 2D matrix where rows and columns denote vertices. Each entry in the matrix represents the weight of the edge between those vertices. 

![alt text](./assets/image-7.png)


### Adjacency List Representation of Graph:
This graph is represented as a collection of linked lists. There is an array of pointer which points to the edges connected to that vertex. 

![alt text](./assets/image-8.png)

### Comparison between Adjacency Matrix and Adjacency List
When the graph contains a large number of edges then it is good to store it as a matrix because only some entries in the matrix will be empty. An algorithm such as Prim’s and Dijkstra adjacency matrix is used to have less complexity.

![alt text](./assets/image-9.png)

# Problems
| Solved | Phase | Topic                        | Difficulty | Problem Title | Platform | Link |
|--------|-------|------------------------------|------------|---------------|----------|------|
|Unsolved | 1     | Graph Basics & Traversals    | Easy       | DFS of Graph | GFG      | https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1 |
|Unsolved | 1     | Graph Basics & Traversals    | Easy       | BFS of Graph | GFG      | https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1 |
|Unsolved | 1     | Graph Basics & Traversals    | Easy       | Flood Fill | LeetCode | https://leetcode.com/problems/flood-fill/ |
|Unsolved | 1     | Graph Basics & Traversals    | Easy       | The Maze | LeetCode | https://leetcode.com/problems/the-maze/ |
|Unsolved | 1     | Graph Basics & Traversals    | Medium     | Number of Provinces | LeetCode | https://leetcode.com/problems/number-of-provinces/ |
|Unsolved | 1     | Graph Basics & Traversals    | Medium     | Rotting Oranges | LeetCode | https://leetcode.com/problems/rotting-oranges/ |
|Unsolved | 1     | Graph Basics & Traversals    | Medium     | Walls and Gates | LeetCode | https://leetcode.com/problems/walls-and-gates/ |
|Unsolved | 1     | Graph Basics & Traversals    | Medium     | Shortest Path in Binary Matrix | LeetCode | https://leetcode.com/problems/shortest-path-in-binary-matrix/ |
|Unsolved | 1     | Graph Basics & Traversals    | Hard       | Cut Off Trees | LeetCode | https://leetcode.com/problems/cut-off-trees-for-golf-event/ |
|Unsolved | 1     | Graph Basics & Traversals    | Hard       | The Maze III | LeetCode | https://leetcode.com/problems/the-maze-iii/ |
|Unsolved | 2     | Connected Components         | Easy       | Number of Islands | LeetCode | https://leetcode.com/problems/number-of-islands/ |
|Unsolved | 2     | Connected Components         | Easy       | Max Area of Island | LeetCode | https://leetcode.com/problems/max-area-of-island/ |
|Unsolved | 2     | Connected Components         | Easy       | Find the Town Judge | LeetCode | https://leetcode.com/problems/find-the-town-judge/ |
|Unsolved | 2     | Connected Components         | Easy       | Find Center of Star Graph | LeetCode | https://leetcode.com/problems/find-center-of-star-graph/ |
|Unsolved | 2     | Connected Components         | Medium     | Count Connected Components | LeetCode | https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/ |
|Unsolved | 2     | Connected Components         | Medium     | Surrounded Regions | LeetCode | https://leetcode.com/problems/surrounded-regions/ |
|Unsolved | 2     | Connected Components         | Medium     | Pacific Atlantic Water Flow | LeetCode | https://leetcode.com/problems/pacific-atlantic-water-flow/ |
|Unsolved | 2     | Connected Components         | Medium     | Color Border | LeetCode | https://leetcode.com/problems/coloring-a-border/ |
|Unsolved | 2     | Connected Components         | Hard       | Number of Distinct Islands II | LeetCode | https://leetcode.com/problems/number-of-distinct-islands-ii/ |
|Unsolved | 2     | Connected Components         | Hard       | Remove Max Edges to Keep Graph Traversable | LeetCode | https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/ |
|Unsolved | 3     | Cycle Detection              | Easy       | Find if Path Exists in Graph | LeetCode | https://leetcode.com/problems/find-if-path-exists-in-graph/ |
|Unsolved | 3     | Cycle Detection              | Easy       | Path Exists in Graph | LeetCode | https://leetcode.com/problems/path-with-maximum-probability/ |
|Unsolved | 3     | Cycle Detection              | Easy       | Find Redundant Connection | LeetCode | https://leetcode.com/problems/redundant-connection/ |
|Unsolved | 3     | Cycle Detection              | Easy       | Detect Cycle in Undirected Graph | GFG | https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1 |
|Unsolved | 3     | Cycle Detection              | Medium     | Course Schedule | LeetCode | https://leetcode.com/problems/course-schedule/ |
|Unsolved | 3     | Cycle Detection              | Medium     | Course Schedule II | LeetCode | https://leetcode.com/problems/course-schedule-ii/ |
|Unsolved | 3     | Cycle Detection              | Medium     | Detect Cycle in Directed Graph | GFG | https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1 |
|Unsolved | 3     | Cycle Detection              | Medium     | Minimum Height Trees | LeetCode | https://leetcode.com/problems/minimum-height-trees/ |
|Unsolved | 3     | Cycle Detection              | Hard       | Alien Dictionary | LeetCode | https://leetcode.com/problems/alien-dictionary/ |
|Unsolved | 3     | Cycle Detection              | Hard       | Longest Cycle in a Graph | LeetCode | https://leetcode.com/problems/longest-cycle-in-a-graph/ |
|Unsolved | 4     | Topological Sort             | Easy       | All Tasks Scheduling Orders | Educative | https://www.educative.io/courses/grokking-the-coding-interview/xV4BvG1qBAK |
|Unsolved | 4     | Topological Sort             | Easy       | Tasks Scheduling | Educative | https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00 |
|Unsolved | 4     | Topological Sort             | Easy       | Find Order of Characters | GFG | https://practice.geeksforgeeks.org/problems/alien-dictionary/1 |
|Unsolved | 4     | Topological Sort             | Easy       | Prerequisite Tasks | GFG | https://practice.geeksforgeeks.org/problems/prerequisite-tasks/1 |
|Unsolved | 4     | Topological Sort             | Medium     | Parallel Courses | LeetCode | https://leetcode.com/problems/parallel-courses/ |
|Unsolved | 4     | Topological Sort             | Medium     | Parallel Courses III | LeetCode | https://leetcode.com/problems/parallel-courses-iii/ |
|Unsolved | 4     | Topological Sort             | Medium     | Minimum Time to Complete All Tasks | LeetCode | https://leetcode.com/problems/minimum-time-to-complete-all-tasks/ |
|Unsolved | 4     | Topological Sort             | Medium     | Sequence Reconstruction | LeetCode | https://leetcode.com/problems/sequence-reconstruction/ |
|Unsolved | 4     | Topological Sort             | Hard       | Jump Game IV | LeetCode | https://leetcode.com/problems/jump-game-iv/ |
|Unsolved | 4     | Topological Sort             | Hard       | Minimum Height Trees (Hard variant) | LeetCode | https://leetcode.com/problems/minimum-height-trees/ |
|Unsolved | 5     | Shortest Path Algorithms     | Easy       | Cheapest Flights Within K Stops | LeetCode | https://leetcode.com/problems/cheapest-flights-within-k-stops/ |
|Unsolved | 5     | Shortest Path Algorithms     | Easy       | Dijkstra Implementation | GFG | https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1 |
|Unsolved | 5     | Shortest Path Algorithms     | Easy       | Bellman-Ford | GFG | https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1 |
|Unsolved | 5     | Shortest Path Algorithms     | Easy       | Minimum Time to Reach Destination | LeetCode | https://leetcode.com/problems/minimum-time-to-reach-destination-in-grid/ |
|Unsolved | 5     | Shortest Path Algorithms     | Medium     | Path with Minimum Effort | LeetCode | https://leetcode.com/problems/path-with-minimum-effort/ |
|Unsolved | 5     | Shortest Path Algorithms     | Medium     | Network Delay Time | LeetCode | https://leetcode.com/problems/network-delay-time/ |
|Unsolved | 5     | Shortest Path Algorithms     | Medium     | Find the City With the Smallest Number of Neighbors | LeetCode | https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/ |
|Unsolved | 5     | Shortest Path Algorithms     | Medium     | Minimum Cost to Make at Least One Valid Path | LeetCode | https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/ |
|Unsolved | 5     | Shortest Path Algorithms     | Hard       | Minimum Obstacle Removal to Reach Corner | LeetCode | https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/ |
|Unsolved | 5     | Shortest Path Algorithms     | Hard       | Path With Minimum Effort (Hard variant) | LeetCode | https://leetcode.com/problems/path-with-minimum-effort/ |
|Unsolved | 6     | Union-Find                   | Easy       | Path Compression Explanation | GFG | https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1 |
|Unsolved | 6     | Union-Find                   | Easy       | Union By Rank | GFG | https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1 |
|Unsolved | 6     | Union-Find                   | Easy       | Satisfiability of Equality Equations | LeetCode | https://leetcode.com/problems/satisfiability-of-equality-equations/ |
|Unsolved | 6     | Union-Find                   | Easy       | Accounts Merge | LeetCode | https://leetcode.com/problems/accounts-merge/ |
|Unsolved | 6     | Union-Find                   | Medium     | Number of Islands II | LeetCode | https://leetcode.com/problems/number-of-islands-ii/ |
|Unsolved | 6     | Union-Find                   | Medium     | Redundant Connection II | LeetCode | https://leetcode.com/problems/redundant-connection-ii/ |
|Unsolved | 6     | Union-Find                   | Medium     | Most Stones Removed with Same Row or Column | LeetCode | https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/ |
|Unsolved | 6     | Union-Find                   | Medium     | Evaluate Division | LeetCode | https://leetcode.com/problems/evaluate-division/ |
|Unsolved | 6     | Union-Find                   | Hard       | Swim in Rising Water | LeetCode | https://leetcode.com/problems/swim-in-rising-water/ |
|Unsolved | 6     | Union-Find                   | Hard       | Bricks Falling When Hit | LeetCode | https://leetcode.com/problems/bricks-falling-when-hit/ |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Easy       | Kruskal’s Algorithm | GFG | https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1 |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Easy       | Prim’s Algorithm | GFG | https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1 |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Easy       | Connecting Cities With Minimum Cost | GFG | https://practice.geeksforgeeks.org/problems/connecting-the-graph/1 |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Easy       | Optimize Water Distribution | LeetCode | https://leetcode.com/problems/optimize-water-distribution-in-a-village/ |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Medium     | Connecting Islands | GFG | https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1 |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Medium     | Network Connection in Cities | LeetCode | https://leetcode.com/problems/network-connected-in-cities/ |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Medium     | Min Cost to Connect All Points | LeetCode | https://leetcode.com/problems/min-cost-to-connect-all-points/ |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Medium     | Smallest String With Swaps | LeetCode | https://leetcode.com/problems/smallest-string-with-swaps/ |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Hard       | Designing an Efficient Road Network | GFG | https://practice.geeksforgeeks.org/problems/designing-an-efficient-road-network/0 |
|Unsolved | 7     | MST (Minimum Spanning Tree) | Hard       | Min Cost to Supply Water | LeetCode | https://leetcode.com/problems/optimize-water-distribution-in-a-village/ |
|Unsolved | 8     | Advanced Problems            | Easy       | Graph Valid Tree | LeetCode | https://leetcode.com/problems/graph-valid-tree/ |
|Unsolved | 8     | Advanced Problems            | Easy       | Clone Graph | LeetCode | https://leetcode.com/problems/clone-graph/ |
|Unsolved | 8     | Advanced Problems            | Easy       | Reorder Routes to Make All Paths Lead to the City Zero | LeetCode | https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/ |
|Unsolved | 8     | Advanced Problems            | Easy       | Reconstruct Itinerary | LeetCode | https://leetcode.com/problems/reconstruct-itinerary/ |
|Unsolved | 8     | Advanced Problems            | Medium     | Word Ladder | LeetCode | https://leetcode.com/problems/word-ladder/ |
|Unsolved | 8     | Advanced Problems            | Medium     | Word Ladder II | LeetCode | https://leetcode.com/problems/word-ladder-ii/ |
|Unsolved | 8     | Advanced Problems            | Medium     | Strongly Connected Components (Kosaraju) | GFG | https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1 |
|Unsolved | 8     | Advanced Problems            | Medium     | Bridges in Graph | GFG | https://practice.geeksforgeeks.org/problems/bridge-edge-in-graph/1 |
|Unsolved | 8     | Advanced Problems            | Hard       | Critical Connections | LeetCode | https://leetcode.com/problems/critical-connections-in-a-network/ |
|Unsolved | 8     | Advanced Problems            | Hard       | Shortest Path Visiting All Nodes | LeetCode | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |
