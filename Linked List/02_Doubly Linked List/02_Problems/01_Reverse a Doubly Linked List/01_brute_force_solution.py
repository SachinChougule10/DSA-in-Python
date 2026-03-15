# GFG : Reverse a Doubly Linked List. You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head (Brute Force Solution)

from typing import Optional


class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None


class Solution:
    def reverse_dll(self, head: Optional[Node]) -> Optional[Node]:

        if head is None:
            return None

        curr = head
        stack = []

        # Pass 1 — push all node values onto the stack
        while curr is not None:
            stack.append(curr.val)  # stack grows: [1, 2, 3, 4, 5, 6]
            curr = curr.next

        curr = head
        # Pass 2 — pop from stack and overwrite node values in forward order
        while curr is not None:
            e = stack.pop()  # pop gives reversed order: 6, 5, 4, 3...
            curr.val = e  # overwrite current node's value
            curr = curr.next

        return head  # head pointer is unchanged, values are reversed


def visualize_dll(head):
    curr = head

    while curr is not None:
        print(curr.val, end=" <-> ")
        curr = curr.next

    print("None")


# Doubly Linked List Creation
head = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)

# Wire next pointers (forward direction)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Wire prev pointers (backward direction)
n1.prev = head
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4

# Result: None <-- 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 --> None

dll = Solution()

visualize_dll(head)  # 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> None

reversed_head = dll.reverse_dll(head)
visualize_dll(reversed_head)  # Output : # 6 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> None

"""
Logic:

Brute Force — Reverse a Doubly Linked List using a Stack
==========================================================
 
    Approach:
        Instead of rewiring prev/next pointers, we collect all node values into a stack (LIFO),
        then overwrite node values in forward order using the popped (reversed) values.
 
    Why a stack works here:
        A stack reverses order naturally — last in, first out.
        Pushing  1→2→3→4→5→6 and popping gives 6→5→4→3→2→1.
 
    Visual:
        Original : 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
        Stack    : [1, 2, 3, 4, 5, 6]  (bottom to top)
        Pop order: 6, 5, 4, 3, 2, 1
        Result   : 6 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1
 
    Note:
        This approach only swaps VALUES, not pointers.
        The prev/next structure of the list remains unchanged.
        For a true pointer-based reversal, swap next and prev on each node instead (optimal approach — O(n) time, O(1) space).
 
    Time Complexity  : O(n) — two passes through the list
    Space Complexity : O(n) — stack holds all n values
"""
