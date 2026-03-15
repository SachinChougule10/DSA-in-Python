# Doubly Linked List - Basic Operations
# ======================================

# A Doubly Linked List (DLL) is a linear data structure where each node holds:
#   - val  : the data stored in the node
#   - next : pointer to the next node
#   - prev : pointer to the previous node

# Unlike a singly linked list, traversal is possible in both directions.

# Structure:
#     None <-- [1] <--> [2] <--> [3] <--> [4] --> None
#               ^                           ^
#              head                        tail

# Operations covered:
#     - insert_at_head  : O(1) — insert at the front
#     - append          : O(n) — insert at the end by traversing
#     - append_using_tail: O(1) — insert at the end using tail pointer
#     - insert_at       : O(n) — insert at a specific position
#     - delete          : O(n) — delete node at a specific position
#     - display_dll     : O(n) — print the entire list

# Edge cases handled:
#     - Empty list
#     - Single element list (head and tail are the same node)
#     - Insert/delete at head (position 0)
#     - Insert/delete at tail (last position)
#     - Out-of-bounds position


class Node:
    def __init__(self, val):
        self.val = val  # Data stored in the node
        self.next = None  # Pointer to next node (forward direction)
        self.prev = None  # Pointer to previous node (backward direction)


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node

    def insert_at_head(self, val):
        new_node = Node(val)

        if not self.head:
            # Empty list: new node is both head and tail
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # New node points forward to old head
            self.head.prev = new_node  # Old head points backward to new node
            self.head = new_node  # Update head to new node

    def append(self, val):
        """Insert at the end by traversing the entire list — O(n)."""
        new_node = Node(val)

        if not self.head:
            # Empty list: new node is both head and tail
            self.head = self.tail = new_node
        else:
            curr = self.head
            while curr.next is not None:  # Traverse to the last node
                curr = curr.next

            curr.next = new_node  # Last node points forward to new node
            new_node.prev = curr  # New node points backward to last node
            self.tail = new_node  # Update tail to new node

    def append_using_tail(self, val):
        """Insert at the end using the tail pointer — O(1)."""
        new_node = Node(val)

        if not self.head:
            # Empty list: new node is both head and tail
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Current tail points forward to new node
            new_node.prev = self.tail  # New node points backward to current tail
            self.tail = new_node  # Update tail to new node

    def insert_at(self, val, position):
        """Insert a node at the given position (0-indexed)."""

        if position == 0:
            # Delegate to head insertion
            self.insert_at_head(val)
            return

        new_node = Node(val)

        curr = self.head
        count = 0

        # Traverse to the node just BEFORE the target position
        while curr is not None and count < position - 1:
            curr = curr.next
            count += 1

        if curr is None:
            # Ran out of nodes before reaching position — out of bounds
            print("Position out of bound")
            return

        # Wire new_node between curr and curr.next
        new_node.next = curr.next  # New node points forward to curr's next
        new_node.prev = curr  # New node points backward to curr

        if curr.next is not None:
            curr.next.prev = new_node  # curr's next points backward to new node
        else:
            self.tail = new_node  # Inserting at end — update tail

        curr.next = new_node  # curr points forward to new node

    def delete(self, position):
        """
        Delete the node at the given position (0-indexed).

        Core pattern — works for all 3 cases with the same logic:
            Delete Head   → prev is None → update head
            Delete Tail   → next is None → update tail
            Delete Middle → both prev and next exist → stitch neighbors together
        """

        if self.head is None:
            return None  # Nothing to delete in empty list

        count = 0
        curr = self.head

        # Traverse until we reach the target position
        while curr is not None and count < position:
            curr = curr.next
            count += 1

        if curr is None:
            # If we reach None before position → position is out of bounds.
            print("Invalid position!")
            return self.head

        # Fix the BACKWARD link of curr's next neighbor
        if curr.prev is None:
            # Deleting head — move head forward
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None  # New head has no previous node
            else:
                self.tail = None  # List is now empty
        else:
            curr.prev.next = curr.next  # Skip over curr in forward direction

        # Fix the FORWARD link of curr's previous neighbor
        if curr.next is not None:
            curr.next.prev = curr.prev  # Skip over curr in backward direction
        else:
            self.tail = curr.prev  # Deleting tail — move tail backward

        return self.head

    def display_dll(self):
        """Print all node values from head to tail."""

        curr = self.head
        while curr is not None:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print("None")


# ─────────────────────────────────────────────
# Test all operations
# ─────────────────────────────────────────────

dll = DoublyLinkedList()

# Test append — build initial list
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.display_dll()  # 2 <-> 3 <-> 4 <-> 5 <-> None

# Test insert_at_head
dll.insert_at_head(1)
dll.display_dll()  # 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None

# Test append_using_tail
dll.append_using_tail(6)
dll.display_dll()  # 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> None

# Test insert_at (middle)
dll.insert_at(99, 3)
dll.display_dll()  # 1 <-> 2 <-> 3 <-> 99 <-> 4 <-> 5 <-> 6 <-> None

# Test insert_at (out of bounds)
dll.insert_at(100, 80)  # Position out of bound
dll.display_dll()  # List unchanged

# Test delete head (position 0)
dll.delete(0)
dll.display_dll()  # 2 <-> 3 <-> 99 <-> 4 <-> 5 <-> 6 <-> None

# Test delete middle
dll.delete(2)
dll.display_dll()  # 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> None

# Test delete tail
dll.delete(4)
dll.display_dll()  # 2 <-> 3 <-> 4 <-> 5 <-> None

# Test delete out of bounds
dll.delete(80)  # Invalid position!
dll.display_dll()  # List unchanged
