# Leetcode : 206. Reverse Linked List Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse_linked_list(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        stack = []  # Stack to store node values

        # Step 1: Push all node values into the stack
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next

        # Step 2: Pop values from stack and overwrite node values
        curr = head
        while curr is not None:
            e = stack.pop()
            curr.val = e
            curr = curr.next

        # Returning `head` because the node links are not reversed. Only the node values are reassigned in reverse order
        # If only the head VALUE is needed, return `head.val`

        # the head remains the same because links are not changed; only node values are reassigned in reverse order.
        return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


obj = Solution()
reversed_head = obj.reverse_linked_list(head)
print_list(reversed_head)  # output : 5 -> 4 -> 3 -> 2 -> 1 -> None
print("New head value: ", reversed_head.val)  # New head value:  5

"""
Logic: Reverse Linked List Using Stack (Value Reversal)

This approach reverses the linked list by reversing the VALUES of the nodes, not by modifying the node links.

Steps:
1. Traverse the linked list and push each node's value onto a stack.
2. Traverse the linked list again and pop values from the stack.
3. Assign the popped values back to the nodes in order.

Because a stack follows LIFO (Last In, First Out), values are reassigned in reverse order.

Important Notes:
- The structure of the linked list (next pointers) remains unchanged.
- The head node remains the same.
- Only the values inside the nodes are modified.

Return Value:
- Return `head` since the node links are not reversed.

Time Complexity: O(n)
Space Complexity: O(n) (extra stack)

In a linked list, reversing the list is equivalent to returning the new head, since it represents the entry point to the entire reversed structure.
"""
