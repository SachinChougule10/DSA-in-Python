# 234. Palindrome Linked List (Optimal Solution)
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val  # value stored in the node
        self.next = None  # pointer to the next node


class Solution:
    def is_palindrome(self, head: Optional[Node]) -> bool:

        # Edge case: empty list or single node is always palindrome
        if head is None or head.next is None:
            return True

        fast = head
        slow = head

        # Find the middle of the linked list using fast and slow pointers
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next  # move slow pointer by 1
            fast = fast.next.next  # move fast pointer by 2

        # Reverse the second half of the linked list
        new_head = self.reverse_ll(slow.next)

        curr1 = head  # pointer for first half
        curr2 = new_head  # pointer for reversed second half

        # Compare the first half and the reversed second half
        while curr2 is not None:
            if curr2.val != curr1.val:
                slow.next = self.reverse_ll(new_head)  # restore original list
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        # Restore the original linked list structure
        slow.next = self.reverse_ll(new_head)
        return True

    def reverse_ll(self, head):
        curr = head
        prev = None

        # Standard iterative linked list reversal
        while curr is not None:
            temp = curr.next  # store next node
            curr.next = prev  # reverse the link
            prev = curr  # move prev forward
            curr = temp  # move curr forward

        return prev  # new head of reversed list


obj = Solution()

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print(obj.is_palindrome(head))  # Output : True

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)

print(obj.is_palindrome(head1))  # Output : False

"""
Logic:

Goal: Check whether a singly linked list is a palindrome using O(1) extra space.

Steps:

1. Find the middle of the linked list using the fast and slow pointer technique.
   - slow moves 1 step at a time
   - fast moves 2 steps at a time
   When fast reaches the end, slow will be at the middle.

Example:
1 → 2 → 2 → 1
        ↑
       slow

2. Reverse the second half of the linked list starting from slow.next.

Original second half:
2 → 1

After reversal:
1 → 2

3. Compare the first half and the reversed second half node by node.

First half:     1 → 2
Second half:    1 → 2

If any value differs → not a palindrome.

4. Restore the original linked list by reversing the second half again.

Time Complexity:
O(N)
- Finding middle → O(N)
- Reversing second half → O(N/2)
- Comparing halves → O(N/2)

Space Complexity:
O(1)
- No extra data structures are used.
"""
