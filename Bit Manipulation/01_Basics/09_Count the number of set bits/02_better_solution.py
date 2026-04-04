# Problem: Count Number of Set Bits (Bit Manipulation Approach)

# Description:
# Given an integer n, return the number of set bits (1s) in its binary representation using bit manipulation.

# Approach:
# - Use bitwise AND (n & 1) to check the last bit
# - Right shift the number (n >> 1) to process next bit
# - Repeat until n becomes 0

# Example:
# Input: 13  → Binary: 1101
# Output: 3


class Solution:
    def no_of_set_bits(self, n: int):
        count = 0  # Stores number of set bits

        # Loop until all bits are processed
        while n > 0:
            # Check last bit using AND operation
            # (n & 1) gives 1 if last bit is 1, else 0
            count += n & 1  # equivalent to n % 2

            # Right shift to remove the last bit
            # Equivalent to integer division by 2
            n = n >> 1  # equivalent to n // 2

        return count  # Return total count of set bits


obj = Solution()
print(obj.no_of_set_bits(13))  # Output : 3

"""
Logic Explanation:

1. Binary Representation:
   Any number can be represented in binary form.
   Example:
   13 → 1101

2. Core Idea:
   - Use (n & 1) to extract the last bit:
       • 1 → bit is set (odd number)
       • 0 → bit is not set (even number)
   - Add this directly to count

3. Remove Last Bit:
   - Right shift the number:
       n >> 1
   - This moves all bits one position to the right

4. Repeat until n becomes 0

Step-by-step for n = 13:
    n = 13 → 1101 → last bit = 1 → count = 1
    n = 6  → 0110 → last bit = 0 → count = 1
    n = 3  → 0011 → last bit = 1 → count = 2
    n = 1  → 0001 → last bit = 1 → count = 3
    n = 0 → stop

Final Answer = 3

Time Complexity: O(log n)
Space Complexity: O(1)

Advantages:
- Faster than division/modulo approach
- Uses efficient bitwise operations

Limitation:
- Still processes every bit (including 0s)
- Not the most optimal approach

Best Optimization:
- Use (n & (n - 1)) to remove the last set bit directly
"""
