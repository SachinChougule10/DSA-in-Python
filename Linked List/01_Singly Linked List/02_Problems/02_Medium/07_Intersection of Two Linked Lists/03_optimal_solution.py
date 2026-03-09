# Leetcode : 160. Intersection of Two Linked Lists : Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect (Optimal Solution)
# If the two linked lists have no intersection at all, return null.

# Example 1:

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references.
# In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

# Example 2:


# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

# Example 3:


# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # Defines how the node will appear when printed
    def __repr__(self):
        return f"Node: ({self.val})"


class Solution:
    def getIntersectionPoint(self, headA: Optional[Node], headB: Optional[Node]):

        # Initialize two pointers pointing to the heads of both lists
        l1 = headA
        l2 = headB

        # Traverse until both pointers point to the same node
        # (either the intersection node or None if no intersection)
        while l1 != l2:

            # Move pointer forward in list A
            # If it reaches end, redirect it to head of list B
            l1 = l1.next if l1 else headB

            # Move pointer forward in list B
            # If it reaches end, redirect it to head of list A
            l2 = l2.next if l2 else headA

        # When l1 == l2, it is either the intersection node or None
        return l1


# Creating the common intersection part
common = Node(8)
common.next = Node(4)
common.next.next = Node(5)

# Creating first linked list
headA = Node(4)
headA.next = Node(1)
headA.next.next = Node(2)
headA.next.next.next = common

# Creating second linked list
headB = Node(5)
headB.next = Node(1)
headB.next.next = Node(7)
headB.next.next.next = Node(9)
headB.next.next.next.next = common

obj = Solution()
intersection = obj.getIntersectionPoint(headA, headB)
print(intersection)  # Output : Node: (8)

"""
Logic:

Goal:
Find the node where two singly linked lists intersect. Intersection means both lists share the same node reference in memory.

Key Idea:
Use two pointers that traverse both lists. When a pointer reaches the end of its list, redirect it to the head of the other list.

This ensures both pointers traverse the same total distance.

Why this works:

Let:
A = length of list A
B = length of list B
C = length of common intersection part

Pointer l1 path:
A + B

Pointer l2 path:
B + A

Since both traverse the same total distance, they will meet at
the intersection node.

Steps:

1. Initialize two pointers:
      l1 → headA
      l2 → headB

2. Move both pointers forward one step at a time.

3. If a pointer reaches the end of its list:
      redirect it to the head of the other list.

4. Eventually both pointers will meet at:
      - the intersection node
      OR
      - None if there is no intersection.

Example:

List A:
4 → 1 → 2 → 8 → 4 → 5
            ↑
List B:     |
5 → 1 → 7 → 9

Traversal:

l1 path:
4 → 1 → 2 → 8 → 4 → 5 → None → 5 → 1 → 7 → 9 → 8

l2 path:
5 → 1 → 7 → 9 → 8 → 4 → 5 → None → 4 → 1 → 2 → 8

Both pointers meet at node 8.

Time Complexity:
O(N + M)

N = length of list A
M = length of list B

Each pointer traverses at most two lists.

Space Complexity:
O(1)

No additional data structures are used.

Interview Notes:
This is the optimal solution because it avoids computing list lengths and still ensures both pointers travel equal distances.

Important:
Intersection is determined by node reference equality, not by node value.
"""
