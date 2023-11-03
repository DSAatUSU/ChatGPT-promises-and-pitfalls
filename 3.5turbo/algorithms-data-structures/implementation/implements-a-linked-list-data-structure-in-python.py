class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Add a new node to the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """
        Add a new node to the beginning of the linked list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        Remove the first occurrence of a node with the given data from the linked list.
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        """
        Print all the nodes in the linked list.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()

    # Append nodes
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Prepend nodes
    linked_list.prepend(0)
    linked_list.prepend(-1)

    # Display nodes
    linked_list.display()  # Output: -1 0 1 2 3

    # Delete node
    linked_list.delete(0)

    # Display nodes after deletion
    linked_list.display()  # Output: -1 1 2 3
