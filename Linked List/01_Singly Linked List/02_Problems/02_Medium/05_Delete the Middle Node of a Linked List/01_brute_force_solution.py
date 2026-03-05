# Leetcode : 2095. Delete the Middle Node of a Linked List (Brute Force Solution)
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

        # -------- First Pass: Count total nodes --------
        curr = head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.next

        # -------- Second Pass: Move to node BEFORE middle --------
        curr = head

        # Middle index = count // 2
        # We stop at (middle - 1) to unlink middle node
        for _ in range(count // 2 - 1):
            curr = curr.next

        # Delete the middle node
        curr.next = curr.next.next

        return head


# Helper function to visualize Linked List, not required for Leetcode
def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Linkde List creation
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

Core Idea:
- First compute the total length of the linked list.
- Then calculate the middle index using floor(n/2).
- Traverse again to reach the node just before the middle.
- Adjust pointers to remove the middle node.

How it works step-by-step:
1. Count total nodes (n).
2. Compute middle index = n // 2.
3. Move to index (middle - 1).
4. Perform: curr.next = curr.next.next.

Characteristics:
- Requires TWO passes over the list.
- Explicitly calculates the middle using length.
- Easier to think about logically.
- Slightly less efficient in traversal count.

Time Complexity: O(n)
Space Complexity: O(1)
"""
