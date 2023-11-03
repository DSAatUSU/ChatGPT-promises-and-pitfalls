# A class to store a special binary tree node with a random pointer
class Node:
    # Constructor
    def __init__(self, data, left=None, right=None, random=None):
        self.data = data
        self.left = left
        self.right = right
        self.random = random


# Function to print the preorder traversal on a given binary tree
def preorder(root):

    if root is None:
        return

    # print the current node's data
    print(root.data, end=" —> (")

    # print left child's data
    print((root.left.data if root.left else "X"), end=", ")

    # print the right child's data
    print((root.right.data if root.right else "X"), end=", ")

    # print the random child's data
    print(str(root.random.data if root.random else "X") + ")")

    # recur for the left and right subtree
    preorder(root.left)
    preorder(root.right)


# Recursive function to copy random pointers from the original binary tree
# into the cloned binary tree using the dictionary
def updateRandomPointers(root, d):

    # base case
    if d.get(root) is None:
        return

    # update the random pointer of the cloned node
    d.get(root).random = d.get(root.random)

    # recur for the left and right subtree
    updateRandomPointers(root.left, d)
    updateRandomPointers(root.right, d)


# Recursive function to clone the data, left, and right children for
# each node of a binary tree into a given dictionary
def cloneLeftRightPointers(root, d):

    # base case
    if not root:
        return None

    # clone all fields of the root node except the random pointer

    # create a new node with the same data as the root node
    d[root] = Node(root.data)

    # clone the left and right subtree
    d[root].left = cloneLeftRightPointers(root.left, d)
    d[root].right = cloneLeftRightPointers(root.right, d)

    # return cloned root node
    return d[root]


# The main function to clone a special binary tree with random pointers
def cloneSpecialBinaryTree(root):

    # base case
    if not root:
        return root

    # create a dictionary to store mappings from a node to its clone
    d = {}

    # clone data, left, and right children for each node of the original
    # binary tree, and put references into the dictionary
    cloneLeftRightPointers(root, d)

    # update random pointers from the original binary tree in the dictionary
    updateRandomPointers(root, d)

    # return the cloned root node
    return d[root]


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.random = root.right
    root.left.right.random = root
    root.right.left.random = root.left.left
    root.random = root.left

    print("Preorder traversal of the original tree:")
    preorder(root)

    clone = cloneSpecialBinaryTree(root)

    print("\nPreorder traversal of the cloned tree:")
    preorder(clone)
