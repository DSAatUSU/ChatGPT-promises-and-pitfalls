import random

# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a LinkedList class


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print("->", current_node.data, end=" ")
            current_node = current_node.next
        print("\n")


# create a new linked list
llist = LinkedList()

LIST_LEN = random.randint(1, 100)
print("Creating a linked list of length :", LIST_LEN, end=" ")
for i in range(LIST_LEN):
    llist.insertAtEnd(i)

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())

# print the linked list
print("Node Data:")
llist.printLL()
