# Geeks For Geeks : Find length of Loop (Brute Force Approach)
# Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
# Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to.
# If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

from typing import Optional


class Node:
    # Represents a node in a singly linked list.
    def __init__(self, val):
        self.val = val  # Value stored in the node
        self.next = None  # Pointer to the next node


class Solution:
    def length_of_loop(self, head: Optional[Node]) -> int:
        curr = head  # Pointer to traverse the linked list
        visited = {}  # Dictionary to store visited nodes with their index
        travel = 0  # Keeps track of traversal position (step count)

        # Traverse the linked list
        while curr is not None:
            # If current node already visited → loop detected
            if curr in visited:
                # Loop length = current index - first visited index
                count = travel - visited[curr]
                return count
            else:
                # Store node with its traversal index
                visited[curr] = travel
                travel += 1
                curr = curr.next  # Move to next node

        # If we reach None → no loop exists
        return 0


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
print(obj.length_of_loop(head))  # Output : 3

# Case 2: Linked list without a cycle
head = create_linked_list([3, 2, 0, -4], -1)
visualize_linked_list(head)
print(obj.length_of_loop(head))  # Output : 0

"""
Logic : 
Approach Used: Brute Force using Hashing (Dictionary)

1. We traverse the linked list using a pointer `curr`.
2. We maintain a dictionary `visited`:
   - Key   → Node reference
   - Value → Index (or step count) at which the node was visited.

3. As we traverse:
   - If the current node is NOT in visited:
        → Store it with its traversal index.
   - If the current node IS already in visited:
        → A loop is detected.
        → Loop length = current_travel_index - first_visited_index_of_that_node

4. If we reach None:
        → No loop exists → return 0.

Why this works:
If a node is visited again, that means we have come back to a previous node, which confirms the presence of a cycle.
The difference in indices gives the number of nodes in the loop.

Time Complexity: O(N)
Space Complexity: O(N)  (because of dictionary)

Note:
This is a brute force approach.
Optimal solution uses Floyd's Cycle Detection Algorithm (Tortoise & Hare) which works in O(N) time and O(1) space.
"""
