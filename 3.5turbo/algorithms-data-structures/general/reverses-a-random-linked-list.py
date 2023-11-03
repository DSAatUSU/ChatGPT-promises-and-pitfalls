class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def print_linked_list(head):
    current = head

    while current:
        print(current.data, end=" ")
        current = current.next

    print()

# Create a random linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

print("Reversed Linked List:")
print_linked_list(head)
