import random as rand


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def set_next(self, next):
        self.next = next

    # Recursive function to delete the linked list
    def delete_list(self):
        if self.head is None:
            return
        while self.head:
            print(self.head.data, end=" ")
            del self.head.data
            self.head = self.head.next


# Driver program to test above functions
llist = LinkedList()

rand_len = rand.randint(1, 100)
for i in range(rand_len):
    llist.push(rand.randint(1, 100))


print("\nGiven Linked List")
llist.printList()
print("\nDeleting Linked List")
llist.delete_list()

print("\nNew Linked List [1,2,3,4]")
for i in [1, 2, 3, 4]:
    llist.push(i)
llist.printList()
