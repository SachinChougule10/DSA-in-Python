# Leetcode : 142. Linked List Cycle II : Given the head of a linked list, return the node where the cycle begins. (Optimal Solution)
# If there is no cycle, return null. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Note that pos is not passed as a parameter. Do not modify the linked list.

from typing import Optional


class Node:
    # Represents a node in a singly linked list.
    def __init__(self, val):
        self.val = val  # Value stored in the node
        self.next = None  # Reference to the next node


class Solution:
    def detectCycle(self, head: Optional[Node]) -> Optional[Node]:
        slow = head  # Moves one step at a time
        fast = head  # Moves two steps at a time

        # Phase 1: Detect cycle using slow & fast pointers
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                slow = head  # Reset slow to head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.val  # On LeetCode: return slow (node)

        # No cycle found
        return None


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
print(obj.detectCycle(head))  # Output : 2

# Case 2: Linked list without a cycle
head = create_linked_list([3, 2, 0, -4], -1)
visualize_linked_list(head)
print(obj.detectCycle(head))  # Output : None


"""
Logic (Optimal Solution - Floyd's Cycle Detection)

Goal:
Given the head of a linked list, detect whether a cycle exists and return the node where the cycle begins.

Note:
On LeetCode, we must return the NODE itself.
In this local implementation, node.val is returned for readable output.

----------------------------------------------------------
Phase 1: Cycle Detection
----------------------------------------------------------
1. Use two pointers:
   - slow pointer moves one step at a time.
   - fast pointer moves two steps at a time.

2. Initialize both pointers at the head of the linked list.

3. Traverse the list:
   - slow = slow.next
   - fast = fast.next.next

4. If the linked list does NOT contain a cycle,
   the fast pointer will reach None.

5. If a cycle exists, the fast pointer will eventually
   meet the slow pointer inside the cycle.

This confirms the presence of a cycle.

-----------------------------------------------------------
Phase 2: Finding the start of the cycle
-----------------------------------------------------------
Let:
- a = distance from head to the start of the cycle
- b = distance from cycle start to the meeting point
- c = remaining distance in the cycle

At the meeting point:
- slow has traveled (a + b)
- fast has traveled (a + b + c + b)

Since fast moves twice as fast as slow:
2(a + b) = a + 2b + c
⇒ a = c

This means:
The distance from the head to the cycle start is equal to the
distance from the meeting point to the cycle start.

---------------------------------------------------------------
How to locate the cycle start? 
---------------------------------------------------------------
1. Move the slow pointer back to the head.
2. Keep the fast pointer at the meeting point.
3. Move both pointers one step at a time.
4. The node where they meet again is the start of the cycle.

-------------------------
Complexity Analysis :-
-------------------------
Time Complexity: O(N)
Space Complexity: O(1)

--------------------------
Leetcode Requirement :- 
--------------------------
Return the node where the cycle begins.
Do NOT return node.val on LeetCode submissions.
"""
