# GFG : Remove duplicates from a sorted doubly linked list (Brute Force Solution)
# Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.


# Example 1:
# Input:
# n = 6
# 1<->1<->1<->2<->3<->4
# Output:
# 1<->2<->3<->4
# Explanation:
# Only the first occurance of node with value 1 is retained, rest nodes with value = 1 are deleted.


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class Solution:
    def removeDuplicates(self, head):
        seen = set()  # Set to store unique values (automatically ignores duplicates)
        curr = head  # Start traversal from head

        # Step 1: Traverse the entire list and collect all unique values
        while curr is not None:
            # Add value to set; duplicates are silently ignored
            seen.add(curr.val)
            curr = curr.next

        # Step 2: Sort the unique values to restore original sorted order
        # (sets do not preserve insertion order, so sorting is required)
        values = sorted(seen)

        # Step 3: Build a brand new DLL from the sorted unique values
        head = Node(values[0])  # Create new head with the smallest value
        curr = head

        # Iterate over remaining unique values
        for val in values[1:]:
            new_node = Node(val)  # Create a new node
            new_node.prev = curr  # Link new node's prev to current node
            curr.next = new_node  # Link current node's next to new node
            curr = curr.next  # Advance curr to the newly added node

        # Return the head of the newly constructed DLL
        return head


head = Node(1)
n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)

# Building the next pointers (forward direction)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Building the prev pointers (backward direction)
n1.prev = head
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4


def visualize_dll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" <-> ")
        curr = curr.next
    print("None")


obj = Solution()
no_duplicates_head = obj.removeDuplicates(head)
visualize_dll(no_duplicates_head)  # Output: 1 <-> 2 <-> 3 <-> 4

"""
LOGIC — Remove Duplicates from a Sorted Doubly Linked List (Brute Force)
=========================================================================

INTUITION:
    Instead of rewiring pointers in-place, we take a simpler approach:
    extract all values into a set to eliminate duplicates automatically,
    sort them to restore order, then rebuild a fresh DLL from scratch.
    This trades space for simplicity.

ALGORITHM (3 Steps):
    1. COLLECT — Traverse the original DLL and insert every node value into a set. 
    Since sets only store unique elements, duplicates are dropped automatically.

    2. SORT — Convert the set to a sorted list. This step is necessary because sets are unordered in Python
    and do not guarantee insertion order is preserved.

    3. REBUILD — Construct a brand new doubly linked list from the sorted unique values, wiring both `next` and `prev` pointers as we go.

WHY SORT IS NEEDED:
    Even though the input list is sorted, a set discards ordering.
    For example: {1, 2, 3, 4} may not iterate in that order internally.
    sorted() guarantees we rebuild the DLL in ascending order.

COMPLEXITY:
    Time  : O(n log n) — dominated by sorted(); traversal is O(n)
    Space : O(n)       — set stores up to n unique values + new DLL nodes

EXAMPLE WALKTHROUGH:
    Input : 1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 4

    Step 1 — Collect into set:
             seen = {1, 2, 3, 4}

    Step 2 — Sort:
             values = [1, 2, 3, 4]

    Step 3 — Rebuild DLL:
             head(1) <-> Node(2) <-> Node(3) <-> Node(4)

    Output: 1 <-> 2 <-> 3 <-> 4
"""
