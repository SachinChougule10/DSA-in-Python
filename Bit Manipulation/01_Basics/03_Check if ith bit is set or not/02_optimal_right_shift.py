# Problem: Check if i-th Bit is Set (Using Right Shift)

# Description:
# This program checks whether the i-th bit (0-based index from right) of a given integer is set (1) or not (0) using bit manipulation.

# Example:
# Input: n = 13 (1101), i = 2 → Output: True
# Input: n = 13 (1101), i = 1 → Output: False

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def check_if_set(self, n: int, i: int):
        # Right shift n by i positions and check last bit using AND with 1
        # If result is non-zero → bit is set
        if (n >> i) & 1 != 0:
            return True
        else:
            return False


obj = Solution()
print(obj.check_if_set(13, 2))  # Output : True
print(obj.check_if_set(13, 1))  # Output : False

"""
Logic: Check if i-th Bit is Set (Right Shift Method)

Goal:
Check whether the i-th bit of a number is 1 (set) or 0 (unset).

Key Idea:
- Use right shift to bring the i-th bit to the least significant position.
- Then use bitwise AND with 1 to extract that bit.

Expression Used:
(n >> i) & 1

Steps:
1) Right shift the number by i:
   - This moves the i-th bit to the last position.

2) Perform AND with 1:
   - If result = 1 → bit is set (True)
   - If result = 0 → bit is not set (False)

Example:
n = 13 → binary = 1101

Check i = 2:
1101 >> 2 = 0011
0011 & 0001 = 1 → True

Check i = 1:
1101 >> 1 = 0110
0110 & 0001 = 0 → False

Time Complexity: O(1)
Space Complexity: O(1)
"""
