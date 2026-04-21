# GFG : First Set Bit (Optimal Solution)
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
        # If number is 0 → no set bits
        if n == 0:
            return 0

        # Step 1: isolate rightmost set bit
        # Example: n = 18 (10010)
        # rightmost = 00010
        rightmost = n & -n

        # Step 2: find position of this bit (1-based index)
        pos = 1

        # Keep shifting right until we reach 1
        while rightmost > 1:
            rightmost >>= 1  # shift right
            pos += 1  # increase position

        return pos


obj = Solution()

n1 = 18
print(obj.get_first_set_bit(n1))  # Output : 2

n2 = 12
print(obj.get_first_set_bit(n2))  # Output : 3

n3 = 1
print(obj.get_first_set_bit(n3))  # Output : 1

"""
Logic:

1. If n == 0 → return 0

2. Extract rightmost set bit:
   rightmost = n & -n

3. This gives a power of 2 (only one bit set)

4. Count how many shifts needed to make it 1:
   - Start pos = 1
   - Right shift until rightmost == 1
   - Increment pos each time

5. Return pos

Time Complexity: O(log n)
Space Complexity: O(1)
"""
