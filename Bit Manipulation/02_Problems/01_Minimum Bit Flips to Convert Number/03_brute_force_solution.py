# Leetcode : 2220. Minimum Bit Flips to Convert Number (Brute Force Solution)
# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
# For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

# Example 1:
# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

# Example 2:
# Input: start = 3, goal = 4
# Output: 3
# Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
# - Flip the first bit from the right: 011 -> 010.
# - Flip the second bit from the right: 010 -> 000.
# - Flip the third bit from the right: 000 -> 100.
# It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

# Constraints:
# 0 <= start, goal <= 109


class Solution:
    def minimum_bit_flips(self, start, goal):
        # stores number of flips required
        count = 0

        # XOR gives 1 at positions where bits differ
        ans = start ^ goal

        # Traverse all bits until ans becomes 0
        while ans > 0:
            count += ans & 1  # Any number & 1 → gives last bit
            ans >>= 1  # Right shift → removes last bit

        return count


obj = Solution()
print(obj.minimum_bit_flips(10, 7))  # Output : 3

"""
Problem: Minimum Bit Flips to Convert Number

Logic:
- To convert 'start' into 'goal', we need to flip bits where they differ.
- XOR (^) helps identify these positions:
    - 1 → bits are different (flip needed)
    - 0 → bits are same

- Therefore, number of flips = number of set bits (1s) in (start ^ goal)

Approach:
1. Compute XOR:
   ans = start ^ goal

2. Count set bits using bitwise operations:
   - Extract last bit using (ans & 1)
   - Add it to count
   - Right shift using (ans >>= 1) to move to next bit

3. Repeat until ans becomes 0

Example:
start = 10 (1010)
goal  = 7  (0111)

XOR result = 1101 → 3 set bits → 3 flips required

Time Complexity:
- O(log n) → number of bits in the integer

Space Complexity:
- O(1)

Note:
- This is a brute force bit counting approach using bitwise operations.
- More efficient than division-based method (no costly division).
- Can be further optimized using:
  Brian Kernighan’s Algorithm → O(number of set bits)
"""
