# GFG : Add Number Linked Lists (Brute Force Solution)
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


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def add_two_lists(self, head1, head2):

        arr1 = []
        arr2 = []

        # Traverse first linked list and store digits in arr1
        while head1:
            arr1.append(head1.val)
            head1 = head1.next

        # Traverse second linked list and store digits in arr2
        while head2:
            arr2.append(head2.val)
            head2 = head2.next

        # Reverse arrays so we can start addition from least significant digit
        arr1.reverse()
        arr2.reverse()

        carry = 0
        result = []

        # maximum length of both arrays
        n = max(len(arr1), len(arr2))

        # perform digit-by-digit addition
        for i in range(n):

            # if one list is shorter, treat missing value as 0
            x = arr1[i] if i < len(arr1) else 0
            y = arr2[i] if i < len(arr2) else 0

            # sum including carry
            s = x + y + carry

            # store the last digit
            result.append(s % 10)

            # update carry
            carry = s // 10

        # if carry remains, append it
        if carry:
            result.append(carry)

        # reverse result because digits should be in forward order
        result.reverse()

        # build result linked list
        dummy = Node(0)
        curr = dummy

        for num in result:
            curr.next = Node(num)
            curr = curr.next

        # return the head of the result list
        return dummy.next


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

Problem:
Two linked lists represent numbers where each node contains a single digit. The digits are stored in forward order.

Example:
1 -> 2 -> 3 represents the number 123
9 -> 9 -> 9 represents the number 999

Expected Result:
123 + 999 = 1122
Output list = 1 -> 1 -> 2 -> 2
-------------------------------------------------

Brute Force Approach (Array + Reverse)

Step 1: Convert both linked lists into arrays.

Example:
head1 -> arr1 = [1,2,3]
head2 -> arr2 = [9,9,9]

Step 2: Reverse both arrays so that addition starts from the least significant digit.
arr1 = [3,2,1]
arr2 = [9,9,9]

Step 3: Perform digit-by-digit addition while maintaining a carry.
Formula:

sum = digit1 + digit2 + carry
digit_to_store = sum % 10
new_carry = sum // 10

Example:

3 + 9 = 12  -> store 2, carry = 1
2 + 9 + 1 = 12 -> store 2, carry = 1
1 + 9 + 1 = 11 -> store 1, carry = 1

result = [2,2,1,1]

Step 4: Reverse the result array because digits were generated from least significant digit.
result = [1,1,2,2]

Step 5: Convert the result array into a linked list.

dummy -> 1 -> 1 -> 2 -> 2

Return dummy.next as the head of the resulting linked list.
-------------------------------------------------

Time Complexity:
O(N + M)

N = length of first linked list
M = length of second linked list

Space Complexity:
O(N + M)

Extra space is used to store digits in arrays.
-------------------------------------------------

Why Another Brute Force?

The previous brute force solution converted the linked lists into integers:

Linked List → Integer → Addition → Linked List

While this works in Python (because Python supports arbitrarily large integers), it can cause integer overflow in languages like C++ and Java when the number
represented by the linked list becomes very large.

To avoid this issue, this approach performs digit-by-digit addition instead of forming a single large integer.

Approach Used Here:

Linked List → Array → Reverse → Digit-wise Addition → Linked List

Comparison of Brute Force Approaches

Brute Force 1:
Linked List → Integer → Linked List  
Risk: Integer overflow in languages like C++ and Java.

Brute Force 2 (This Implementation):
Linked List → Array → Reverse → Digit-wise Addition → Linked List  
Advantage: Avoids integer overflow and works safely for very large numbers.
"""
