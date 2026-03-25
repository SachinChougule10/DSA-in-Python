# Leetcode : 203. Remove Linked List Elements (Brute Force Solution)
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val  # Store value of node
        self.next = None  # Pointer to next node


class Solution:
    def remove_elements(self, head: Optional[Node], val: int) -> Optional[Node]:
        values = []  # List to store all node values
        new_values = []  # List to store filtered values
        curr = head  # Pointer to traverse the linked list

        # Step 1: Traverse linked list and store values in array
        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        # Step 2: Filter out elements equal to 'val'
        for num in values:
            if num != val:
                new_values.append(num)

        # Step 3: Rebuild linked list using filtered values
        dummy = Node(0)  # Dummy node to simplify list creation
        tail = dummy  # Tail pointer to build the new list

        for num in new_values:
            new_node = Node(num)  # Create new node
            tail.next = new_node  # Attach node to list
            tail = tail.next  # Move tail forward

        return dummy.next  # Return head of new list (skip dummy)


# visualize linked list
def visualize(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# linked list creation
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

head2 = Node(11)
head2.next = Node(12)
head2.next.next = Node(13)
head2.next.next.next = Node(14)
head2.next.next.next.next = Node(15)

obj = Solution()

new_head = obj.remove_elements(head1, 1)
visualize(new_head)  # Output : 2 -> 3 -> 4 -> 5 -> None

new_head = obj.remove_elements(head2, 15)
visualize(new_head)  # Output : 11 -> 12 -> 13 -> 14 -> None

"""
Logic:
Approach:
---------
This is a brute force approach where we do the problem in 3 steps:

1. Convert Linked List → Array
   - Traverse the linked list using a pointer (curr)
   - Store each node value into a list (values)

2. Filter the Array
   - Iterate through the values list
   - Add only those elements to new_values where num != val
   - This effectively removes all occurrences of val

3. Convert Array → Linked List
   - Create a dummy node to simplify list creation
   - Use a tail pointer to build the new linked list
   - For each value in new_values:
       → Create a new node
       → Attach it to the list
       → Move tail forward

Key Insight:
------------
- Instead of modifying the original linked list, we rebuild a new one
- This avoids pointer manipulation complexity
- But it uses extra space, so it's not optimal

Edge Cases:
-----------
1. Empty list → values = [] → return None
2. All nodes equal to val → new_values = [] → return None
3. No node equals val → list remains unchanged
4. Single node → handled naturally

Time Complexity:
----------------
O(n)
- One pass to store values
- One pass to filter
- One pass to rebuild

Space Complexity:
-----------------
O(n)
- Extra space for array + new linked list
"""
