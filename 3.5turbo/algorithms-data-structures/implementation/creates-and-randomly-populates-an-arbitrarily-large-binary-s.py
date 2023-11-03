'''
Binary Search Tree:
- A binary search tree is a binary tree in which each node has a value greater than all the values in its left subtree and less than all the values in its right subtree.

Approach:
- To randomly populate an arbitrarily large binary search tree, we can generate a list of random values and then insert them into the binary search tree.

Steps:
1. Define the Node class to represent a node in the binary search tree.
2. Define the BinarySearchTree class with the following methods:
   - __init__(): Initializes an empty binary search tree.
   - insert(value): Inserts a value into the binary search tree.
   - get_random_tree(size): Generates a random binary search tree of the specified size.
   - inorder_traversal(node): Helper method to perform an inorder traversal of the binary search tree.
3. In the main part of the script, create an instance of the BinarySearchTree class and call the get_random_tree(size) method to generate a random binary search tree of a specified size.

'''

import random

# Node class to represent a node in the binary search tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinarySearchTree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Method to insert a value into the binary search tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Recursive method to insert a value into the binary search tree
    def _insert_recursive(self, curr_node, value):
        if value < curr_node.value:
            if curr_node.left is None:
                curr_node.left = Node(value)
            else:
                self._insert_recursive(curr_node.left, value)
        else:
            if curr_node.right is None:
                curr_node.right = Node(value)
            else:
                self._insert_recursive(curr_node.right, value)

    # Method to generate a random binary search tree of the specified size
    def get_random_tree(self, size):
        values = random.sample(range(1, 10000), size)  # Generate a list of random values
        for value in values:
            self.insert(value)  # Insert values into the binary search tree

    # Helper method to perform an inorder traversal of the binary search tree
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

# Create an instance of BinarySearchTree class
bst = BinarySearchTree()

# Generate a random binary search tree of size 10
bst.get_random_tree(10)
