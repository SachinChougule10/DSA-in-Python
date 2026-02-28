# Geeks For Geeks : Find length of Loop (Optimal Solution)
# Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
# Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to.
# If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.


from typing import Optional


class Node:
    # Represents a node in a singly linked list.
    def __init__(self, val):
        self.val = val  # Value stored in the node
        self.next = None  # Reference to the next node


class Solution:
    def length_of_loop(self, head: Optional[Node]) -> Optional[Node]:
        slow = head  # Slow pointer moves one step at a time
        fast = head  # Fast pointer moves two steps at a time

        # Step 1: Detect cycle using Floyd’s Algorithm
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow by 1
            fast = fast.next.next  # Move fast by 2

            # If both pointers meet, cycle exists
            if slow == fast:
                # Step 2: Count length of the loop
                slow = slow.next  # Move slow one step ahead
                count = 1  # Initialize loop length counter

                # Traverse the loop until we reach the same node again
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count  # Return loop length

        # If fast reaches None → no cycle
        return 0


# Helper Function: Linked List Creation (NOT required for LeetCode). Used only for local testing & debugging
#  Creates a linked list from a list of values. Optionally introduces a cycle using 'pos'. If pos != -1, creates a cycle by connecting last node to index 'pos'.
def create_linked_list(arr, pos):

    if not arr:
        return

    # Create all nodes first
    nodes = [Node(val) for val in arr]

    # Link nodes sequentially
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if pos is valid
    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# Helper Function: Visualization (NOT required for LeetCode). Used only for understanding & debugging
def visualize_linked_list(head, limit=10):

    # Safely prints linked list values.
    # A linked list that contains a cycle will never reach None, so traversing it normally would result in an infinite loop.
    # To prevent this during visualization, we use a limit to stop traversal after a fixed number of steps.

    curr = head
    count = 0
    while curr is not None and count < limit:
        print(curr.val, end=" -> ")
        curr = curr.next
        count += 1

    if curr is not None:
        print("     ....cycle detected")
    else:
        print("None", end="     ....cycle not detected\n")


obj = Solution()

# Case 1: Linked list with a cycle
head = create_linked_list([3, 2, 0, -4], 1)
visualize_linked_list(head)
print(obj.length_of_loop(head))  # Output : 3

# Case 2: Linked list without a cycle
head = create_linked_list([3, 2, 0, -4], -1)
visualize_linked_list(head)
print(obj.length_of_loop(head))  # Output : 0

"""
Logic:

Approach Used: Floyd's Cycle Detection Algorithm (Tortoise & Hare)

Step 1: Detect Cycle
- Use two pointers:
    slow → moves 1 step at a time
    fast → moves 2 steps at a time
- If there is a cycle, slow and fast will eventually meet.
- If fast reaches None, there is no cycle.

Step 2: Count Loop Length
- Once slow == fast (cycle detected), keep one pointer fixed.
- Move the other pointer one step at a time until it reaches the same node again.
- Count the number of steps taken.
- That count is the length of the loop.

Why this works:
Inside a cycle, the fast pointer gains one step over slow
each iteration, so they must meet inside the loop.

Time Complexity: O(N)
Space Complexity: O(1)

This is optimal because:
- No extra data structures are used.
- Works in constant space.
"""
