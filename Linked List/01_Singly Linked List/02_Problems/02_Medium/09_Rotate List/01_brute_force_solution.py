# Leetcode : 61. Rotate List (Brute Force Solution)
# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Constraints:
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def rotate_right(self, head: Optional[Node], k: int) -> Optional[Node]:

        # Edge case: empty list or single node
        if not head or not head.next:
            return head

        # Perform rotation k times
        for _ in range(k):
            curr = head
            prev = None

            # Traverse to the last node
            while curr.next is not None:
                prev = curr
                curr = curr.next

            # Detach the last node from the list
            prev.next = None

            # Move the last node to the front
            curr.next = head

            # Update head to the new first node
            head = curr

        return head


# Visualize Linked List
def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Linked List Creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

obj = Solution()

visualize_ll(head)  # 1 -> 2 -> 3 -> 4 -> 5 -> None

new_head = obj.rotate_right(head, 2)
visualize_ll(new_head)  # Output : 4 -> 5 -> 1 -> 2 -> 3 -> None

# Rotate right by k = break the list at (length − k) and move the last k nodes to the front.

"""
Logic (Brute Force Approach)
----------------------------

Goal:
Rotate a linked list to the RIGHT by k places.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5,  k = 2

Rotation 1:
Take the last node (5) and move it to the front
5 -> 1 -> 2 -> 3 -> 4

Rotation 2:
Take the last node (4) and move it to the front
4 -> 5 -> 1 -> 2 -> 3


Algorithm
---------
1. If the list is empty or has only one node, return it as is.

2. Repeat the rotation process k times:
    a. Traverse the list to reach the last node.
    b. Keep track of the second last node (prev).
    c. Break the link between second last and last node.
    d. Attach the last node at the front of the list.
    e. Update head to this new node.

3. Return the new head of the rotated list.


Visualization
-------------
Original:
1 -> 2 -> 3 -> 4 -> 5

Step 1:
Detach last node (5)

1 -> 2 -> 3 -> 4      5

Step 2:
Move it to the front

5 -> 1 -> 2 -> 3 -> 4


Time Complexity
---------------
Each rotation requires traversing the entire list.

Traversal per rotation = O(n)
Number of rotations = k

Total Time Complexity = O(n * k)

Space Complexity
----------------
O(1)

No extra data structures are used. The rotation is performed in-place.
"""
