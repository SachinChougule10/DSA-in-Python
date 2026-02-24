# Leetcode : 206. Reverse Linked List Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse_linked_list(self, head: Optional[Node]) -> Optional[Node]:
        curr = head  # Pointer to traverse the list
        prev = None  # Will become the new head after reversal

        while curr is not None:
            front = curr.next  # Store next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr  # Move prev forward
            curr = front  # Move curr forward

        # Returning `prev` returns the NEW HEAD of the reversed list (LeetCode requirement)
        # If only the head VALUE is needed, return `prev.val` instead

        return prev  # New head of the reversed linked list


def print_list(head):

    # Utility function to display the linked list structure. Used only for visualization/debugging, not part of the LeetCode solution.

    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

obj = Solution()
# Reversed list head (Node)
reversed_head = obj.reverse_linked_list(head)

# Print full linked list structure
print_list(reversed_head)  # output : 5 -> 4 -> 3 -> 2 -> 1 -> None

# If you only want the new head VALUE:
print("New head value:", reversed_head.val)  # output: New head value: 5

"""
Logic: Reverse Linked List by Reversing Pointers (Optimal Approach)

This approach reverses the linked list by changing the direction of the `next` pointers of each node.

We use three pointers:
- curr: points to the current node being processed
- prev: points to the previous node (initially None)
- front: temporarily stores the next node to avoid losing access

Steps:
1. Store the next node in `front`
2. Reverse the link by setting curr.next = prev
3. Move `prev` to curr
4. Move `curr` to front

The process continues until curr becomes None.
At the end, `prev` points to the last node of the original list, which becomes the new head of the reversed list.

Return Value:
- Return `prev`, which is the new head of the reversed linked list.

Time Complexity: O(n)
Space Complexity: O(1) (in-place)

In a linked list, reversing the list is equivalent to returning the new head, since it represents the entry point to the entire reversed structure.
"""
