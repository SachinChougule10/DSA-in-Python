# Leetcode : 191. Number of 1 Bits (Optimal Solution)
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3

# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1

# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30

# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.


# Constraints:
# 1 <= n <= 231 - 1

# Follow up: If this function is called many times, how would you optimize it?


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize count of set bits
        count = 0

        # Loop runs until n becomes 0
        while n:
            # Remove the lowest set bit from n
            n = n & (n - 1)

            # Increment count for each removed set bit
            count += 1

        # Return total number of set bits
        return count


obj = Solution()

n1 = 11
print(obj.hammingWeight(n1))  # Output: 3

n2 = 128
print(obj.hammingWeight(n2))  # Output: 1

n3 = 2147483645
print(obj.hammingWeight(n3))  # Output: 30

"""
LOGIC EXPLANATION:

This solution uses an optimal bit manipulation trick:

Key Idea:
The expression (n & (n - 1)) removes the **rightmost set bit (1)** from a number.

-----------------------------------------------------

Example:
n = 11 → binary: 1011

Iteration 1:
n = 1011
n-1 = 1010
n & (n-1) = 1010  (removed one '1')

Iteration 2:
n = 1010
n-1 = 1001
n & (n-1) = 1000  (removed another '1')

Iteration 3:
n = 1000
n-1 = 0111
n & (n-1) = 0000  (removed last '1')

Total iterations = 3 → number of set bits

-----------------------------------------------------

Why this is optimal?
Instead of checking all 32 bits, we only loop through the number of set bits.

Time Complexity:
O(k) → where k = number of set bits

Worst case: O(32) → when all bits are 1
Best case: O(1) → when only one bit is set

Space Complexity:
O(1)
"""
