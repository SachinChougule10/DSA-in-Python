# Leetcode : 328. Odd Even Linked List Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list (Brute Force Solution)
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def odd_even_linked_list(self, head: Optional[Node]) -> Optional[Node]:

        # Edge case: If list is empty or has only one node
        if not head or head.next is None:
            return head

        values = []  # This will store reordered values

        # Step 1: Collect ODD indexed values
        curr = head
        while curr is not None:
            values.append(curr.val)  # Store current node value
            # Jump two steps to reach next odd index
            if curr.next is not None:
                curr = curr.next.next
            else:
                break  # No more nodes

        # Step 2: Collect EVEN indexed values
        curr = head.next  # Start from second node (even index)
        while curr is not None:
            values.append(curr.val)
            # Jump two steps to reach next even index
            if curr.next is not None:
                curr = curr.next.next
            else:
                break

        # Step 3: Rewrite linked list
        curr = head
        index = 0
        while curr is not None:
            curr.val = values[index]  # Overwrite node value
            index += 1
            curr = curr.next

        return head


# Helper Function: Linked List Creation. Used only for local testing & debugging
def create_linked_list(arr):

    if not arr:
        return

    # Create all nodes first
    nodes = [Node(val) for val in arr]

    # Link nodes sequentially
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
visualize_linked_list(head)

print("After: ")
head = obj.odd_even_linked_list(head)
visualize_linked_list(head)


# Golden rule for linked list testing - Always follow this order: CREATE → PRINT → MODIFY → PRINT

"""
Logic:

Problem Understanding:
We need to rearrange a linked list such that:
- All nodes at odd indices come first
- Then all nodes at even indices
- Maintain relative order within both groups

Example:
Input  : 1 → 2 → 3 → 4 → 5
Output : 1 → 3 → 5 → 2 → 4

Brute Force Idea:
Instead of rearranging pointers (which is optimal approach),we:

1. Traverse only odd indexed nodes (1st, 3rd, 5th...)
   - Jump by two nodes each time
   - Store their values

2. Traverse even indexed nodes (2nd, 4th, 6th...)
   - Again jump by two nodes
   - Store their values

3. Overwrite the original linked list using stored values

Why it works:
Because we preserve order while collecting, and rewrite in correct sequence.

Time Complexity  : O(N)
Space Complexity : O(N)

Drawback:
Uses extra space.
Optimal solution would rearrange pointers in O(1) space.
"""
