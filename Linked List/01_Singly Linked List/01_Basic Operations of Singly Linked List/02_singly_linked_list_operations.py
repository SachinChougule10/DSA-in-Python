# Description:
# This program implements a basic Singly Linked List (SLL) in Python.

# The code defines:
# - A Node class to represent each element in the linked list
# - A Singly_Linked_List class to manage the list operations

# The linked list supports the following operations:
# - Append: Add a new node at the end of the list
# - Traverse: Print all elements of the list
# - Insert at position: Insert a node at a specified index
# - Delete by value: Remove the first occurrence of a given value

# This implementation demonstrates how nodes are linked using references (`next`) and
# is intended for learning and understanding linked list fundamentals.


# Node class represents a single element of the linked list
class Node:
    def __init__(self, val):
        self.val = val  # Stores the data/value of the node
        self.next = None  # Reference to the next node (initially None)


# Class representing a Singly Linked List
class Singly_Linked_List:
    def __init__(self):
        self.head = None  # Head pointer of the linked list

    # Append a node at the end of the linked list
    def append(self, val):
        new_node = Node(val)
        # if SLL is empty
        if not self.head:
            self.head = new_node
        # if SLL is not empty
        else:
            curr = self.head
            # we will add the node at the end, i.e. when a node's next is None
            while curr.next is not None:
                curr = curr.next
            # Link the last node to the new node
            curr.next = new_node

    # Traverse and print all elements of the linked list
    def traverse(self):
        # If the list is empty
        if not self.head:
            print("SLL is empty!")
        else:
            curr = self.head
            # Traverse from head to end
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next

    # Insert a node at a given position (0-based index)
    def insert_at(self, val, position):
        new_node = Node(val)  # Create the new node

        # Edge case: inserting at non-zero position in empty list
        if self.head is None and position != 0:
            print("Invalid position")
            return

        # Insertion at head (valid for empty & non-empty list)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        prev = None
        count = 0  # Keeps track of current position

        # Traverse until desired position or end of list
        while curr is not None and count < position:
            prev = curr
            curr = curr.next
            count += 1

        # If position is greater than list length
        if count != position:
            print("Position out of range")
            return
        # Insert the new node between prev and curr
        prev.next = new_node
        new_node.next = curr

    # Delete the first occurrence of a given value
    def delete(self, val):
        # If the list is empty
        if not self.head:
            print("List is empty !")
            return
        curr = self.head

        # If the node to delete is the head node
        if curr.val == val:
            self.head = curr.next
            curr.next = None  # or del curr # Disconnect the node
            return

        prev = None

        # Traverse the list to find the node to delete
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                curr.next = None  # or del curr # Disconnect the node
                return
            prev = curr
            curr = curr.next
        # If the value is not found in the list
        print("Node not found !")


sll = Singly_Linked_List()

# Appending elements to the list
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)

# Traversing the list
sll.traverse()  # Output: 10 20 30 40
print()

# Inserting 50 at position 2
sll.insert_at(50, 2)
sll.traverse()  # Output: 10 20 50 30 40
print()

# Deleting the head node (10)
sll.delete(10)
sll.traverse()  # Output: 20 50 30 40
print()

# Deleting a middle node (30)
sll.delete(30)
sll.traverse()  # Output: 20 50 40
