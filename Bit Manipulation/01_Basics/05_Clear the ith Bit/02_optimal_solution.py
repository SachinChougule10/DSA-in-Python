# Problem: Clear i-th Bit (Optimal using Bit Manipulation)

# Description:
# This program clears (sets to 0) the i-th bit (0-based index from right) of a given integer using bitwise operations.

# If the bit is already 0, the number remains unchanged.

# Example:
# Input: n = 9 (1001), i = 2 → Output: 9 (1001)
# Input: n = 13 (1101), i = 2 → Output: 9 (1001)

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def clear_ith_bit(self, n: int, i: int):
        # (1 << i) creates a number with only i-th bit set
        # ~(1 << i) flips all bits → i-th bit becomes 0, others become 1
        # AND with n clears the i-th bit while keeping others unchanged
        return n & ~(1 << i)


obj = Solution()
print(obj.clear_ith_bit(9, 2))  # Output : 9
print(obj.clear_ith_bit(13, 2))  # Output : 9

"""
Logic: Clear i-th Bit (Optimal)

Goal:
Set the i-th bit of a number to 0.

Key Idea:
- Create a mask where all bits are 1 except the i-th bit (which is 0).
- Perform AND with the number to clear that bit.

Expression Used:
n & ~(1 << i)

------------------------------------------------------------
Step-by-Step Breakdown
------------------------------------------------------------

1) Create mask with i-th bit set:
   (1 << i)

   Example:
   i = 2 → 00000100

2) Invert the mask:
   ~(1 << i)

   Example:
   00000100 → 11111011
   - All bits = 1 except i-th bit = 0

3) Perform AND with n:
   n & mask

   - 1 & 1 = 1 → unchanged
   - 1 & 0 = 0 → cleared

------------------------------------------------------------
Example Walkthrough
------------------------------------------------------------

n = 13 → binary = 1101
i = 2

Step 1: (1 << 2) = 0100
Step 2: ~(0100) = 1011
Step 3: 1101 & 1011 = 1001 → 9

------------------------------------------------------------
Edge Case:
------------------------------------------------------------

n = 9 → binary = 1001
i = 2

Step 1: mask = 0100
Step 2: ~mask = 1011
Step 3: 1001 & 1011 = 1001 → unchanged

------------------------------------------------------------
Time Complexity: O(1)
Space Complexity: O(1)
"""
