# Leetcode : 876. Middle of the Linked List (Optimal Solution)
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val  # Value stored in the node
        self.next = None  # Pointer to the next node


class Solution:
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        # Initialize two pointers at the head
        slow = head
        fast = head

        # Move slow by 1 step and fast by 2 steps
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow is at the middle
        return slow


# Linked List Structure:
# 1 -> 2 -> 3 -> 4 -> 5 -> None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

obj = Solution()
mid = obj.middleNode(head)
print(mid.val)  # Output: 3

"""
Logic Explanation (Optimal Approach - Slow & Fast Pointers / Tortoise & Hare):

1. This approach is also known as the Tortoise and Hare algorithm.
2. Two pointers are initialized at the head of the linked list:
   - Tortoise (slow pointer) moves one node at a time.
   - Hare (fast pointer) moves two nodes at a time.
3. As the hare moves twice as fast as the tortoise, when the hare reaches the end of the linked list (or becomes None),
   the tortoise will be at the middle node.
4. If the number of nodes is even, the tortoise naturally ends up at the second middle node, which satisfies the problem requirement.
5. The node pointed to by the tortoise (slow pointer) is returned.

Time and Space Complexity Analysis:
- The slow pointer moves one step at a time, while the fast pointer moves two steps.
- The loop runs approximately n/2 times.

- Time Complexity:
  O(n/2) = O(n).
  
- Space Complexity:
  O(1), since no extra memory is used.
"""
