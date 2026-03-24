# Leetcode : 21. Merge Two Sorted Lists : You are given the heads of two sorted linked lists list1 and list2 (Brute Force Solution)
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
        result = []  # This will store all values from both linked lists

        # Traverse first linked list and store values
        curr = list1
        while curr is not None:
            result.append(curr.val)
            curr = curr.next

        # Traverse second linked list and store values
        curr = list2
        while curr is not None:
            result.append(curr.val)
            curr = curr.next

        # Sort all collected values
        result.sort()

        # Create a dummy node to build the new linked list
        dummy_node = Node(0)
        tail = dummy_node  # Tail pointer to build list

        # Create new nodes from sorted values
        for i in result:
            new_node = Node(i)
            tail.next = new_node  # Attach new node
            tail = new_node  # Move tail forward

        # Return head of merged list (skip dummy node)
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
LOGIC (Brute Force Approach):

1. Traverse list1 and store all values in an array.
2. Traverse list2 and store all values in the same array.
3. Sort the combined array.
4. Create a new linked list using the sorted values.
5. Return the head of the new merged list.

WHY IT WORKS:
- Since both lists are already sorted, combining and sorting ensures correct order.
- We rebuild a fresh linked list to maintain structure.

---------------------------------------------------------------------

TIME COMPLEXITY (TC):

Let:
n = number of nodes in list1
m = number of nodes in list2

Step-by-step:

1. Traversing list1 → O(n)
2. Traversing list2 → O(m)
   → Combined traversal = O(n + m)

3. Sorting the array of size (n + m):
   → O((n + m) log(n + m))  ← Dominant step

4. Creating new linked list:
   → O(n + m)

Final TC:
O(n + m) + O((n + m) log(n + m)) + O(n + m)

Ignoring smaller terms:
TC = O((n + m) log(n + m))

Reason:
Sorting takes more time than linear traversal, so it dominates.

---------------------------------------------------------------------

SPACE COMPLEXITY (SC):

1. Array 'result' stores (n + m) elements:
   → O(n + m)

2. New linked list created:
   → O(n + m)

3. Dummy node and pointers:
   → O(1)

Final SC:
O(n + m) + O(n + m)

Ignoring constants:
SC = O(n + m)

---------------------------------------------------------------------

NOTE:
- This approach uses extra space and sorting, so it is not optimal.
- Optimal solution avoids sorting and works in:
  → O(n + m) time
  → O(1) space (in-place merge using pointers)
"""
