# Leetcode : 2095. Delete the Middle Node of a Linked List (Optimal Solution)
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.

# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.

# Example 3:
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.

# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 1 <= Node.val <= 105

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteMiddle(self, head: Optional[Node]) -> Optional[Node]:
        # If list is empty OR contains only one node, deleting the middle means returning None
        if not head or not head.next:
            return None

        slow = head  # moves 1 step
        fast = head  # moves 2 steps
        prev = None  # tracks node before slow

        # Move fast twice as fast as slow
        # When fast reaches end, slow will be at middle (floor(n/2))
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Remove the middle node
        prev.next = slow.next

        return head


# Helper function to visualize Linked List, not required for Leetcode
def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Linked List creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

obj = Solution()

visualize_ll(head)  # Output : 1 -> 2 -> 3 -> 4 -> 5 -> None

new_head = obj.deleteMiddle(head)
visualize_ll(new_head)  # Output : 1 -> 2 -> 4 -> 5 -> None


"""
Logic:

- Use two pointers moving at different speeds.
- Fast moves 2 steps, slow moves 1 step.
- When fast reaches the end, slow will be at floor(n/2).

How it works step-by-step:
1. Initialize slow = head, fast = head.
2. Move slow by 1 step and fast by 2 steps.
3. Maintain a 'prev' pointer to track node before slow.
4. When fast reaches end:
      slow is at middle.
5. Perform: prev.next = slow.next.

Why it works:
- Fast pointer completes traversal twice as quickly.
- So when fast reaches the end,
  slow has covered exactly half the distance.

Characteristics:
- Requires ONLY ONE pass.
- Does NOT explicitly calculate length.
- More elegant and interview-preferred.
- Uses pointer mechanics instead of arithmetic.

Time Complexity: O(n)
Space Complexity: O(1)
"""
