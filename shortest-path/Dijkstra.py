from queue import PriorityQueue

from Graph import Graph as Graph


def create_graph() -> Graph:
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3)
    return g


def dijkstra(graph: Graph, start: int):
    D = {v: float('inf') for v in range(graph.vertices)}
    D[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))
    visited = []

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in range(graph.vertices):
            print(f"{current_vertex}:{neighbor}")

            if graph.edges[current_vertex][neighbor] != 0:

                distance = graph.edges[current_vertex][neighbor]

                print(f"distance {graph.edges[current_vertex][neighbor]}")

                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


if __name__ == "__main__":
    graph = create_graph()
    print(str(graph))
    d = dijkstra(graph, 0)
    print(d)
