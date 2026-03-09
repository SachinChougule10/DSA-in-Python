# Leetcode : 160. Intersection of Two Linked Lists : Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect (Better Solution)
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

    # Defines how the node object will appear when printed
    def __repr__(self):
        return f"Node: ({self.val})"


class Solution:
    def getIntersectionPoint(self, headA: Optional[Node], headB: Optional[Node]):

        # Count number of nodes in list A
        count1 = 0
        curr = headA

        while curr is not None:
            count1 += 1
            curr = curr.next

        # Count number of nodes in list B
        count2 = 0
        curr = headB

        while curr is not None:
            count2 += 1
            curr = curr.next

        # Find difference in lengths and align both lists
        if count1 < count2:
            count = count2 - count1
            return self.collision_point(headA, headB, count)
        else:
            count = count1 - count2
            return self.collision_point(headB, headA, count)

    def collision_point(self, head1: Optional[Node], head2: Optional[Node], d: int):

        # Move pointer of longer list 'd' steps ahead
        while d > 0:
            head2 = head2.next
            d -= 1

        # Traverse both lists together until node references match
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next

        # Either intersection node or None
        return head1


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
print(intersection)  # Output: Node: (8)


"""
Logic:

Goal:
Find the node where two singly linked lists intersect. Intersection means both lists share the same node reference in memory.

Key Idea:
If the lists intersect, they will have a common tail portion.

Steps:

1. Traverse List A and count its length (count1).
2. Traverse List B and count its length (count2).
3. Compute the difference between the two lengths.

4. Move the pointer of the longer list forward by the difference in lengths. This aligns both lists so that the remaining number of nodes is equal.

5. Traverse both lists simultaneously:
      move head1 and head2 one step at a time.

6. The first node where head1 == head2 is the intersection node.

7. If both pointers reach None, then the lists do not intersect.

Example:

List A:
4 → 1 → 2 → 8 → 4 → 5
            ↑
List B:     |
5 → 1 → 7 → 9

Nodes starting from 8 are shared.

Length of A = 6
Length of B = 7

Difference = 1

Move pointer of longer list (B) by 1 step.

Now traverse both lists together:

A: 4 → 1 → 2 → 8 → ...
B: 1 → 7 → 9 → 8 → ...

Eventually both pointers reach the same node (8).

Time Complexity:
O(N + M)

N = length of list A
M = length of list B

Traversal of A → O(N)
Traversal of B → O(M)
Traversal after alignment → O(min(N, M))

Space Complexity:
O(1)

No additional data structures are used.

Interview Notes:
Important to compare node references, not node values.
Two nodes having the same value does NOT mean intersection.
Intersection occurs only when both pointers refer to the same memory location.
"""
