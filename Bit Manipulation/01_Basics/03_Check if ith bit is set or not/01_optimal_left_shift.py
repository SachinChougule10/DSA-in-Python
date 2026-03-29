# Problem: Check if i-th Bit is Set (Using Left Shift)
#
# Description:
# This program checks whether the i-th bit (0-based index from right)
# of a given integer is set (1) or not (0) using bit manipulation.
#
# It uses a bit mask created by left shifting 1 to the i-th position.
#
# Example:
# Input: n = 13 (1101), i = 2 → Output: True
# Input: n = 13 (1101), i = 1 → Output: False
#
# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def check_if_set(self, n: int, i: int):
        # Create a mask by left shifting 1 by i positions → (1 << i)
        # Perform AND with n:
        # - If result is non-zero → bit is set
        # - If result is zero → bit is not set
        if n & (1 << i) != 0:
            return True
        else:
            return False


obj = Solution()
print(obj.check_if_set(13, 2))  # Output : True
print(obj.check_if_set(13, 1))  # Output : False

"""
Logic: Check if i-th Bit is Set (Left Shift Method)

Goal:
Check whether the i-th bit of a number is 1 (set) or 0 (unset).

Key Idea:
- Create a bitmask with only the i-th bit set using (1 << i).
- Perform bitwise AND with the number.
- If result is non-zero → bit is set.

Expression Used:
n & (1 << i)

Steps:
1) Create mask:
   (1 << i)
   - This shifts 1 to the i-th position.

2) Perform AND with n:
   - If result ≠ 0 → bit is set (True)
   - If result = 0 → bit is not set (False)

Example:
n = 13 → binary = 1101

Check i = 2:
Mask = 1 << 2 = 0100
1101 & 0100 = 0100 → True

Check i = 1:
Mask = 1 << 1 = 0010
1101 & 0010 = 0000 → False

Time Complexity: O(1)
Space Complexity: O(1)
"""
