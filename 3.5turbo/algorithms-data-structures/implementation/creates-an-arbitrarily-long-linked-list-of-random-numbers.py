import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def generate_random_list(self, length):
        for _ in range(length):
            self.add_node(random.randint(1, 100))

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.generate_random_list(10)  # Replace 10 with the desired length of the linked list
    linked_list.display()
