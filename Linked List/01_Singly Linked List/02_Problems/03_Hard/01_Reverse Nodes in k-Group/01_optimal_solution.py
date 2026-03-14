# Leetcode : 25. Reverse Nodes in k-Group Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list (Optimal Solution)
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseKGroup(self, head: Optional[Node], k: int) -> Optional[Node]:
        curr = head  # Pointer to traverse the linked list
        prevLast = None  # Last node of the previous reversed group

        # Traverse the list group by group
        while curr is not None:
            # Find the kth node from the current node
            kth = self.getKth(curr, k)

            # If fewer than k nodes remain, leave them unchanged
            if not kth:
                if prevLast:
                    prevLast.next = curr
                break

            # Save the starting node of the next group
            next_node = kth.next
            # Temporarily detach the current group
            kth.next = None

            # Reverse the current k-group
            new_head = self.reverse_ll(curr)

            # If reversing the first group, update head
            if curr == head:
                head = new_head
            else:
                # Connect previous reversed group with current reversed group
                prevLast.next = new_head

            # After reversal, curr becomes the last node of the group
            prevLast = curr

            # Move to the next group
            curr = next_node

        return head

    def getKth(self, node, k):
        # Move k-1 steps ahead to find the kth node
        k -= 1

        while node is not None and k > 0:
            node = node.next
            k -= 1

        # Returns kth node if exists, otherwise None
        return node

    def reverse_ll(self, head):
        curr = head  # Current node pointer
        prev = None  # Previous node pointer

        # Standard linked list reversal
        while curr is not None:
            temp = curr.next  # Store next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev forward
            curr = temp  # Move curr forward

        # prev becomes new head after reversal
        return prev


# Helper function to print linked list
def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Creating the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

obj = Solution()
new_head = obj.reverseKGroup(head, 3)
visualize_ll(new_head)  # Output : 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7 -> None

"""
Logic :

We reverse nodes of the linked list in groups of size k.

Steps:
1. Start traversing the linked list using a pointer `curr`.
2. For each group, find the kth node using the helper function `getKth`.
3. If the kth node does not exist, it means fewer than k nodes remain, so we leave the remaining nodes unchanged.
4. Detach the current group by setting kth.next = None.
5. Reverse the detached group using the helper function `reverse_ll`.
6. Connect the reversed group to the previous reversed group:
      - If it is the first group, update the head.
      - Otherwise, link prevLast.next to the new head of the reversed group.
7. After reversing, the original first node of the group becomes the last node, so update prevLast to that node.
8. Move curr to the next group and repeat the process.

Helper Functions:

getKth(node, k)
    Traverses k nodes ahead and returns the kth node.

reverse_ll(head)
    Reverses a linked list using three pointers:
    prev, curr, and next.

Time Complexity: O(n)
Each node is processed a constant number of times.

Space Complexity: O(1)
Reversal is done in-place without extra memory.
"""
