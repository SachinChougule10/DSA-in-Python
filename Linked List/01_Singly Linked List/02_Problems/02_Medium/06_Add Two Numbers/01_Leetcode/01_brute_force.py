# Leetcode : 2. Add Two Numbers : You are given two non-empty linked lists representing two non-negative integers (Brute Force Solution)
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
    def add_two_numbers(self, l1, l2):
        arr1 = []
        arr2 = []

        # Traverse first linked list and store values in arr1
        while l1 is not None:
            arr1.append(l1.val)
            l1 = l1.next

        # Traverse second linked list and store values in arr2
        while l2 is not None:
            arr2.append(l2.val)
            l2 = l2.next

        carry = 0  # carry generated during addition
        result = []  # list to store resulting digits

        # maximum length of both arrays
        n = max(len(arr1), len(arr2))

        # iterate through digits
        for i in range(n):
            # if one list is shorter, treat missing values as 0
            x = arr1[i] if i < len(arr1) else 0
            y = arr2[i] if i < len(arr2) else 0

            # sum of digits including carry
            s = x + y + carry

            # store the last digit of sum
            result.append(s % 10)

            # update carry
            carry = s // 10

        # if carry remains after loop, append it
        if carry:
            result.append(carry)

        # create dummy node to build result linked list
        dummy = Node(0)
        curr = dummy

        # convert result array to linked list
        for num in result:
            curr.next = Node(num)
            curr = curr.next

        # return head of the resulting linked list
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
Two linked lists represent numbers where each node stores a single digit and the digits are stored in reverse order.

Example:
l1 = [2,4,3] -> represents number 342
l2 = [5,6,4] -> represents number 465

Expected result:
342 + 465 = 807
Output list = [7,0,8]

-------------------------------------------------

Brute Force (Array Based Approach)

Step 1: Convert both linked lists into arrays
Example:
l1 -> arr1 = [2,4,3]
l2 -> arr2 = [5,6,4]

Step 2: Traverse both arrays and perform digit-wise addition while maintaining a carry value.

Formula:
sum = digit1 + digit2 + carry

digit_to_store = sum % 10
new_carry = sum // 10

Example:
2 + 5 = 7      -> result = [7]
4 + 6 = 10     -> store 0, carry = 1
3 + 4 + 1 = 8  -> result = [7,0,8]

Step 3: If carry remains after finishing the loop, append it to the result list.

Example:
999 + 1 = 1000
carry = 1 -> append to result

Step 4: Convert the resulting array into a linked list.

Use a dummy node to simplify linked list construction.

dummy -> 7 -> 0 -> 8

Return dummy.next as the head of the result list.

-------------------------------------------------

Time Complexity:
O(max(n, m))
n = length of first linked list
m = length of second linked list

Space Complexity:
O(n + m)
because we store digits in arrays.

-------------------------------------------------

Note:
This is a brute force solution because we convert linked lists into arrays before performing addition.
The optimal approach adds digits directly from the linked lists using pointers and carry.
"""
