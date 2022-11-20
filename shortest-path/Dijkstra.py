from queue import PriorityQueue

from MatrixGraph import MatrixGraph


def create_graph() -> MatrixGraph:
    g = MatrixGraph()
    g.add_edge(0, 0, 0)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 0, 4)
    g.add_edge(1, 1, 0)
    g.add_edge(1, 2, 6)
    g.add_edge(2, 0, 7)
    g.add_edge(2, 1, 8)
    g.add_edge(2, 2, 0)
    return g


def dijkstra(graph: MatrixGraph, start: int):
    D = {v: float('inf') for v in range(graph.vertices)}
    D[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))
    visited = []

    print(f"== Starting at {start}, max vertices {graph.vertices} ==")

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        print(f"Running vertex {current_vertex}")
        for neighbor in range(graph.vertices):
            print(f"Visit neighbor {neighbor} ==>")

            if graph.matrix[current_vertex][neighbor] != 0:
                distance = graph.matrix[current_vertex][neighbor]
                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        print(
                            f"From {start} to {current_vertex},{neighbor} cost {new_cost}"
                        )
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


if __name__ == "__main__":
    graph = MatrixGraph(template=True)
    print(str(graph))
    print(dijkstra(graph, 0))
