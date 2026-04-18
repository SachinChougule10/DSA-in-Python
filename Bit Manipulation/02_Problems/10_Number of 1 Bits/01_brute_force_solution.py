# Leetcode : 191. Number of 1 Bits (Brute Force Solution)
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
        count = 0  # Initialize count of set bits

        # Traverse all bits until n becomes 0
        while n:
            # Check if last bit is 1
            if n & 1:
                count += 1

            # Right shift to check next bit
            n = n >> 1

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

This is the brute force approach where we check each bit individually.

Key Idea:
- Every number is made of bits (0s and 1s)
- We extract bits one by one using bit operations

-----------------------------------------------------

Steps:
1. Check the last bit using (n & 1)
   - If result is 1 → last bit is set → increment count
2. Right shift the number (n >> 1)
   - This removes the last bit
3. Repeat until n becomes 0

-----------------------------------------------------

Example:
n = 11 → binary: 1011

Iteration 1:
n = 1011 → last bit = 1 → count = 1
n = 0101

Iteration 2:
n = 0101 → last bit = 1 → count = 2
n = 0010

Iteration 3:
n = 0010 → last bit = 0 → count = 2
n = 0001

Iteration 4:
n = 0001 → last bit = 1 → count = 3
n = 0000 → stop

-----------------------------------------------------

Time Complexity:
O(32) → since integer has at most 32 bits

Space Complexity:
O(1)

-----------------------------------------------------

Difference from Optimal:
- Brute Force → checks all bits
- Optimal → runs only for number of set bits

Example:
n = 10000000
Brute force → 8 iterations
Optimal → 1 iteration

-----------------------------------------------------
"""
