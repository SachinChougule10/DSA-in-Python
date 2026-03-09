# Leetcode : 160. Intersection of Two Linked Lists : Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect (Brute Force Solution)
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

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # Defines how the node object is represented when printed
    def __repr__(self):
        return f"Node: ({self.val})"


class Solution:
    def getIntersectionPoint(self, headA: Optional[Node], headB: Optional[Node]):
        # Create a set to store all nodes of list A
        hash_set = set()

        # Traverse list A and store each node reference in the set
        curr1 = headA
        while curr1 is not None:
            hash_set.add(curr1)  # store node reference
            curr1 = curr1.next  # move to next node

        # Traverse list B and check if any node already exists in the set it means both lists share the same memory reference
        curr2 = headB
        while curr2 is not None:
            if curr2 in hash_set:
                return curr2  # intersection node found

            curr2 = curr2.next  # move to next node

        # If no node is common between both lists
        return None


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
Find the node where two singly linked lists intersect.
Intersection means both lists point to the same node reference in memory.

Key Idea:
Instead of comparing values, we compare node references.

Steps:

1. Traverse the first linked list (List A).
2. Store each node reference in a hash set.
3. Traverse the second linked list (List B).
4. For each node in List B:
      check if the node reference exists in the set.
5. If found, that node is the intersection point.
6. If traversal completes without match → no intersection.

Example:

List A:
4 → 1 → 2 → 8 → 4 → 5
            ↑
List B:     |
5 → 1 → 7 → 9

Nodes starting from 8 are shared.

Set after traversing A:
{4,1,2,8,4,5} (node references)

While traversing B:
5 → not in set
1 → not in set
7 → not in set
9 → not in set
8 → FOUND in set → intersection

Time Complexity:
O(N + M)

N = length of list A
M = length of list B

Traversal of A → O(N)
Traversal of B → O(M)

Space Complexity:
O(N)

We store all nodes of list A in the set.

Why this works:
Hash set lookup takes O(1) average time, so intersection detection is fast.

Interview Notes:
Important to mention that we store node references, not values.
Two nodes having same value does NOT mean intersection.
Intersection happens only when memory addresses are same.
"""
