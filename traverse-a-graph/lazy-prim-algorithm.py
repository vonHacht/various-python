import heapq


class LazyPrimMST:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.minimum_spanning_tree = []

    def lazy_prim(self, start_node):
        self.visit(start_node)
        priority_queue = self.get_edges(start_node)

        while priority_queue:
            edge = heapq.heappop(priority_queue)
            vertex1, vertex2, weight = edge

            if vertex1 in self.visited and vertex2 in self.visited:
                continue

            self.minimum_spanning_tree.append(edge)

            if vertex1 not in self.visited:
                self.visit(vertex1)
                priority_queue.extend(self.get_edges(vertex1))
            elif vertex2 not in self.visited:
                self.visit(vertex2)
                priority_queue.extend(self.get_edges(vertex2))

    def visit(self, vertex):
        self.visited.add(vertex)

    def get_edges(self, vertex):
        edges = []
        for neighbor, weight in self.graph[vertex].items():
            if neighbor not in self.visited:
                heapq.heappush(edges, (vertex, neighbor, weight))
        return edges


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

    # Create an instance of LazyPrimMST
    lazy_prim = LazyPrimMST(graph)

    # Run Lazy Prim's algorithm starting from node 'A'
    lazy_prim.lazy_prim('A')

    # Print the minimum spanning tree
    for edge in lazy_prim.minimum_spanning_tree:
        print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
