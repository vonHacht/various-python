class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1


def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((vertex, neighbor, weight))

    # Sort edges by weight in ascending order
    edges.sort(key=lambda x: x[2])

    # Initialize disjoint set
    vertices = set(vertex for edge in edges for vertex in edge[:2])
    disjoint_set = DisjointSet(vertices)

    # Initialize minimum spanning tree
    minimum_spanning_tree = []

    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree


if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': {
            'B': 1,
            'C': 4
        },
        'B': {
            'A': 1,
            'C': 2,
            'D': 5
        },
        'C': {
            'A': 4,
            'B': 2,
            'D': 1
        },
        'D': {
            'B': 5,
            'C': 1
        }
    }

    # Run Kruskal's algorithm
    result = kruskal(graph)

    # Print the minimum spanning tree
    for edge in result:
        print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
