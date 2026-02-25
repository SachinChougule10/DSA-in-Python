# Leetcode : 141. Linked List Cycle : Given head, the head of a linked list, determine if the linked list has a cycle in it. (Brute Force Solution)
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

from typing import Optional


class Node:
    # Represents a node in a singly linked list.
    def __init__(self, val):
        self.val = val  # Stores node value
        self.next = None  # Pointer to next node


class Solution:
    def hasCycle(self, head: Optional[Node]) -> bool:
        curr = head  # Start traversal from head
        visited = set()  # Stores references of visited nodes

        while curr is not None:
            # If current node was already visited, a cycle exists
            if curr in visited:
                return True
            visited.add(curr)  # Mark current node as visited
            curr = curr.next  # Move to the next node

        # Reached None → no cycle
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
Logic (Brute Force Approach):

1. Start from the head of the linked list.
2. Maintain a set to store references of visited nodes.
3. Traverse the list node by node:
   - If the current node is already present in the set, it means we have revisited a node → cycle exists.
   - Otherwise, add the node to the set and move forward.
4. If traversal reaches None, the list ends normally, meaning no cycle exists.

WHY THIS WORKS:
- Each node has a unique memory reference.
- Re-visiting the same node means a loop is present.

TIME COMPLEXITY:
- O(n) where n is the number of nodes.

SPACE COMPLEXITY:
- O(n) due to the visited set.

"""
