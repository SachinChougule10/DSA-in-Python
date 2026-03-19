# Leetcode : 148. Sort List : Given the head of a linked list, return the list after sorting it in ascending order (Optimal Solution)
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
        # Base case: empty list or single node is already sorted
        if head is None or head.next is None:
            return head

        left = head
        right = self.getMid(head)  # Find the middle node of the list

        # Split the list into two halves
        temp = right.next  # Save the start of the right half
        right.next = None  # Cut the left half here
        right = temp  # Right half starts from temp

        left = self.sortList(left)  # Recursively sort left half
        right = self.sortList(right)  # Recursively sort right half

        return self.merge(left, right)  # Merge both sorted halves

    def getMid(self, head):
        slow = head  # Moves one step at a time
        fast = head.next  # Moves two steps at a time (offset by 1 to get left-mid)

        # When fast reaches end, slow is at the middle
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow by 1
            fast = fast.next.next  # Move fast by 2

        return slow  # Slow pointer is now at the midpoint

    def merge(self, list1, list2):
        dummy = Node(0)  # Sentinel node to simplify edge cases
        tail = dummy  # Tail always points to the last node in merged list

        # Compare and attach the smaller node at each step
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1  # Attach list1's node
                list1 = list1.next  # Advance list1
            else:
                tail.next = list2  # Attach list2's node
                list2 = list2.next  # Advance list2
            tail = tail.next  # Move tail forward

        # Attach remaining nodes (at most one list has leftover nodes)
        if list1 is not None:
            tail.next = list1

        if list2 is not None:
            tail.next = list2

        return dummy.next  # Return merged list, skipping sentinel


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
visualize_dll(new_head)  # Output : 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> None

"""
Logic :
Algorithm: Top-Down Merge Sort

Why Merge Sort for Linked Lists?
---------------------------------
Arrays support random access, so QuickSort and HeapSort work well on them. Linked lists do NOT support random access (no index jumping),
but they DO support efficient sequential splitting and pointer rewiring — exactly what Merge Sort needs. This gives us O(n log n) guaranteed, with no extra array.

Step-by-step Breakdown
------------------------

1. BASE CASE  [sortList]
   - If head is None or head.next is None, the list is 0 or 1 node.
   - A single node is already sorted — return it immediately.
   - This is the condition that stops recursion from going forever.

2. FIND MIDDLE  [getMid]
   - Use Floyd's slow/fast pointer technique.
   - slow starts at head, fast starts at head.NEXT (not head — see below).
   - Each iteration: slow moves 1 step, fast moves 2 steps.
   - When fast cannot move further, slow sits at the LEFT midpoint.

   Why fast starts at head.next (critical detail):
   ┌─────────────────────────────────────────────────────────┐
   │  List: [4] → [2]   (2 nodes)                            │
   │                                                         │
   │  If fast = head:   slow=4, fast=4 → fast.next=2 ≠ None  │
   │                    slow=2, fast=None → loop ends        │
   │                    slow lands on node 2 (last node)     │
   │                    right.next = None → right is EMPTY   │
   │                    → left=[4,2], right=[] → infinite!   │
   │                                                         │
   │  If fast = head.next: fast=2, fast.next=None → stops    │
   │                    slow stays at node 4 (first node)    │
   │                    right.next = node 2 → right=[2]      │
   │                    → left=[4], right=[2] → correct!     │
   └─────────────────────────────────────────────────────────┘

3. SPLIT  [sortList]
   - temp = right.next  →  save the start of the right half
   - right.next = None  →  physically cut the list (left half ends here)
   - right = temp       →  right half begins from saved pointer
   - Now two independent lists exist in memory.

4. RECURSE  [sortList]
   - sortList(left)  → keeps halving until base case is hit
   - sortList(right) → same
   - Each call returns a sorted sublist.
   - The call stack unwinds bottom-up, merging on the way back up.

   Recursion tree for [4, 2, 1, 3]:
                  [4, 2, 1, 3]
                 /             \
           [4, 2]             [1, 3]
           /    \             /    \
         [4]   [2]          [1]   [3]
           \    /             \    /
           [2, 4]             [1, 3]
                 \             /
               [1, 2, 3, 4]  ← final merged result

5. MERGE  [merge]
   - A dummy sentinel node is created: dummy = Node(0)
     This avoids special-casing the very first node attachment.
     The real merged list starts at dummy.next.
   - tail always points to the last attached node.
   - Compare list1.val vs list2.val:
       if list1 is smaller → attach list1, advance list1
       else                → attach list2, advance list2
       move tail forward after each attachment.
   - When one list is exhausted, directly attach the remainder of the other (it's already sorted, no need to walk it).
   - Return dummy.next as the new head.

   Trace for merge([2,4], [1,3]):
   ┌────────────────────────────────────────────────────┐
   │  dummy → ?                                         │
   │  compare 2 vs 1 → take 1   dummy → 1               │
   │  compare 2 vs 3 → take 2   dummy → 1 → 2           │
   │  compare 4 vs 3 → take 3   dummy → 1 → 2 → 3       │
   │  list2 empty    → append 4 dummy → 1 → 2 → 3 → 4   │
   │  return dummy.next = 1                             │
   └────────────────────────────────────────────────────┘

Complexity
-----------
  Time  : O(n log n)
          — log n levels of splitting (list halves each time)
          — O(n) total work done across all merges at each level
  Space : O(log n)
          — no auxiliary arrays are used
          — only the recursion call stack (depth = log n levels)
          — optimal for a linked list sort
"""
