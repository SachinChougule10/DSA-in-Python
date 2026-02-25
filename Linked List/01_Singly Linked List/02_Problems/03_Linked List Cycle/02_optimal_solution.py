# Leetcode : 141. Linked List Cycle : Given head, the head of a linked list, determine if the linked list has a cycle in it. (Optimal Solution)
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


from typing import Optional


class Node:
    # Represents a node in a singly linked list.
    def __init__(self, val):
        self.val = val  # Value stored in the node
        self.next = None  # Reference to the next node


class Solution:
    def hasCycle(self, head: Optional[Node]) -> bool:

        # Detects whether a linked list contains a cycle using Floyd's Cycle Detection Algorithm.

        slow = head  # Moves one step at a time
        fast = head  # Moves two steps at a time

        # Continue traversal as long as fast pointer can safely move two steps
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow by 1 step
            fast = fast.next.next  # Move fast by 2 steps

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # Fast reached None → no cycle
        return False


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
        print(" ....cycle detected")
    else:
        print("None", end=" ....cycle not detected\n")


obj = Solution()

# Case 1: Linked list with a cycle
head1 = create_linked_list([3, 2, 0, -4], 1)
visualize_linked_list(head1)
print(obj.hasCycle(head1))  # Output : True

# Case 2: Linked list without a cycle
head2 = create_linked_list([3, 2, 0, -4], -1)
visualize_linked_list(head2)
print(obj.hasCycle(head2))  # Output : False

"""
Logic (Floyd's cycle detection algorithm):

1. Use two pointers:
   - Slow pointer moves one step at a time.
   - Fast pointer moves two steps at a time.

2. Traverse the linked list:
   - If the list has no cycle, the fast pointer will reach None.
   - If the list has a cycle, the fast pointer will eventually meet the slow pointer inside the loop.

3. If slow and fast pointers meet at any point:
   - A cycle exists → return True.

4. If the loop ends because fast or fast.next becomes None:
   - No cycle exists → return False.

Why this works? :
- In a cyclic list, the fast pointer will always "lap" the slow pointer, similar to runners on a circular track.

Time Complexity:
- O(n), where n is the number of nodes.

Space complexity:
- O(1), since no extra memory is used.

"""
