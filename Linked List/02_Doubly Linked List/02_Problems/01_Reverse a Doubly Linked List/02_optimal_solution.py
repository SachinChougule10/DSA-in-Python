# GFG : Reverse a Doubly Linked List. You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head (Optimal Solution)


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None  # Points to the previous node (None for head)
        self.next = None  # Points to the next node (None for tail)


class Solution:
    def reverse_dll(self, head):
        if head is None:  # Points to the next node (None for tail)
            return None
        if head.next is None:  # Edge case: single node, already "reversed"
            return head

        prev = None  # Will trail behind curr; becomes new next after swap
        curr = head  # Starts at head, walks forward each iteration

        while curr is not None:
            front = curr.next  # Save next node before we overwrite curr.next

            curr.next = prev  # Reverse the next pointer: now points backward
            curr.prev = front  # Reverse the prev pointer: now points forward

            prev = curr  # Advance prev to current node
            curr = front  # Advance curr to the saved next node

        return prev  # prev is now sitting on the new head (old tail)


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
visualize_dll(reversed_head)  # Output : 6 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> None

"""
LOGIC:

INTUITION:
    In a singly linked list reversal you only swap the `next` pointer.
    In a DLL every node carries both `next` AND `prev`, so both pointers
    must be swapped in a single pass — no extra space needed.

ALGORITHM  (in-place, O(n) time / O(1) space):
    ┌─────────────────────────────────────────────────────────────────┐
    │  For every node, swap its next ↔ prev pointers:                 │
    │      old:  prev  <──  curr  ──>  next                           │
    │      new:  prev  <──  curr  ──>  next   (roles reversed)        │
    └─────────────────────────────────────────────────────────────────┘

    We keep two running pointers:
        • curr  — the node currently being processed
        • prev  — the node just processed (starts as None)

    Each iteration:
        1. Save curr.next in `front` so we don't lose the rest of the list.
        2. curr.next = prev   → point backward (reversal of forward link)
        3. curr.prev = front  → point forward  (reversal of backward link)
        4. Slide prev and curr one step ahead.

    When curr becomes None we've processed every node and `prev` is
    sitting on the old tail — which is the new head.

STEP-BY-STEP TRACE  (1 <-> 2 <-> 3):
    ─────────────────────────────────────────────────────────────────
    Start : prev=None, curr=1
    ─────────────────────────────────────────────────────────────────
    iter 1│ front=2 | 1.next=None, 1.prev=2 | prev=1, curr=2
    iter 2│ front=3 | 2.next=1,    2.prev=3 | prev=2, curr=3
    iter 3│ front=None | 3.next=2, 3.prev=None | prev=3, curr=None
    ─────────────────────────────────────────────────────────────────
    Return prev=3  →  new head

    Resulting list: None <-- 3 <-> 2 <-> 1 --> None 

COMPLEXITY:
    Time  — O(n)  : single pass through all n nodes
    Space — O(1)  : only two extra pointers (prev, front); no auxiliary DS

EDGE CASES HANDLED:
    • Empty list  (head is None)  → return None
    • Single node (head.next is None) → return head unchanged
"""
