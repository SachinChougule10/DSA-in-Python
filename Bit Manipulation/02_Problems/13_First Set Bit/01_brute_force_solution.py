# GFG : First Set Bit (Brute Force Solution)
# Given an integer n. You have to return the position of the first set bit  from the right side in the binary representation of the number.
# If there is no set bit in the integer N, then return 0 from the function.

# Examples:
# Input: n = 18
# Output: 2
# Explanation: Binary representation of 18 is 010010,the first set bit from the right side is at position 2.

# Input: n = 12
# Output: 3
# Explanation: Binary representation of  12 is 1100, the first set bit from the right side is at position 3.

# Input: n = 1
# Output: 1
# Explanation: Binary representation of  1 is 1, the first set bit from the right side is at position 1.
# Constraints:
# 1 ≤ n ≤ 109


class Solution:
    def get_first_set_bit(self, n):
        # position starts from 1 (1-based indexing)
        pos = 1

        # Loop until all bits are checked
        while n > 0:
            # Check if the last (rightmost) bit is 1
            if n & 1:
                return pos  # first set bit found

            # Shift bits to the right to check next bit
            n >>= 1

            # Move to next position
            pos += 1

        # If no set bit is found (n was 0)
        return 0


obj = Solution()

n1 = 18
print(obj.get_first_set_bit(n1))  # Output : 2

n2 = 12
print(obj.get_first_set_bit(n2))  # Output : 3

n3 = 1
print(obj.get_first_set_bit(n3))  # Output : 1

"""
Logic:

1. Initialize position counter pos = 1 (since indexing is 1-based)

2. Traverse bits of n from right to left:
   - Use (n & 1) to check if the last bit is 1
   - If yes → return current position

3. If last bit is 0:
   - Right shift n by 1 (n >>= 1) to remove last bit
   - Increment position

4. Repeat until n becomes 0

5. If no set bit is found → return 0

Time Complexity: O(log n)
  - We check each bit once

Space Complexity: O(1)
  - No extra space used
"""
