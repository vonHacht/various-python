class MatrixGraph:

    def __init__(self, template=False):
        self._matrix = [[0]]

        if template:
            self._template()

    def add_edge_2(self, u, v, weight):
        self.add_edge(u, v, weight)
        self.add_edge(v, u, weight)

    def add_edge(self, u: int, v: int, weight: int):
        hz = (u + 1) - len(self._matrix)

        if hz >= 1:
            for i in range(0, hz):
                self._matrix.append([0] * (v + 1))

        vt = (v + 1) - len(self._matrix[u])

        if vt >= 1:
            new = [0] * (v + 1)
            for i in range(0, len(self._matrix[u])):
                new[i] = self._matrix[u][i]
            self._matrix[u] = new

        longest = self._longest()

        for i in range(0, len(self._matrix)):
            for j in range(0, longest - len(self._matrix[i])):
                self._matrix[i].append(0)

        self._matrix[u][v] = weight

    def __str__(self):
        ret = ""

        for i in self._matrix:
            ret += f"{i}\n"

        return ret

    @property
    def matrix(self):
        return self._matrix

    @property
    def vertices(self):
        return len(self._matrix)

    def _longest(self):
        longest = 0
        for i in range(0, len(self._matrix)):
            if len(self._matrix[i]) > longest:
                longest = len(self._matrix[i])

        return longest

    def _template(self):
        for i in [(0, 1, 4), (0, 6, 7), (1, 6, 11), (1, 7, 20), (1, 2, 9),
                  (2, 3, 6), (2, 4, 2), (3, 4, 10), (3, 5, 5), (4, 5, 15),
                  (4, 7, 1), (4, 8, 5), (5, 8, 12), (6, 7, 1), (7, 8, 3)]:
            self.add_edge_2(i[0], i[1], i[2])


if __name__ == "__main__":
    """
    [0, 4, 0, 0, 0, 0, 7, 0, 0]
    [4, 0, 9, 0, 0, 0, 11, 20, 0]
    [0, 9, 0, 6, 2, 0, 0, 0, 0]
    [0, 0, 6, 0, 10, 5, 0, 0, 0]
    [0, 0, 2, 10, 0, 15, 0, 1, 5]
    [0, 0, 0, 5, 15, 0, 0, 0, 12]
    [7, 11, 0, 0, 0, 0, 0, 1, 0]
    [0, 20, 0, 0, 1, 0, 1, 0, 3]
    [0, 0, 0, 0, 5, 12, 0, 3, 0]
    """
    g = MatrixGraph(template=True)
    print(str(g))
    print(g.vertices)
