# Problem: Toggle i-th Bit (Bit Manipulation)

# Description:
# This program toggles (flips) the i-th bit (0-based index from right) of a given integer using bitwise XOR.

# If the bit is 0 → it becomes 1
# If the bit is 1 → it becomes 0

# Example:
# Input: n = 9 (1001), i = 2 → Output: 13 (1101)
# Input: n = 13 (1101), i = 2 → Output: 9 (1001)


class Solution:
    def toggle_ith_bit(self, n: int, i: int):
        # Create a mask with only the i-th bit set (1 shifted i times to the left)
        # Example: i = 2 → 1 << 2 = 4 → binary: 100
        return n ^ (1 << i)  # XOR flips the i-th bit (0→1 or 1→0)


obj = Solution()
print(obj.toggle_ith_bit(9, 2))  # Output : 13
print(obj.toggle_ith_bit(13, 2))  # Output : 9

"""
Logic Explanation:

1. Create a Mask:
   (1 << i) shifts 1 to the left by i positions.
   This creates a number where only the i-th bit is set.
   Example: i = 2 → 1 << 2 = 4 → binary: 100

2. Apply XOR Operation:
   XOR (^) is used to toggle bits.
   - If bit is 0 → 0 ^ 1 = 1 (bit becomes 1)
   - If bit is 1 → 1 ^ 1 = 0 (bit becomes 0)

3. Final Result:
   n ^ (1 << i) flips only the i-th bit of n, while keeping all other bits unchanged.

Time Complexity: O(1)
Space Complexity: O(1)
"""
