# Leetcode : 203. Remove Linked List Elements (Optimal Solution)
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def remove_elements(self, head: Optional[Node], val: int) -> Optional[Node]:
        curr = head  # Pointer to traverse the list
        prev = None  # Pointer to track previous valid node
        while curr is not None:
            if curr.val == val:
                # Case 1: Node to be deleted is the head node
                if prev is None:
                    head = curr.next  # Move head forward
                else:
                    # Case 2: Node is in middle or end
                    prev.next = curr.next  # Skip current node
            else:
                # Move prev only when current node is NOT deleted
                prev = curr

            # Move current pointer forward
            curr = curr.next

        return head


# visualize linked list
def visualize(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# linked list creation
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

head2 = Node(11)
head2.next = Node(12)
head2.next.next = Node(13)
head2.next.next.next = Node(14)
head2.next.next.next.next = Node(15)

obj = Solution()

new_head = obj.remove_elements(head1, 1)
visualize(new_head)  # Output : 2 -> 3 -> 4 -> 5 -> None

new_head = obj.remove_elements(head2, 15)
visualize(new_head)  # Output : 11 -> 12 -> 13 -> 14 -> None


"""
Logic:

Approach:
---------
We traverse the linked list using two pointers:
1. curr -> points to the current node
2. prev -> points to the previous valid node

At each step:
-------------
1. If curr.val == val (node needs to be removed):
   a) If prev is None:
      - This means we are deleting the head node
      - Move head to next node → head = curr.next

   b) Else:
      - Skip the current node by linking:
        prev.next = curr.next

2. If curr.val != val:
   - Move prev forward → prev = curr

3. Move curr forward in every iteration → curr = curr.next

Key Insight:
------------
- We only move prev when we KEEP the node
- If we delete a node, prev stays in place to maintain proper linking

Edge Cases:
-----------
1. Empty list → return None
2. All nodes match val → return None
3. Head node(s) need removal → handled using prev == None
4. No nodes match val → list remains unchanged

Time Complexity:
----------------
O(n) → We traverse the list once

Space Complexity:
-----------------
O(1) → No extra space used

"""
