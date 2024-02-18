class Node:
    right = None
    left = None
    value: str

    def __init__(self, value: str):
        self.value = value


class BinaryTree:
    root: Node = None
    size: int = 0
    heap: list = []

    def __init__(self, value):
        self.insert(value)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):

        if root is None:
            # if len(self.heap) == 5:  # our special case
            #    self.heap.append("")

            # self.heap.append(value)

            return Node(value)

        if value < root.value:  # left
            root.left = self._insert(root.left, value)
        else:  # right
            root.right = self._insert(root.right, value)

        return root

    def convertToBST(self):
        # convert special case heap
        self.root

        pass

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, root):
        if root is None: return

        print(root.value)

        if root.left is not None:
            self._traverse(root.left)
        else:
            self._traverse(root.right)

    def create_heap(self, root, heap=None, position=0):

        if heap is None:
            heap = []

        if root is None:
            return heap

        heap.append(root.value)

        if root.left is not None:
            self._traverse(root.left)
        else:
            self._traverse(root.right)



    def print_heap(self):
        print(self.heap)


if __name__ == "__main__":
    tree = BinaryTree("A")
    for value in ["B", "C", "D", "E", "F", "G", "H"]:
        tree.insert(value)

    # tree.print_heap()
    tree.traverse()
