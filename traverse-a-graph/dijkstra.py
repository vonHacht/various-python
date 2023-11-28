import heapq


def dijkstra(graph, start):
    # Initialize distances to infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Use a priority queue (min heap) to track the nodes and their distances
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the current distance is greater than the known distance
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors and update distances
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


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

    # Start node
    start_node = 'A'

    # Run Dijkstra's algorithm
    result = dijkstra(graph, start_node)

    # Print the shortest distances from the start node to each node
    for node, distance in result.items():
        print(f"Shortest distance from {start_node} to {node}: {distance}")
