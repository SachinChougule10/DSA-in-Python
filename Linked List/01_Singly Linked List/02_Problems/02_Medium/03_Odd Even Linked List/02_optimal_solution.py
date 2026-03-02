# Leetcode : 328. Odd Even Linked List. Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list (Optimal Solution)
# The first node is considered odd, and the second node is even, and so on. Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def odd_even_linked_list(self, head: Optional[Node]) -> Optional[Node]:

        # Edge case: empty list or single node
        if not head or head.next is None:
            return head

        # Initialize pointers
        odd = head  # Points to current odd node
        even = head.next  # Points to current even node
        even_head = even  # Store head of even list to connect later

        # Traverse while there are available even nodes
        while even is not None and even.next is not None:
            # Link current odd node to next odd node
            odd.next = odd.next.next
            odd = odd.next

            # Link current even node to next even node
            even.next = even.next.next
            even = even.next

        # Attach even list after odd list
        odd.next = even_head

        return head


# Helper Function: Linked List Creation. Used only for local testing & debugging
def create_linked_list(arr):
    if not arr:
        return

    nodes = [Node(val) for val in arr]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]


# Helper Function: Visualization (NOT required for LeetCode). Used only for understanding & debugging
def visualize_linked_list(head):
    curr = head

    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


obj = Solution()

print("Before: ")
head = create_linked_list([1, 2, 3, 4, 5])
visualize_linked_list(head)  # Output : 1 -> 2 -> 3 -> 4 -> 5 -> None

print("After: ")
head = obj.odd_even_linked_list(head)
visualize_linked_list(head)  # Output : 1 -> 3 -> 5 -> 2 -> 4 -> None


"""
Logic:

Goal:
Rearrange the linked list so that:
- All nodes at odd positions come first
- Then all nodes at even positions
- Maintain original relative order
- Use O(1) extra space

Example:
Input  : 1 -> 2 -> 3 -> 4 -> 5
Index  : 1   2   3   4   5

Odd nodes  : 1 -> 3 -> 5
Even nodes : 2 -> 4

Output:
1 -> 3 -> 5 -> 2 -> 4

------------------------------------------------

Core Idea:

Instead of creating new lists, we rearrange pointers in-place.

We maintain:
- odd pointer
- even pointer
- even_head (to reconnect later)

Step-by-step:

1. odd starts at head
2. even starts at head.next
3. Store even_head for final attachment

Inside loop:
- Connect odd to next odd (skip even)
- Connect even to next even (skip odd)
- Move both pointers forward

Finally:
- Attach even list after odd list

Why this works:
We are effectively splitting the list into two chains during traversal and reconnecting them at the end.

Time Complexity:
O(n) → Each node visited once

Space Complexity:
O(1) → Only pointer variables used
"""
