# GFG: Intersection of Two Linked Lists
# Given two linked lists head1 and head2, find the intersection of two linked lists. Each of the two linked lists contains distinct node values.
# Note: The order of nodes in this list should be the same as the order in which those particular nodes appear in input head1 and return null if no common element is present.

# Examples:
# Input: LinkedList1: 9->6->4->2->3->8 , LinkedList2: 1->2->8->6
# Output: 6->2->8
# Explanation: Nodes 6, 2 and 8 are common in both of the lists and the order will be according to LinkedList1.

# Input: LinkedList1: 5->3->1->13->14 , LinkedList2: 3->13
# Output: 3->13
# Explanation: Nodes 3 and 13 are common in both of the lists and the order will be according to LinkedList1.

# Expected time complexity: O(m+n)
# Expected auxiliary space: O(m+n)

# Constraints:
# 1 <= no. of nodes in head1, head2 <= 104
# 1 <= node->data <= 105

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val  # stores the value of the node
        self.next = None  # pointer to the next node


class Solution:
    def find_intersection(self, head1: Optional[Node], head2: Optional[Node]):
        hash_set = set()  # stores values from the second linked list

        curr2 = head2
        while curr2 is not None:
            hash_set.add(curr2.val)  # insert values of head2 for O(1) lookup
            curr2 = curr2.next

        dummy = Node(0)  # dummy node to simplify result list creation
        tail = dummy  # tail pointer to build the result list

        curr1 = head1
        while curr1 is not None:
            # if value exists in second list, it is part of intersection
            if curr1.val in hash_set:
                tail.next = Node(curr1.val)  # create new node in result list
                tail = tail.next  # move tail forward

            curr1 = curr1.next

        return dummy.next  # return head of the new intersection list


def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


head1 = Node(9)
head1.next = Node(6)
head1.next.next = Node(4)
head1.next.next.next = Node(2)
head1.next.next.next.next = Node(3)
head1.next.next.next.next.next = Node(8)


head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(8)
head2.next.next.next = Node(6)

obj = Solution()

visualize_ll(head1)  #  9 -> 6 -> 4 -> 2 -> 3 -> 8 -> None
visualize_ll(head2)  #  1 -> 2 -> 8 -> 6 -> None

new_head = obj.find_intersection(head1, head2)
visualize_ll(new_head)  # Output : 6 -> 2 -> 8 -> None

"""
Logic Explanation
-----------------

1. Traverse the second linked list and store all node values in a hash set. This allows constant time membership checking.

2. Traverse the first linked list. For each node, check whether its value exists in the hash set.

3. If the value exists, it means the value is common to both lists. Create a new node and append it to the result linked list.

4. A dummy node is used to simplify result list construction and avoid handling special cases for the first node.

5. Finally return dummy.next which points to the head of the intersection list.

Time Complexity
---------------
O(m + n)
m = number of nodes in head1
n = number of nodes in head2

Space Complexity
----------------
O(m + n)
Extra space is used for the hash set and the resulting linked list.

Difference from LeetCode Intersection Problem
----------------------------------------------

This problem is different from LeetCode "Intersection of Two Linked Lists".

In this GFG problem:
- Intersection is based on COMMON VALUES.
- A new linked list is created containing those common values.
- The order must follow head1.

In the LeetCode problem:
- Intersection means the two linked lists share the SAME NODE reference.
- We return the node where the lists physically merge.
- No new list is created.
"""
