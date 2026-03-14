# GFG : Linked List Group Reverse (Optimal Solution)
# You are given the head of a Singly linked list. You have to reverse every k node in the linked list and return the head of the modified list.
# Note: If the number of nodes is not a multiple of k then the left-out nodes at the end, should be considered as a group and must be reversed.

# Examples:
# Input: k = 2,
# Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5
# Explanation: Linked List is reversed in a group of size k = 2.

# Input: k = 4,
# Output: 4 -> 3 -> 2 -> 1 -> 6 -> 5
# Explanation: Linked List is reversed in a group of size k = 4.

# Constraints:
# 1 ≤ size of linked list ≤ 105
# 0 ≤ node->data ≤ 106
# 1 ≤ k ≤ size of linked list

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):

        curr = head  # Pointer used to traverse the list
        prevLast = None  # Last node of the previously reversed group

        # Traverse the linked list group by group
        while curr:

            # Find the kth node from the current position
            kth = self.getKth(curr, k)

            # If kth node exists, we have a full group
            if kth:
                next_node = kth.next  # Save start of next group
                kth.next = None  # Detach current group
            else:
                # If fewer than k nodes remain (GFG requirement), we still reverse the remaining nodes
                next_node = None

            # Reverse the current group
            new_head = self.reverseLL(curr)

            # If this is the first group, update the head
            if prevLast is None:
                head = new_head
            else:
                # Connect previous reversed group with current reversed group
                prevLast.next = new_head

            # After reversal, 'curr' becomes the last node of this group
            prevLast = curr
            # Move to the next group
            curr = next_node

        return head

    def getKth(self, node, k):
        k -= 1  # We are already on the first node

        # Move forward k-1 steps to reach the kth node
        while node is not None and k > 0:
            node = node.next
            k -= 1

        # Returns kth node if it exists, otherwise None
        return node

    def reverseLL(self, head):
        curr = head
        prev = None

        # Standard linked list reversal
        while curr is not None:
            temp = curr.next  # Store next node
            curr.next = prev  # Reverse the pointer
            prev = curr  # Move prev forward
            curr = temp  # Move curr forward

        # 'prev' becomes the new head after reversa
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
head.next.next.next.next.next.next.next = Node(8)


obj = Solution()
new_head = obj.reverseKGroup(head, 3)
visualize_ll(new_head)  # Output : 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> None

"""
Logic:

We reverse the linked list in groups of size k.

Steps:
1. Start traversing the linked list using pointer `curr`.
2. For each group, try to locate the kth node using `getKth`.
3. If the kth node exists:
      - Detach the group by setting kth.next = None.
      - Reverse that group.
4. If the kth node does NOT exist:
      - It means fewer than k nodes remain.
      - For the GFG problem, we STILL reverse these remaining nodes.
5. After reversing a group:
      - Connect the previous reversed group's last node (prevLast)
        to the new head of the current reversed group.
6. Update prevLast to the last node of the current group
   (which was the first node before reversal).
7. Move curr to the next group and repeat the process.


Helper Functions

getKth(node, k)
    Moves k nodes ahead and returns the kth node if it exists.

reverseLL(head)
    Reverses a linked list using the classic three-pointer approach.


Time Complexity
O(n)
Each node is processed a constant number of times.

Space Complexity
O(1)
Reversal is done in-place without extra memory.


Difference Between GFG and LeetCode Versions

LeetCode Problem: Reverse Nodes in k-Group

If the last group contains fewer than k nodes:
    DO NOT reverse them.

Example:
Input
1 -> 2 -> 3 -> 4 -> 5
k = 3

Output
3 -> 2 -> 1 -> 4 -> 5


GFG Problem: Reverse a Linked List in Groups of Given Size

If the last group contains fewer than k nodes:
    STILL reverse them.

Example:
Input
1 -> 2 -> 3 -> 4 -> 5
k = 3

Output
3 -> 2 -> 1 -> 5 -> 4


Example Output for This Code

Input
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
k = 3

Output
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> None
"""
