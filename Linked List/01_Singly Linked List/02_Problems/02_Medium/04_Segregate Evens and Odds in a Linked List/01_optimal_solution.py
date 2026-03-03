# Geeks For Geeks : Segregate Evens and Odds in a Linked List
# Given a link list, modify the list such that all the even numbers appear before all the odd numbers in the modified list.
# NOTE: Don't create a new linked list, instead rearrange the provided one.

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def segregate_even_odd(self, head: Optional[Node]) -> Optional[Node]:
        # If list is empty or has only one node, return as it is
        if not head or not head.next:
            return head

        # Initialize separate heads and tails for even and odd lists
        even_head, even_tail = None, None
        odd_head, odd_tail = None, None

        curr = head

        # Traverse the original linked list
        while curr is not None:

            # Store next node before modifying links
            next_node = curr.next

            # If current node value is even
            if curr.val % 2 == 0:
                # First even node
                if even_head is None:
                    even_head = even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = curr

            # If current node value is odd
            else:
                # First odd node
                if odd_head is None:
                    odd_head = odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = curr

            # Move to next node
            curr = next_node

        # If there are no even nodes, return odd list
        if even_head is None:
            return odd_head

        # Connect even list to odd list
        even_tail.next = odd_head

        # Ensure last node points to None
        if odd_tail:
            odd_tail.next = None

        return even_head


# Helper Function: Visualization. Used only for understanding & debugging


def visualize_ll(head):
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
new_head = obj.segregate_even_odd(head)

visualize_ll(new_head)  # Output : 2 -> 4 -> 1 -> 3 -> 5 -> None


"""
Logic:

Problem:
Segregate even and odd nodes in a linked list such that all even-valued nodes appear before odd-valued nodes. Rearrangement must be done in-place.

Approach:
1. Traverse the original linked list once.
2. Maintain two separate lists:
   - One for even nodes
   - One for odd nodes
3. Use head and tail pointers for both lists.
4. For each node:
   - If value is even → append to even list
   - Else → append to odd list
5. After traversal:
   - If no even nodes exist → return odd_head
   - Else connect even_tail.next to odd_head
6. Return even_head as new head.

Why store next_node?
Because we modify node links while rearranging, so we must save the next pointer before changing connections.

Time Complexity:
O(N) → We traverse the list once.

Space Complexity:
O(1) → No extra data structures used.
Only pointer rearrangement.

Edge Cases:
- Empty list
- All even nodes
- All odd nodes
- Single node list
"""
