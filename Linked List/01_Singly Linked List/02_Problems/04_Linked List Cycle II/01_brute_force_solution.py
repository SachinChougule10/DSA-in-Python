# Leetcode : 142. Linked List Cycle II : Given the head of a linked list, return the node where the cycle begins. (Brute Force Solution)
# If there is no cycle, return null. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Note that pos is not passed as a parameter. Do not modify the linked list.

from typing import Optional


class Node:
    # Represents a node in a singly linked list.
    def __init__(self, val):
        self.val = val  # Value stored in the node
        self.next = None  # Pointer to the next node


class Solution:
    def detectCycle(self, head: Optional[Node]) -> Optional[Node]:
        curr = head  # Start traversal from head
        visited = set()  # Set to store visited node references

        # Traverse the linked list
        while curr is not None:
            # If current node is already visited, cycle starts here
            if curr in visited:
                return curr.val  # On LeetCode: return curr (node itself)
            visited.add(curr)  # Mark current node as visited
            curr = curr.next  # Move to the next node

        # If traversal ends, no cycle exists
        return None


# Helper Function: Linked List Creation (NOT required for LeetCode). Used only for local testing & debugging
# Creates a linked list from array. If pos != -1, creates a cycle by connecting last node to index 'pos'.
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
print(obj.detectCycle(head))  # Output : 2

# Case 2: Linked list without a cycle
head = create_linked_list([3, 2, 0, -4], -1)
visualize_linked_list(head)
print(obj.detectCycle(head))  # Output : None

"""
Logic (Brute Force):

1. Traverse the linked list node by node.
2. Store each visited node's reference in a set.
3. If a node is encountered again, it means a cycle exists.
4. The first repeated node is the starting point of the cycle.
5. If traversal reaches None, no cycle is present.

Time Complexity: O(N)
Space Complexity: O(N) due to hash set

LeetCode Requirement:
- Return the node where the cycle begins (NOT node.val).
"""
