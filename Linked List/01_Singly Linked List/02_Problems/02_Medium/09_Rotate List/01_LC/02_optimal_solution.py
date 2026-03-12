# Leetcode : 61. Rotate List (Optimal Solution)
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

        tail = head
        length = 1

        # Find the length of the list and the last node
        while tail.next is not None:
            tail = tail.next
            length += 1

        # Reduce k because rotating length times gives the same list
        k = k % length

        # If k becomes 0, no rotation is needed
        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail node
        # New tail will be at position (length - k - 1)
        new_tail = self.get_Nth_node(head, length - k - 1)

        # New head is the node after new tail
        head = new_tail.next

        # Break the circular link
        new_tail.next = None

        return head

    def get_Nth_node(self, head, distance):
        curr = head

        # Move "distance" steps from head
        for _ in range(distance):
            curr = curr.next

        return curr


# visualize linked list
def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# create linked list
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
Logic:

Goal
----
Rotate a linked list to the RIGHT by k places.

Example
-------
Input:
1 -> 2 -> 3 -> 4 -> 5, k = 2

Output:
4 -> 5 -> 1 -> 2 -> 3


Key Idea
--------
Instead of rotating the list k times (which costs O(n*k)), we compute the list length and rotate it in ONE operation.

Algorithm
---------

1. Find the length of the linked list. Also keep track of the last node (tail).

2. Reduce unnecessary rotations:
       k = k % length

3. If k == 0, return the list because it will remain the same.

4. Convert the list into a circular linked list:
       tail.next = head

5. Find the new tail node:
       new_tail position = length - k - 1

6. The new head will be:
       new_head = new_tail.next

7. Break the circular link:
       new_tail.next = None

8. Return the new head.


Visualization
-------------

Original:
1 -> 2 -> 3 -> 4 -> 5

Make circular:
1 -> 2 -> 3 -> 4 -> 5
^                   |
|___________________|

k = 2

New tail position:
length - k - 1 = 5 - 2 - 1 = 2

New tail = node 3
New head = node 4

Final list:
4 -> 5 -> 1 -> 2 -> 3


Time Complexity
---------------
O(n)

- Finding length: O(n)
- Finding new tail: O(n)
- Constant pointer operations

Space Complexity
----------------
O(1)

Only pointer manipulation is used.
"""
