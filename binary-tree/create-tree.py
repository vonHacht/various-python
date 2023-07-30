from BinaryTree import BinaryTree, insert_left, insert_right, print_tree

#          1
#       /     \
#      2       3
#    /   \    /   \
#   6     7  8     9
#  / \
# 4   5

if __name__ == "__main__":

    # Create a binary tree with root value 1
    tree = BinaryTree(1)

    # Add left child with value 2 to root
    insert_left(tree.root, 2)

    # Add right child with value 3 to root
    insert_right(tree.root, 3)

    # Add left child with value 4 to left child of root
    insert_left(tree.root.left_child, 4)

    # Add right child with value 5 to right child of root
    insert_right(tree.root.right_child, 5)

    # Add left child with value 6 to left child of node 2
    insert_left(tree.root.left_child, 6)

    # Add right child with value 7 to right child of node 2
    insert_right(tree.root.left_child, 7)

    # Add left child with value 8 to left child of node 3
    insert_left(tree.root.right_child, 8)

    # Add right child with value 9 to right child of node 3
    insert_right(tree.root.right_child, 9)

    print_tree(tree.root)
