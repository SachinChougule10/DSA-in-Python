# This file demonstrates the basic implementation of a singly linked list node in Python.
# It shows how to:
# - Create nodes using a Node class
# - Link nodes together using the `next` reference
# - Access node values and references
# - Understand how linked list nodes are connected in memory
# This file is intended for learning and understanding linked list fundamentals.


# Node class represents a single node in a singly linked list
class Node:
    def __init__(self, value):
        self.value = value  # Stores the data/value of the node
        self.next = None  # Reference to the next node (initially None)


# Creating individual nodes with values
node1 = Node(5)
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)

# Linking nodes together to form the linked list
# node1 -> node2 -> node3 -> node4 -> None
node1.next = node2
node2.next = node3
node3.next = node4

# Printing the node object itself
# This prints the memory address because __str__ or __repr__ is not defined
print(node1)  # Output: <__main__.Node object at 0x...>

# Printing the value stored in node1
print(node1.value)  # Output: 5

# Printing the next of node1
# Since node1.next = node2, this prints the address of node2
print(node1.next)  # Output: <__main__.Node object at 0x...>   (same as node2)

# Printing node2 directly
# This address will be the same as node1.next
print(node2)  # Output: <__main__.Node object at 0x...>

# Accessing the value of the next node (node2) using node1
print(node1.next.value)  # Output: 10

# Accessing node4's value by traversing through next references
# node1.next -> node2
# node2.next -> node3
# node3.next -> node4
print(node1.next.next.next.value)  # equivalent to - node4.value    # Output: 8

# Note:
# Accessing nodes like this is not efficient for large linked lists.
# Instead, traversal using a loop is preferred.
