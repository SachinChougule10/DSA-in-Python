# 234. Palindrome Linked List (Brute Force Solution)
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
        self.val = val  # value stored in node
        self.next = None  # pointer to next node


class Solution:
    def is_palindrome(self, head: Optional[Node]) -> bool:
        stack = []  # stack to store node values

        # Traverse the linked list and push all values into stack
        curr = head
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next

        # Traverse again and compare with stack elements (reverse order)
        curr = head
        while curr is not None:
            e = stack.pop()  # pop gives last inserted element (reverse order)
            if curr.val != e:  # if values don't match, not a palindrome
                return False
            curr = curr.next

        return True  # all values matched → palindrome


obj = Solution()

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print(obj.is_palindrome(head))  # Output: True

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)

print(obj.is_palindrome(head1))  # Output: False

"""
Logic:

1. Traverse the linked list and store all node values in a stack.
   Example:
   Linked List: 1 → 2 → 2 → 1
   Stack: [1, 2, 2, 1]

2. Traverse the linked list again from the head.

3. Pop elements from the stack and compare them with the current node value.
   Since stack follows LIFO (Last In First Out), popping gives elements in reverse order.

4. If at any point the values do not match → return False.

5. If all values match → the linked list is a palindrome.

Example Walkthrough:
Linked List: 1 → 2 → 2 → 1
Stack: [1,2,2,1]

Comparisons:
1 == 1
2 == 2
2 == 2
1 == 1

Result: True

Time Complexity: O(N)
- First traversal to fill stack → O(N)
- Second traversal to compare → O(N)

Space Complexity: O(N)
- Stack stores N elements.
"""
