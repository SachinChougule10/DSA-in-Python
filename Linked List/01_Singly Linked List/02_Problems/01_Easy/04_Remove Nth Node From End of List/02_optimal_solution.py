# Leetcode : 19. Remove Nth Node From End of List : Given the head of a linked list, remove the nth node from the end of the list and return its head (OptimalSolution)

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def remove_Nth_from_end(self, head: Optional[Node], n: int) -> Optional[Node]:
        slow = head
        fast = head

        # for _ in range(n):
        #     fast = fast.next

        # Move fast pointer n steps ahead
        for _ in range(n):
            if fast is None:  # Case: n > length of list
                return head
            fast = fast.next

        # If fast becomes None after moving n steps, it means we need to remove the head node
        if fast is None:
            head = head.next
            return head

        # Move both pointers until fast reaches the last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # slow is just before the node to delete
        slow.next = slow.next.next

        return head


# Helper Function: Visualization (NOT required for LeetCode). Used only for understanding & debugging
def visualize_ll(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


obj = Solution()

# Linked List creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


head1 = obj.remove_Nth_from_end(head, 2)
visualize_ll(head1)  # Output : 1 -> 2 -> 3 -> 5 -> None

# Linked List creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head2 = obj.remove_Nth_from_end(head, 5)
visualize_ll(head2)  # Output : 2 -> 3 -> 4 -> 5 -> None

# Linked List creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head3 = obj.remove_Nth_from_end(head, 6)
visualize_ll(head3)  # Output : 1 -> 2 -> 3 -> 4 -> 5 -> None


"""
Logic:

Approach:
We use the Two Pointer (Fast & Slow) technique.

Step 1:
Move the fast pointer n steps ahead.

    Why do we check "if fast is None" inside the loop?

    While moving fast pointer n steps ahead, it is possible that n is greater than the length of the list.

    If we do not check this condition, fast may become None and accessing 'fast.next' will raise an AttributeError.

    Hence we check:
        if fast is None:
            return head

    This safely handles the case where n > length.

Step 2:
If fast becomes None after moving n steps, it means we must remove the head node.

Step 3:
Otherwise, move both slow and fast together until fast reaches the last node.

At this point:
- slow will be just before the node to delete.
- So we update:
      slow.next = slow.next.next

Edge Cases:
1. n == length of list → remove head.
2. n > length → return original list.
3. Single node list.

Time Complexity: O(L)

Where:
L = length of the linked list.

Explanation:

1) First loop runs at most 'n' times.
2) Second loop runs (L - n) times.

Total operations:
n + (L - n) = L

So overall traversal is linear.

Even though we use two loops, we are NOT traversing the list twice fully.

Hence Time Complexity = O(L)

Space Complexity:
O(1) → No extra space used.

Why This Is Optimal?
Because we solve it in one pass instead of counting length first and then traversing again.
"""
