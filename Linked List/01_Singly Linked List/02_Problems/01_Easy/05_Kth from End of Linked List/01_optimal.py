# Geeks For Geeks : Kth from End of Linked List
# You are given the head of a linked list and the number k, You have to return the kth node from the end of linkedList.
# If k is more than the number of nodes, then the return -1.
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getKthFromLast(self, head: Optional[Node], k: int) -> Optional[Node]:
        # If linked list is empty
        if not head:
            return -1

        slow = head  # Will eventually point to kth node from end
        fast = head  # Used to create a gap of k nodes

        # Move fast pointer k steps ahead
        for _ in range(k):
            # If k is greater than length of list
            if fast is None:
                return -1
            fast = fast.next

        # Move both pointers until fast reaches end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # slow now points to kth node from end
        return slow.val


obj = Solution()

# Linked List creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


print(obj.getKthFromLast(head, 2))  # Output : 4

# Linked List creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(obj.getKthFromLast(head, 5))  # Output : 1

# Linked List creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(obj.getKthFromLast(head, 6))  # Output : -1

"""
Logic:

Approach:
---------
We use the Two Pointer (Fast & Slow Pointer) technique.

1. Initialize two pointers:
   - slow = head
   - fast = head

2. Move the fast pointer k steps ahead.
   - This creates a gap of k nodes between slow and fast.
   - If fast becomes None before completing k steps,
     it means k > length of list → return -1.

3. Move both slow and fast one step at a time until fast becomes None.

4. When fast reaches the end, slow will be pointing at the kth node from the end.

Why This Works:
---------------
The gap of k nodes ensures that when fast reaches the end, slow is exactly k nodes behind it.

Time Complexity:
----------------
O(N) → Single traversal of the linked list.

Space Complexity:
-----------------
O(1) → No extra space used.

Edge Cases Handled:
-------------------
✔ Empty list
✔ k greater than length of list
✔ k equal to length of list
"""
