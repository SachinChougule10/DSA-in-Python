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

        # XOR gives bits where start and goal differ
        ans = start ^ goal

        # Process each bit using division (right shift equivalent)
        while ans > 0:
            # Check last bit (LSB)
            if ans % 2 == 1:
                count += 1  # increment if bit is 1

            # Right shift by dividing by 2
            ans //= 2

        return count

    # ans //= 2 → same as ans >> 1
    # ans % 2 → same as ans & 1


obj = Solution()
print(obj.minimum_bit_flips(10, 7))  # Output : 3

"""
Logic:
- We need to count how many bits differ between 'start' and 'goal'.
- Each differing bit represents one flip operation.

Approach:
1. Compute XOR of start and goal:
   - XOR results in 1 where bits differ.
   - So, XOR output directly tells us which bits need flipping.

2. Count set bits (1s) in the XOR result:
   - Each set bit = one required flip.

3. Use division-based method:
   - Check last bit using (ans % 2)
   - If it is 1 → increment count
   - Remove last bit using integer division (ans //= 2)

Example:
start = 10 (1010)
goal  = 7  (0111)

XOR result = 1101 → 3 set bits → 3 flips required

Time Complexity:
- O(log n) → number of bits in the number

Space Complexity:
- O(1)

Note:
- This approach mimics right shift using division.
- Can be further optimized using:
  Brian Kernighan’s Algorithm → O(number of set bits)
"""
