# Leetcode : 148. Sort List : Given the head of a linked list, return the list after sorting it in ascending order (Brute Force Solution)
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []

# GFG : Remove duplicates from a sorted doubly linked list
# Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.


# Example 1:
# Input:
# n = 6
# 1<->1<->1<->2<->3<->4
# Output:
# 1<->2<->3<->4
# Explanation:
# Only the first occurance of node with value 1 is retained, rest nodes with value = 1 are deleted.


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def sortList(self, head):
        # Edge case: empty list — nothing to sort
        if not head:
            return None

        # Step 1: Collect all node values
        my_list = []  # Auxiliary list to hold values
        curr = head  # Start traversal from the head

        while curr is not None:
            my_list.append(curr.val)  # Harvest the current node's value
            curr = curr.next  # Advance to the next node

        # Step 2: Sort the collected values
        my_list.sort()

        # Step 3: Write sorted values back into the original nodes
        curr = head
        n = len(my_list)

        for i in range(n):
            curr.val = my_list[i]  # Overwrite node value with sorted value
            curr = curr.next

        # Head pointer is unchanged; list is now sorted in-place
        return head


# Build a sample doubly linked list: 4 <-> 2 <-> 1 <-> 3 <-> 5 <-> 6
head = Node(4)
n1 = Node(2)
n2 = Node(1)
n3 = Node(3)
n4 = Node(5)
n5 = Node(6)

# Wire up forward (next) pointers
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Wire up backward (prev) pointers
n1.prev = head
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4


def visualize_dll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" <-> ")
        curr = curr.next
    print("None")


obj = Solution()
new_head = obj.sortList(head)
visualize_dll(new_head)  # Output :  1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> None

"""
Logic: 

    Sorts a singly/doubly linked list in ascending order using a brute-force approach: extract all values into a Python list, 
    sort them with the built-in Timsort (O(n log n)), then write the sorted values back into the existing nodes — 
    preserving the original node structure and pointers.

    Approach (Brute Force):
        1. Traverse the list once, collecting every node value into a plain list.
        2. Sort that list in-place.
        3. Traverse the list a second time, overwriting each node's value with the corresponding sorted value.

    Why brute force?
        - Avoids pointer manipulation entirely; sorting is delegated to Python.
        - Simple to reason about and debug.
        - Trade-off: uses O(n) extra space for the auxiliary list.

    Time  Complexity: O(n log n)  — dominated by the sort step.
    Space Complexity: O(n)        — auxiliary list holding all node values.

"""
