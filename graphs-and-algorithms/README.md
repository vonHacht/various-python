# shortest path

## Theory

> Directed acyclic graph (DAG)
> ![Graph 1](img/DAG.png)

> Spanning tree
> ![Graph 1](img/Spanning_tree.png)
> Spanning tree with minimal weight: Minimal Spanning Tree (MST)

> Depth First Search (DFS)\
> Breadth First Search (BFS)

> Eulerian Circuit/Cycle - starts and ends in same vertex, only passes other edges once
> Hamiltonian Circuit/Cycle - only passes other vertex once

> **shortest path**\
> d(A, D) = 10 (**A**-->**C**-->**B**-->**D**)\
> d(E, B) = inf

> **weight of edge**\
> w(A, D) = 20
> w(A, B) = 10

> **shortest path from S to X**\
> d(S, X) = min( d(S, U) + w(U, X) )

> Summation
> ![Summation](img/summation.png)


![Graph 1](img/graph1.png)

## Graph translation

![Graph 2](img/graph2.png)

## Calculations with bytes

A - No. of bytes vertices index\
B - No. of bytes pointer\
C - No. of bytes weight

Adjacency matrix = A * |vertices^2|\
Link node = A + B + C\
Adjacency list = B * |vertices| + Link node * |edges|

![Graph 3](img/graph3.png)

## Time complexity

Dijkstra: O(|Num of Edges|+|Num of vertices|*log|Num of vertices|)

## Documentation

- [Graphs in Python: Theory and implementation](https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/).