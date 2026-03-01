# Leetcode : 19. Remove Nth Node From End of List : Given the head of a linked list, remove the nth node from the end of the list and return its head (Brute Force Solution)

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def remove_Nth_from_end(self, head: Optional[Node], n: int) -> Optional[Node]:

        if not head:
            return None

        # Step 1: Calculate the length of the linked list
        length = 0
        curr = head

        while curr is not None:
            curr = curr.next
            length += 1

        # Step 2: If the node to remove is the head itself (i.e., n == length), simply move head to next node
        if n == length:
            head = head.next
            return head

        # Step 3: Find the position just before the node to delete - position_to_stop = (length - n)
        position_to_stop = length - n
        curr = head
        count = 1
        # for _ in range(length - n - 1):
        #     curr = curr.next
        # curr.next = curr.next.next

        # Step 4: Traverse until the node just before the target node
        while count < position_to_stop:
            curr = curr.next
            count += 1
        # Step 5: Skip the target node
        curr.next = curr.next.next

        return head


# ===================== Driver Code (For Local Testing) =====================


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
head1 = obj.remove_Nth_from_end(head, 2)
visualize_ll(head1)  # Output: 1 -> 2 -> 3 -> 5 -> None  , (2nd node from end removed)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head2 = obj.remove_Nth_from_end(head, 5)
visualize_ll(head2)
# Output: 2 -> 3 -> 4 -> 5 -> None (as n == length, 5th node from end = head removed)


"""
Logic Explanation (Brute Force Approach):

1. First, traverse the linked list to calculate its total length.
2. If n is equal to the length of the list, the node to be removed is the head node. Update head to head.next and return.
3. Otherwise, compute the position of the node just before the node to be removed using:
       position_to_stop = length - n
4. Traverse the list again until reaching this position.
5. Remove the target node by adjusting pointers:
       curr.next = curr.next.next
6. Return the updated head of the linked list.

Time Complexity:
O(n) + O(n) = O(2n) = O(n)
- One traversal to calculate the length
- One traversal to remove the nth node from the end

Space Complexity: O(1)
"""
