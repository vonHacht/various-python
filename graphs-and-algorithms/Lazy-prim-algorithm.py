from queue import PriorityQueue


class Vertex:

    def __init__(self, name):
        # vertex label
        self.name = name
        # edges connected to this vertex
        self.edges = []
        # visited flag
        self.visited = False

    # method to connect vertices through bi-directional edges
    def connect(self, ad_vertex, edge_cost):
        global totalEdges
        self.edges.append(Edge(self, ad_vertex, edge_cost))
        ad_vertex.edges.append(Edge(ad_vertex, self, edge_cost))
        totalEdges += 2

    # string representation of the vertex class
    def __repr__(self):
        return self.name


class Edge:

    def __init__(self, _from, _to, _cost):
        # from vertex
        self._from = _from
        # to vertex
        self._to = _to
        # edge weight or cost
        self._cost = _cost

    # method to compare two edges (used by the priority queue)
    def __lt__(self, other):
        if isinstance(other, Edge):
            return self._cost < other._cost
        return False

    # string representation of the edge class
    def __repr__(self):
        return f"{self._from}-----{self._to}"


class Prims:

    def __init__(self):
        self.pqueue = PriorityQueue()
        self.mst = []
        self.totalCost = 0

    # function implementing Prim's algorithm
    def findMST(self, s):
        global totalEdges

        # add all edges of the starting vertex
        self.addEdges(s)
        edgeCount = 0
        '''
          hunt for low costs edges using PriorityQueue
          until all the edges are discovered
        '''
        while not self.pqueue.empty() and edgeCount != totalEdges:
            # pop the low cost edge from PriorityQueue
            minEdge = self.pqueue.get()
            '''
              do not add edges leading to-
              already visited vertices
            '''
            if minEdge._to.visited:
                continue
            else:
                # increment count and add edge to MST
                edgeCount += 1
                self.totalCost += minEdge._cost
                self.mst.append(minEdge)
                self.addEdges(minEdge._to)
        '''
          if not all edges are dicovered, then probalbly the
          given graph is dicsconnected, hence MST is not possible.
        '''
        return edgeCount != totalEdges

    # function add edges connected with a vertex to the priority queue
    def addEdges(self, s):
        s.visited = True
        for edge in s.edges:
            if not edge._to.visited:
                self.pqueue.put(edge)


if __name__ == '__main__':
    # total number of edges
    totalEdges = 0

    # vertices of the graph
    vertices = [
        Vertex('A'),
        Vertex('B'),
        Vertex('C'),
        Vertex('D'),
        Vertex('E')
    ]

    # connecting vertices
    vertices[0].connect(vertices[1], 3)
    vertices[0].connect(vertices[3], 5)
    vertices[1].connect(vertices[2], 2)
    vertices[1].connect(vertices[3], 10)
    vertices[2].connect(vertices[3], 7)
    vertices[2].connect(vertices[4], 8)
    vertices[3].connect(vertices[4], 1)

    # driver code
    prims = Prims()
    if prims.findMST(vertices[0]):
        print(prims.mst)
        print("Total Cost: ", prims.totalCost)
    else:
        print("MST not possible for given graph")
