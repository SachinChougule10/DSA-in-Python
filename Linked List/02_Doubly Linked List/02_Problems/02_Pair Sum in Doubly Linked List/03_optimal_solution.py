# GFG : Pair Sum in Doubly Linked List
# Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target (Optimal Solution)

# Example 1:

# Input:
# 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
# target = 7
# Output: (1, 6), (2,5)
# Explanation: We can see that there are two pairs (1, 6) and (2,5) with sum 7.

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class Solution:
    def pairsWithGivenSum(self, target: int, head: Optional[Node]) -> list[list[int]]:
        result = []
        left = head  # Left pointer starts at the head (smallest element)
        right = head  # Right pointer will be moved to the tail (largest element)

        # Traverse to the last node to position the right pointer at the tail
        while right.next is not None:
            right = right.next

        # Two-pointer approach: move inward until pointers meet or cross
        while left != right and left.prev != right:
            # Compute the sum of current pair
            total = left.val + right.val
            # Valid pair found, record it
            if total == target:
                result.append([left.val, right.val])
                left = left.next  # Move left pointer forward
                right = right.prev  # Move right pointer backward
            elif total < target:
                # Sum too small, increase it by moving left forward
                left = left.next
            else:
                # Sum too large, decrease it by moving right backward
                right = right.prev

        return result


head = Node(1)
n2 = Node(2)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n8 = Node(8)
n9 = Node(9)

# Link nodes in the forward direction (next pointers)
head.next = n2
n2.next = n4
n4.next = n5
n5.next = n6
n6.next = n8
n8.next = n9

# Link nodes in the backward direction (prev pointers)
n2.prev = head
n4.prev = n2
n5.prev = n4
n6.prev = n5
n8.prev = n6
n9.prev = n8

obj = Solution()
print(obj.pairsWithGivenSum(7, head))  # Output : [[1, 6], [2, 5]]

"""
Logic:

Problem:
--------
Given a sorted doubly linked list of distinct positive integers, find all pairs whose values sum to a given target.

Approach: Two-Pointer (Optimal)
--------------------------------
Because the list is sorted, we exploit the ordering using two pointers:
  - `left`  → starts at the head (smallest value)
  - `right` → starts at the tail (largest value)

At each step we compute total = left.val + right.val and apply three cases:

  1. total == target  → Valid pair found.
                        Move both pointers inward (left forward, right backward).

  2. total < target   → Sum is too small.
                        Advance `left` forward to get a larger value.

  3. total > target   → Sum is too large.
                        Move `right` backward to get a smaller value.

Termination Condition:
-----------------------
The loop stops when:
  - left == right         → both pointers landed on the same node (odd crossing)
  - left.prev == right    → left has moved one step past right (even crossing)

This correctly handles the case where pointers meet between two adjacent nodes.

Complexity:
-----------
  Time  : O(n) — each pointer traverses at most n nodes in total.
  Space : O(1) — no extra data structures used (result list excluded).

Example Walkthrough (target = 7):
-----------------------------------
List : 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9

Step 1 : left=1, right=9  → 1+9=10 > 7  → move right to 8
Step 2 : left=1, right=8  → 1+8=9  > 7  → move right to 6
Step 3 : left=1, right=6  → 1+6=7  == 7 → record (1,6), move both
Step 4 : left=2, right=5  → 2+5=7  == 7 → record (2,5), move both
Step 5 : left=4, right=4  → left == right → stop

Output: [[1, 6], [2, 5]]
"""
