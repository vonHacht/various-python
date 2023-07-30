class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def insert_left(parent_node, new_value):
    if parent_node.left_child is None:
        parent_node.left_child = Node(new_value)
    else:
        new_node = Node(new_value)
        new_node.left_child = parent_node.left_child
        parent_node.left_child = new_node


def insert_right(parent_node, new_value):
    if parent_node.right_child is None:
        parent_node.right_child = Node(new_value)
    else:
        new_node = Node(new_value)
        new_node.right_child = parent_node.right_child
        parent_node.right_child = new_node


def print_tree(node, level=0, char='-'):
    if node is not None:
        print_tree(node.right_child, level + 1, '/')
        print(' ' * 4 * level + char + str(node.value) + char)
        print_tree(node.left_child, level + 1, '\\')


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
