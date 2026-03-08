# GFG : Add Number Linked Lists (Optimal Solution)
# You are given the head of two singly linked lists head1 and head2 representing two non-negative integers.
# Each node contains a single digit and the digits are stored in forward order.
# Return the head of the linked list representing the sum of these two numbers.

# Note:
# - There can be leading zeros in the input lists.
# - The output list should not contain leading zeros.

# Example:
# Input: 1 -> 2 -> 3 , 9 -> 9 -> 9
# Output: 1 -> 1 -> 2 -> 2
# Explanation: 123 + 999 = 1122

# Input: 6 -> 3 , 7
# Output: 7 -> 0
# Explanation: 63 + 7 = 70

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # Standard linked list reversal
    def reverse_ll(self, head):
        curr = head
        temp = None
        prev = None

        while curr is not None:
            temp = curr.next  # store next node
            curr.next = prev  # reverse pointer
            prev = curr  # move prev forward
            curr = temp  # move curr forward

        return prev

    def add_two_lists(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:

        # Reverse both lists so we can add from least significant digit
        l1 = self.reverse_ll(head1)
        l2 = self.reverse_ll(head2)

        # dummy node to build result list
        dummy = Node(0)
        curr = dummy
        carry = 0

        # Traverse both lists until both are exhausted and carry becomes 0
        while l1 or l2 or carry:

            # Extract values safely
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry

            # Current digit
            val = total % 10
            # Carry for next iteration
            carry = total // 10

            # Create new node
            curr.next = Node(val)
            curr = curr.next

            # Move pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Result list is reversed because we added from LSB
        result = self.reverse_ll(dummy.next)

        # Remove leading zeros if present
        while result and result.val == 0:
            result = result.next

        return result


# visualize linked list
def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Creating first linked list
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(5)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(9)

# Creating second linked list
head2 = Node(3)
head2.next = Node(4)
head2.next.next = Node(5)
head2.next.next.next = Node(6)
head2.next.next.next.next = Node(3)

obj = Solution()

visualize_ll(head1)  # 1 -> 2 -> 5 -> 7 -> 9 -> None
visualize_ll(head2)  # 3 -> 4 -> 5 -> 6 -> 3 -> None

new_head = obj.add_two_lists(head1, head2)
visualize_ll(new_head)  # Output : 4 -> 7 -> 1 -> 4 -> 2 -> None

"""
Logic:

This problem adds two numbers represented by linked lists where each node contains a single digit and the digits are stored in forward order.

Example:
1 -> 2 -> 3 represents the number 123

Steps Used:

1. Reverse Both Linked Lists
   Since digits are stored in forward order, addition cannot start directly from the head. Reversing allows us to start addition from the least significant digit.

2. Perform Digit-by-Digit Addition
   Traverse both reversed lists simultaneously and compute:

        total = digit1 + digit2 + carry

   Extract:
        digit = total % 10
        carry = total // 10

   Create a new node for the digit and append it to the result list.

3. Continue Until Lists and Carry Are Exhausted
   The loop runs while either list still has nodes or a carry remains.

4. Reverse the Result List
   The result list is currently reversed because digits were added from least significant to most significant. Reverse again to restore forward order.

5. Remove Leading Zeros
   Input lists may contain leading zeros but the output must not. Therefore any leading zeros are skipped.

Time Complexity:
O(N + M)

Where:
N = length of first linked list
M = length of second linked list

Space Complexity:
O(max(N, M)) for the resulting linked list.


DIFFERENCE FROM LEETCODE "Add Two Numbers"

LeetCode Problem:
Add Two Numbers (digits stored in reverse order)

Example:
2 -> 4 -> 3 represents 342

In LeetCode:
- Digits are already reversed
- Addition starts directly from head
- No need to reverse lists

In This GFG Problem:
- Digits are stored in forward order
- Lists must be reversed before addition
- Result must be reversed again
- Leading zeros must be removed

Therefore the extra steps here are:
1. Reverse input lists
2. Reverse result list
3. Remove leading zeros
"""
