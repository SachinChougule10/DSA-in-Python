# Problem: Set i-th Bit (Using Left Shift)

# Description:
# This program sets the i-th bit (0-based index from right) of a given integer to 1 using bit manipulation.

# If the bit is already set, the number remains unchanged.

# Example:
# Input: n = 9 (1001), i = 2 → Output: 13 (1101)
# Input: n = 13 (1101), i = 2 → Output: 13 (1101)

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def set_ith_bit(self, n: int, i: int):
        # Create a mask with only i-th bit set using left shift
        # Perform OR operation:
        # - If bit is 0 → it becomes 1
        # - If bit is already 1 → remains unchanged
        return n | (1 << i)


obj = Solution()
print(obj.set_ith_bit(9, 2))  # Output : 13
print(obj.set_ith_bit(13, 2))  # Output : 13

"""
Logic: Set i-th Bit

Goal:
Set the i-th bit of a number to 1.

Key Idea:
- Use left shift to create a mask with only the i-th bit set.
- Use bitwise OR to set the bit.

Expression Used:
n | (1 << i)

Steps:
1) Create mask:
   (1 << i)
   - Shifts 1 to the i-th position.

2) Perform OR with n:
   - If bit is 0 → becomes 1
   - If bit is already 1 → remains unchanged

Example:
n = 9 → binary = 1001

Set i = 2:
Mask = 1 << 2 = 0100
1001 | 0100 = 1101 → 13

n = 13 → binary = 1101

Set i = 2:
Mask = 0100
1101 | 0100 = 1101 → unchanged

Time Complexity: O(1)
Space Complexity: O(1)
"""
