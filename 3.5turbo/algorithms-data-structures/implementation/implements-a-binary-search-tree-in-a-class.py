class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_helper(data, self.root)

    def _insert_helper(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_helper(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_helper(data, node.right)

    def search(self, data):
        return self._search_helper(data, self.root)

    def _search_helper(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_helper(data, node.left)
        else:
            return self._search_helper(data, node.right)

    def delete(self, data):
        self.root = self._delete_helper(data, self.root)

    def _delete_helper(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_helper(data, node.left)
        elif data > node.data:
            node.right = self._delete_helper(data, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete_helper(temp.data, node.right)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def traverse_inorder(self):
        self._traverse_inorder_helper(self.root)

    def _traverse_inorder_helper(self, node):
        if node:
            self._traverse_inorder_helper(node.left)
            print(node.data)
            self._traverse_inorder_helper(node.right)

# Example usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder traversal:")
bst.traverse_inorder()

print("Search for value 2:")
result = bst.search(2)
print(result.data if result else "Value not found")

print("Delete value 3:")
bst.delete(3)
bst.traverse_inorder()
