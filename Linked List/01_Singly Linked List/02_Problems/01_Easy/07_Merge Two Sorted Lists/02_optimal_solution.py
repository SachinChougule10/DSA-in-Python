# Leetcode : 21. Merge Two Sorted Lists : You are given the heads of two sorted linked lists list1 and list2 (Optimal Solution)
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def merge_two_lists(self, list1: Optional[Node], list2: Optional[Node]):
        # Create a dummy node to simplify edge cases
        dummy_node = Node(0)
        tail = dummy_node  # Tail pointer to build merged list

        # Traverse both lists until one becomes empty
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1  # Attach smaller node
                list1 = list1.next  # Move list1 forward
            else:
                tail.next = list2  # Attach smaller node
                list2 = list2.next  # Move list2 forward
            tail = tail.next  # Move tail forward

        # Attach remaining nodes (only one of these will execute)

        if list1 is not None:
            tail.next = list1

        if list2 is not None:
            tail.next = list2

        # Return merged list (skip dummy node)
        return dummy_node.next


# visualize linked list
def visaulize_ll(head):
    curr = head

    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


# create linked list 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(4)

# create linked list 2
head2 = Node(1)
head2.next = Node(3)
head2.next.next = Node(4)

obj = Solution()
new_head = obj.merge_two_lists(head1, head2)

visaulize_ll(new_head)  # Output : 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

"""
LOGIC (Optimal Approach - Two Pointer Technique):

1. Create a dummy node to simplify handling of the head.
2. Use a tail pointer to build the merged linked list.
3. Compare nodes of list1 and list2:
   - Attach the smaller node to tail.
   - Move the corresponding list pointer forward.
4. Move the tail pointer forward after each insertion.
5. When one list becomes empty, attach the remaining part of the other list.
6. Return dummy_node.next as the head of the merged list.

---------------------------------------------------------------------

TIME COMPLEXITY (TC):

Let:
n = number of nodes in list1
m = number of nodes in list2

- We traverse both lists only once.
- Each node is visited exactly once.

Final TC:
O(n + m)

---------------------------------------------------------------------

SPACE COMPLEXITY (SC):

- No extra data structures are used.
- We are reusing existing nodes (in-place merge).
- Only a dummy node and pointers are used.

Final SC:
O(1)

---------------------------------------------------------------------

WHY THIS IS OPTIMAL:

- No sorting is required.
- No extra space like arrays is used.
- Directly merges in linear time using two pointers.
"""
