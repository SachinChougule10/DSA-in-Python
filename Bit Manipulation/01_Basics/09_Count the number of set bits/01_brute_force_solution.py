# Problem: Count Number of Set Bits (Brute Force Solution)

# Description:
# Given an integer n, return the number of set bits (1s) present in its binary representation.

# Approach:
# - Repeatedly divide the number by 2
# - Check remainder (n % 2)
# - If remainder is 1 → increment count
# - Continue until n becomes 0

# Example:
# Input: 13  → Binary: 1101
# Output: 3


class Solution:
    def no_of_set_bits(self, n: int):
        count = 0  # Initialize counter to store number of 1s

        # Loop until n becomes 0
        while n > 0:
            # Check if last bit is 1
            if n % 2 == 1:
                count += 1  # Increment count if bit is 1

            # Right shift number by 1 (divide by 2)
            n //= 2

        return count  # Return total count of set bits


obj = Solution()
print(obj.no_of_set_bits(13))  # Output : 3

"""
------------------------------------------------------------
Logic Explanation (Docstring):

1. Any number can be represented in binary form.
   Example:
   13 → 1101

2. To count set bits:
   - We repeatedly extract the last bit using (n % 2)
   - If it's 1 → increment count

3. Then remove the last bit:
   - Do integer division (n //= 2)

4. Continue until n becomes 0

Step-by-step for n = 13:
    n = 13 → 1101 → last bit = 1 → count = 1
    n = 6  → 0110 → last bit = 0 → count = 1
    n = 3  → 0011 → last bit = 1 → count = 2
    n = 1  → 0001 → last bit = 1 → count = 3
    n = 0 → stop

Final Answer = 3

Time Complexity: O(log n)
Space Complexity: O(1)
------------------------------------------------------------
"""
