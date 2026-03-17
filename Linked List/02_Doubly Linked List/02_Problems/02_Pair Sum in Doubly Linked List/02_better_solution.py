# GFG : Pair Sum in Doubly Linked List
# Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target (Better Solution)

# Example 1:

# Input:
# 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
# target = 7
# Output: (1, 6), (2,5)
# Explanation: We can see that there are two pairs (1, 6) and (2,5) with sum 7.

from typing import Optional  # Import Optional for type hinting (node can be None)


class Node:
    def __init__(self, val):
        self.val = val  # Store the integer value of this node
        self.prev = None  # Pointer to the previous node (None for head)
        self.next = None  # Pointer to the next node (None for tail)


class Solution:
    def pairsWithGivenSum(self, target: int, head: Optional[Node]) -> list[list[int]]:
        result = []  # Accumulates all valid [complement, curr.val] pairs
        my_set = set()  # Stores already-visited node values for O(1) lookup
        curr = head  # Traversal pointer, starts at the head of the list

        # Traverse until the tail's next (None)
        while curr is not None:
            # Calculate what value is needed to reach target
            complement = target - curr.val
            # Check if the required complement was seen before
            if complement in my_set:
                # Valid pair found — smaller value first (list is sorted)
                result.append([complement, curr.val])

            # Mark current value as visited before moving on
            my_set.add(curr.val)
            # Advance to the next node
            curr = curr.next

        # Return all pairs whose sum equals target
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
print(obj.pairsWithGivenSum(7, head))  # Ooutput: [[1, 6], [2, 5]]

"""
Logic:

Problem:
--------
    Given a sorted doubly linked list of positive distinct integers, find all pairs of nodes whose values sum to a given target.

    Input  : 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9,  target = 7
    Output : [[1, 6], [2, 5]]

Approach — Hash Set (Better Solution):
---------------------------------------
    Instead of using nested loops (brute force O(n²)), we leverage a hash set to track visited values and find complements in O(1).

    Core Idea:
        For every node with value V, we need (target - V) to exist somewhere earlier in the list. If it does, we have a valid pair.

    Step-by-step walkthrough for target = 7:
    -----------------------------------------
        Node 1 → complement = 6  | set = {}         → 6 not in set → add 1 | set = {1}
        Node 2 → complement = 5  | set = {1}        → 5 not in set → add 2 | set = {1,2}
        Node 4 → complement = 3  | set = {1,2}      → 3 not in set → add 4 | set = {1,2,4}
        Node 5 → complement = 2  | set = {1,2,4}    → 2 IN set     → pair [2,5] ✓
        Node 6 → complement = 1  | set = {1,2,4,5}  → 1 IN set     → pair [1,6] ✓
        Node 8 → complement = -1 | set = {1,2,4,5,6}→ -1 not in set
        Node 9 → complement = -2 | set = {..}       → -2 not in set

        Final result: [[2, 5], [1, 6]]

    Why the smaller value always comes first in the output:
        The list is sorted in ascending order. When a complement is found in the set, it was visited earlier (smaller index),
        meaning complement < curr.val always holds. So appending [complement, curr.val] naturally orders the pair smallest-first.

    Why prev pointers are unused in this approach:
        The hash set approach only needs a single left-to-right pass via .next pointers. The .prev pointers are part of the doubly
        linked list structure but are only needed for a two-pointer approach (optimal O(1) space solution).

Complexity:
-----------
    Time  : O(n) — single pass through all n nodes
    Space : O(n) — hash set stores at most n values
"""
