class Graph:

    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight):

        if len(self.edges) < u + 1:
            self.edges.append([0] * (v + 1))

        longest = v + 1
        for i in self.edges:
            if len(i) > longest:
                longest = len(i)

        index = 0
        for i in self.edges:
            if len(i) < longest:
                tmp = [0] * longest
                for j in range(0, len(i)):
                    tmp[j] = i[j]
                self.edges[index] = tmp

            index += 1

        self.edges[u][v] = weight

    def __str__(self):
        ret = ""

        for i in self.edges:
            ret += f"{i}\n"

        return ret

    @property
    def vertices(self):
        return len(self.edges)


if __name__ == "__main__":
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
    print(str(g))
    print(g.vertices())
