# GFG : Pair Sum in Doubly Linked List
# Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target (Brute Force Solution)

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
        curr1 = head  # Outer pointer starts at the head
        while curr1 is not None:
            curr2 = curr1.next  # Inner pointer starts just ahead of curr1
            while curr2 is not None:
                if curr1.val + curr2.val == target:  # Check if the pair sums to target
                    result.append([curr1.val, curr2.val])  # Store the valid pair
                curr2 = curr2.next  # Advance inner pointer forward
            curr1 = curr1.next  # Advance outer pointer forward

        return result


# Doubly Linked List Creation
head = Node(1)
n1 = Node(2)
n2 = Node(4)
n3 = Node(5)
n4 = Node(6)
n5 = Node(8)
n6 = Node(9)

# Wire next pointers (forward direction)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

# Wire prev pointers (backward direction)
n1.prev = head
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4
n6.prev = n5

obj = Solution()
print(obj.pairsWithGivenSum(7, head))  # Output : [[1, 6], [2, 5]]

"""
LOGIC:

Problem:
    Find all pairs in a sorted doubly linked list whose values sum to a given target.

Approach: Nested Pointer Traversal (Brute Force)
    - Use two nested loops over the linked list nodes.
    - The outer pointer (curr1) visits each node one by one from head to tail.
    - For each position of curr1, the inner pointer (curr2) scans every node
      that comes after curr1 in the list.
    - At each (curr1, curr2) combination, check if their values add up to target.
    - If they do, record the pair in the result list.
    - Since the list contains distinct elements and curr2 always starts ahead of
      curr1, no duplicate or self-pairs are generated.

Why Doubly Linked List?
    - The prev pointers are wired here for completeness and to match the DLL
      structure, but the brute force approach only traverses forward (next),
      so prev pointers are not actively used in this solution.
    - An optimised two-pointer approach (O(n)) would leverage both ends of the
      DLL — starting one pointer at head and another at tail — and would
      actually make use of the prev pointer to move the tail pointer backward.

Complexity:
    Time  : O(n²) — every pair of nodes is examined once.
    Space : O(k)  — where k is the number of valid pairs stored in the result.
    
"""
