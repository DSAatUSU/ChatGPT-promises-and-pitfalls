class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
            
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
                
    def clone(self):
        if self.root is None:
            return None
        else:
            cloned_tree = BinarySearchTree()
            cloned_tree.root = self._clone_recursive(self.root)
            return cloned_tree
        
    def _clone_recursive(self, current_node):
        if current_node is None:
            return None
        cloned_node = Node(current_node.value)
        cloned_node.left = self._clone_recursive(current_node.left)
        cloned_node.right = self._clone_recursive(current_node.right)
        return cloned_node


# Example usage:
if __name__ == "__main__":
    # Create a binary search tree
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)

    # Clone the binary search tree
    cloned_bst = bst.clone()

    # Print the values in the original tree
    def print_tree(node):
        if node is None:
            return
        print_tree(node.left)
        print(node.value)
        print_tree(node.right)

    print("Original tree:")
    print_tree(bst.root)

    # Print the values in the cloned tree
    print("Cloned tree:")
    print_tree(cloned_bst.root)
