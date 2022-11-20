from MatrixGraph import MatrixGraph


#def graphTraverse(graph: MatrixGraph):
#    Visited = set()
#    for V in graph.matrix:
#        if V not in Visited:
#            traverseDFS(graph, V, Visited)


def traverseDFS(G, v, visited):
    if v is None:
        v = G.matrix[0][0]

    if v not in visited:
        visited.add(v)
        PreVisit(G, v)
        for edge in G.outgoingEdges(v):
            traverseDFS(G, edge.end, visited)
        PostVisit(G, v)


if __name__ == "__main__":
    traverseDFS(MatrixGraph(template=True), None, set())

    pass
