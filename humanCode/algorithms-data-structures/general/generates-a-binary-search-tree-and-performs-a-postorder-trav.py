# A O(n) program for construction of BST
# from postorder traversal
INT_MIN = -(2**31)
INT_MAX = 2**31

# A binary tree node has data, pointer to
# left child and a pointer to right child
# A utility function to create a node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# A recursive function to construct
# BST from post[]. postIndex is used
# to keep track of index in post[].
def constructTreeUtil(post, postIndex, key, min, max, size):

    # Base case
    if postIndex[0] < 0:
        return None

    root = None

    # If current element of post[] is
    # in range, then only it is part
    # of current subtree
    if key > min and key < max:

        # Allocate memory for root of this
        # subtree and decrement *postIndex
        root = newNode(key)
        postIndex[0] = postIndex[0] - 1

        if postIndex[0] >= 0:

            # All nodes which are in range key..
            # max will go in right subtree, and
            # first such node will be root of
            # right subtree.
            root.right = constructTreeUtil(
                post, postIndex, post[postIndex[0]], key, max, size
            )

            # Construct the subtree under root
            # All nodes which are in range min ..
            # key will go in left subtree, and
            # first such node will be root of
            # left subtree.
            root.left = constructTreeUtil(
                post, postIndex, post[postIndex[0]], min, key, size
            )

    return root


# The main function to construct BST
# from given postorder traversal. This
# function mainly uses constructTreeUtil()
def constructTree(post, size):

    postIndex = [size - 1]
    return constructTreeUtil(
        post, postIndex, post[postIndex[0]], INT_MIN, INT_MAX, size
    )


# A utility function to printInorder
# traversal of a Binary Tree
def printInorder(node):

    if node == None:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)


# Driver Code
if __name__ == "__main__":
    post = [1, 7, 5, 50, 40, 10]
    size = len(post)

    root = constructTree(post, size)

    print("Inorder traversal of the", "constructed tree: ")
    printInorder(root)
