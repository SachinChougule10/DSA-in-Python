# GFG : Remove duplicates from a sorted doubly linked list (Optimal Solution)
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
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class Solution:
    def removeDuplicates(self, head):
        if not head:  # Edge case: empty list
            return None

        curr = head  # Start traversal from the head

        # Traverse until last node
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:  # Duplicate found
                duplicate = curr.next  # Hold reference to the duplicate node
                curr.next = duplicate.next  # Bypass the duplicate node

                if duplicate.next is not None:
                    # Repair the backward pointer of the node after duplicate
                    duplicate.next.prev = curr
            else:
                # No duplicate, move to the next node
                curr = curr.next

        return head


head = Node(1)
n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)

# Building the next pointers (forward direction)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Building the prev pointers (backward direction)
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
no_duplicates_head = obj.removeDuplicates(head)
visualize_dll(no_duplicates_head)  # Output: 1 <-> 2 <-> 3 <-> 4

"""
LOGIC — Remove Duplicates from a Sorted Doubly Linked List
============================================================

INTUITION:
    Since the list is already sorted, all duplicate values are guaranteed to be adjacent.
    This means we only need a single pass — no need for a set or nested loops.

ALGORITHM (Single Pass, In-Place):
    1. Start `curr` at the head.
    2. At each step, compare `curr.val` with `curr.next.val`.
    3. If they are equal (duplicate detected):
         a. Save the duplicate node (`curr.next`) in a temp variable.
         b. Redirect `curr.next` to skip over the duplicate (`duplicate.next`).
         c. If the node after the duplicate exists, update its `prev` pointer
            back to `curr` to maintain the doubly linked integrity.
         d. Do NOT advance `curr` — there may be more duplicates ahead with
            the same value (e.g., 1 <-> 1 <-> 1).
    4. If no duplicate, simply advance `curr` to `curr.next`.
    5. Repeat until `curr` or `curr.next` is None.

POINTER REPAIR (Key for Doubly Linked List):
    A singly linked list only needs: curr.next = duplicate.next
    A doubly linked list additionally needs: duplicate.next.prev = curr
    Skipping this step would leave a dangling backward pointer.

COMPLEXITY:
    Time  : O(n) — single traversal of the list.
    Space : O(1) — no auxiliary data structures; all edits are in-place.

EXAMPLE WALKTHROUGH:
    Input : 1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 4

    Step 1: curr=1, next=1 → duplicate, skip second 1
            1 <-> 1 <-> 2 <-> 3 <-> 4

    Step 2: curr=1, next=1 → duplicate, skip third 1
            1 <-> 2 <-> 3 <-> 4

    Step 3: curr=1, next=2 → no duplicate, advance curr

    Step 4: curr=2, next=3 → no duplicate, advance curr

    Step 5: curr=3, next=4 → no duplicate, advance curr

    Step 6: curr=4, next=None → loop exits

    Output: 1 <-> 2 <-> 3 <-> 4
"""
