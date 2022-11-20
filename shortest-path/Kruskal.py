def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def apply_union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(graph: list, vertices: int):
    result = []
    i, e = 0, 0
    edges = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(vertices):
        parent.append(node)
        rank.append(0)
    while e < vertices - 1:
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            apply_union(parent, rank, x, y)
    for u, v, weight in result:
        print("%d - %d: %d" % (u, v, weight))


if __name__ == "__main__":
    graph = [
        [0, 1, 4],
        [0, 2, 4],
        [1, 2, 2],
        [1, 0, 4],
        [2, 0, 4],
        [2, 1, 2],
        [2, 3, 3],
        [2, 5, 2],
        [2, 4, 4],
        [3, 2, 3],
        [3, 4, 3],
        [4, 2, 4],
        [4, 3, 3],
        [5, 2, 2],
        [5, 4, 3]
    ]
    kruskal(graph, 9)
