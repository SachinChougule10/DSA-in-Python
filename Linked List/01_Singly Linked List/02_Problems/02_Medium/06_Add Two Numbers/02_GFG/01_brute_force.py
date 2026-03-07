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
        num1 = 0
        curr = head1

        # Convert first linked list into integer
        while curr is not None:
            num1 = num1 * 10 + curr.val
            curr = curr.next

        num2 = 0
        curr = head2

        # Convert second linked list into integer
        while curr is not None:
            num2 = num2 * 10 + curr.val
            curr = curr.next

        # Add both numbers
        total = num1 + num2

        # Dummy node to build the result linked list
        dummy = Node(0)
        curr = dummy

        # Convert result number into digits and create linked list, so traversing becomes easy
        for digit in str(total):
            curr.next = Node(int(digit))  # convert character to integer
            curr = curr.next

        # Return head of the result list
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
Brute Force Approach

This solution converts the linked lists into integers, adds them, and then converts the resulting number back into a linked list.

Steps:

1. Traverse the first linked list and construct the number.
   Example:
   1 -> 2 -> 3
   num1 = 123

2. Traverse the second linked list and construct the number.
   Example:
   9 -> 9 -> 9
   num2 = 999

3. Add the two numbers:
   total = num1 + num2

4. Convert the resulting number into a string so that each digit can be accessed individually.

5. Create a new linked list where each node stores one digit of the result.

Example:
1122 -> 1 -> 1 -> 2 -> 2


Time Complexity:
O(N + M)

N = length of first linked list
M = length of second linked list


Space Complexity:
O(max(N, M))

Used for creating the result linked list.


Limitation:

This approach may fail in languages like C++ or Java for extremely large numbers due to integer overflow.

Therefore the optimal approach performs digit-by-digit addition directly using linked list operations instead of converting the entire number.
"""
