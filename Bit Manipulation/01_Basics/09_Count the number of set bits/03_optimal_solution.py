# Problem: Count Number of Set Bits (Brian Kernighan’s Algorithm - Optimal Approach)

# Description:
# Given an integer n, return the number of set bits (1s) in its binary representation using an efficient method.

# Approach:
# - Use Brian Kernighan’s Algorithm
# - Repeatedly remove the rightmost set bit using:
#       n = n & (n - 1)
# - Count how many times this operation is performed

# Example:
# Input: 13  → Binary: 1101
# Output: 3


class Solution:
    def no_of_set_bits(self, n: int):
        count = 0  # Stores number of set bits

        # Loop runs only for number of set bits
        while n:
            # Remove the rightmost set bit
            n = n & (n - 1)
            # Increment count for each removed set bit
            count += 1

        return count  # Return total set bits


obj = Solution()
print(obj.no_of_set_bits(13))  # Output : 3

"""
Logic Explanation - Brian Kernighan’s Algorithm:

1. Key Insight:
   - Expression: n & (n - 1)
   - This removes the rightmost set bit (1) from n

2. Why it works:
   Example:
       n     = 1101
       n - 1 = 1100
       ----------------
       n & (n - 1) = 1100  (rightmost 1 removed)

3. Core Idea:
   - Each operation removes ONE set bit
   - So number of iterations = number of 1s

4. Dry Run (n = 13):
    n = 1101 → becomes 1100 → count = 1
    n = 1100 → becomes 1000 → count = 2
    n = 1000 → becomes 0000 → count = 3
    n = 0 → stop

Final Answer = 3

Time Complexity:
- O(k), where k = number of set bits

Space Complexity:
- O(1)

Advantages:
- Much faster than brute force
- Does NOT process zero bits

Comparison:
- Division / Bit shift → O(log n)
- Brian Kernighan → O(k) (optimal)

"""
