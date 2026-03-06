# Leetcode : 2. Add Two Numbers : You are given two non-empty linked lists representing two non-negative integers (Optimal Solution)
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def add_two_numbers(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)  # dummy node to simplify result list construction
        curr = dummy  # pointer used to build the new linked list
        carry = 0  # stores carry generated during addition

        # continue while nodes remain in either list OR carry exists
        while l1 or l2 or carry:

            # get values from nodes, if node doesn't exist use 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # compute total including carry
            total = v1 + v2 + carry

            # digit to store in result list
            val = total % 10

            # update carry
            carry = total // 10

            # create new node with computed digit
            curr.next = Node(val)

            # move pointer forward
            curr = curr.next

            # move l1 pointer if it exists
            l1 = l1.next if l1 else None
            # move l2 pointer if it exists
            l2 = l2.next if l2 else None

        # return the head of the new linked list
        return dummy.next


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

visualize_ll(head1)  #  1 -> 2 -> 5 -> 7 -> 9 -> None

visualize_ll(head2)  # 3 -> 4 -> 5 -> 6 -> 3 -> None

new_head = obj.add_two_numbers(head1, head2)
visualize_ll(new_head)  # Output : 4 -> 6 -> 0 -> 4 -> 3 -> 1 -> None

"""
Logic:

Problem:
Two linked lists represent non-negative integers where each node contains a single digit.
Digits are stored in reverse order.

Example:
l1 = [2,4,3] → represents 342
l2 = [5,6,4] → represents 465

Result:
342 + 465 = 807
Output list = [7,0,8]

------------------------------------------------

Optimal Approach (Digit by Digit Addition)

Instead of converting linked lists into arrays or numbers, we directly process digits from both linked lists.

Step 1: Create a dummy node
This simplifies building the result linked list.

dummy -> start of result list

Step 2: Maintain three things:
1. pointer for list1
2. pointer for list2
3. carry

Step 3: Traverse both lists simultaneously

Loop condition:
while l1 OR l2 OR carry exists

This ensures we process:
• remaining nodes in longer list
• final carry

Step 4: Extract digit values

v1 = l1.val if l1 exists else 0
v2 = l2.val if l2 exists else 0

This handles lists of different lengths.

Step 5: Perform addition

total = v1 + v2 + carry

Example:
4 + 6 + 0 = 10

Step 6: Extract digit and carry

digit_to_store = total % 10
new_carry = total // 10

Example:
10 % 10 = 0
10 // 10 = 1

Step 7: Create a new node with the digit
Attach it to the result list.

curr.next = Node(digit)

Step 8: Move pointers forward

l1 = l1.next
l2 = l2.next
curr = curr.next

Step 9: Continue until both lists AND carry are exhausted.

Time Complexity:
O(max(n, m))

n = length of first linked list
m = length of second linked list

We traverse each list only once.

------------------------------------------------

Space Complexity:
O(max(n, m))

A new linked list is created to store the result.

Extra auxiliary space used = O(1)
(only carry and pointers)

------------------------------------------------

Why This Is Optimal

• No conversion to arrays
• No number conversion
• Single traversal
• Constant extra space
"""
