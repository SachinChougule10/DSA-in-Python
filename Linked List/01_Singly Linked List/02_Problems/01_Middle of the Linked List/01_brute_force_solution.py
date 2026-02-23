# Leetcode : 876. Middle of the Linked List (Brute Force Approach)
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Optional[T] indicates that a variable can either be of type T or None, improving code clarity and safety.
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val  # Store node value
        self.next = None  # Pointer to next node


class Solution:
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        n = 0
        curr = head

        # First traversal: count total nodes
        while curr is not None:
            n += 1
            curr = curr.next

        # Second traversal: move to n//2-th node
        curr = head
        for _ in range(0, n // 2):
            curr = curr.next

        # curr now points to the middle node
        return curr


# Linked List Structure:
# 1 -> 2 -> 3 -> 4 -> 5 -> None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

obj = Solution()
mid = obj.middleNode(head)
print(mid.val)  # output : 3


"""
Logic Explanation (Brute Force Approach):

1. Traverse the linked list once to count the total number of nodes (n).
2. The middle node index is n // 2.
   - For odd length, this gives the exact middle.
   - For even length, this gives the second middle (as required).
3. Traverse the list again from the head and move n // 2 steps.
4. Return the node reached after these steps.


Time and Space Complexity Analysis:
- First traversal to count the number of nodes takes O(n).
- Second traversal to reach the middle node takes O(n).

- Total Time Complexity:
  O(n + n) = O(2n) = O(n).

- Space Complexity:
  O(1), as only pointer variables are used.
  
"""
