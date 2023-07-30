class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self._insert(node, self.root)

    def _insert(self, node, current):
        if node.value < current.value:
            if current.left is None:
                current.left = node
            else:
                self._insert(node, current.left)
        else:
            if current.right is None:
                current.right = node
            else:
                self._insert(node, current.right)


def linear_test(N: int, x: list[int]):
    if N != len(x):
        raise Exception("...")

    result = True

    keep = []

    for n in range(0, N):
        keep.append(x[n])

        if len(keep) == 3:
            if keep[0] < keep[1]:
                if keep[0] > keep[2]:
                    result = False
                    break

            if keep[0] > keep[1]:
                if keep[0] < keep[2]:
                    result = False
                    break

            keep.pop(0)

    return result


if __name__ == "__main__":
    Nn = 5

    success = [4, 0, 1, 3, 2]
    fail = [4, 0, 5, 3, 2]

    print(linear_test(Nn, success))
