import queue


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.hd = 0  # horizontal distance from the root


def add_node(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = add_node(node.left, key)
    elif key > node.key:
        node.right = add_node(node.right, key)

    return node


def top_view(root):
    if root is None:
        return

    # Queue for level order traversal
    q = queue.Queue()
    # To store horizontal distance from the root node
    hd = 0
    # Dictionary to store the top view
    top_view_dict = {}

    # Assign initial horizontal distance to the root node and enqueue it
    root.hd = hd
    q.put(root)

    while not q.empty():
        # Get the front node from the queue
        temp_node = q.get()

        # Update the horizontal distance for the node
        hd = temp_node.hd

        # If the horizontal distance is not in the dictionary, add it to the dictionary
        if hd not in top_view_dict:
            top_view_dict[hd] = temp_node.key

        # Enqueue the left and right child nodes if they exist
        if temp_node.left:
            temp_node.left.hd = hd - 1
            q.put(temp_node.left)

        if temp_node.right:
            temp_node.right.hd = hd + 1
            q.put(temp_node.right)

    # Print the top view nodes in the correct order
    for key in sorted(top_view_dict):
        print(top_view_dict[key], end=' ')


# Example usage
if __name__ == '__main__':
    # Create a binary search tree
    bst = None
    bst = add_node(bst, 50)
    bst = add_node(bst, 30)
    bst = add_node(bst, 70)
    bst = add_node(bst, 20)
    bst = add_node(bst, 40)
    bst = add_node(bst, 60)
    bst = add_node(bst, 80)
    bst = add_node(bst, 10)
    bst = add_node(bst, 25)
    bst = add_node(bst, 35)
    bst = add_node(bst, 45)
    bst = add_node(bst, 55)
    bst = add_node(bst, 65)
    bst = add_node(bst, 75)
    bst = add_node(bst, 85)

    # Print the top view of the binary search tree
    top_view(bst)
