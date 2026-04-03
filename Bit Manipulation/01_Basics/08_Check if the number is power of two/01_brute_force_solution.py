# Problem: Check if a Number is a Power of Two (Brute Force)

# Description:
# This program determines whether a given integer is a power of 2.
# A number is considered a power of 2 if it can be repeatedly divided by 2
# until the result becomes exactly 1.

# Approach:
# - If the number is less than or equal to 0, return False (invalid case)
# - Continuously divide the number by 2 while it is even
# - After the loop, check if the result is 1
#   → If yes, it's a power of 2
#   → Otherwise, it's not

# Example:
# Input: n = 16 → Output: True
# Input: n = 25 → Output: False

# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def is_power_of_two(self, n: int):
        # Edge case: powers of 2 are always positive
        if n <= 0:
            return False

        # Keep dividing n by 2 while it is even
        while n % 2 == 0:
            n = n // 2  # Reduce n

        # If n becomes 1, it is a power of 2
        return n == 1


obj = Solution()
print(obj.is_power_of_two(16))  # Output : True
print(obj.is_power_of_two(25))  # Output : False

"""
Logic Explanation:

1. A power of 2 number can be written as:
   2^k (where k ≥ 0)

2. Such numbers are always divisible by 2 until they reduce to 1.
   Example:
   16 → 8 → 4 → 2 → 1

3. The loop runs only while the number is divisible by 2.
   - If at any point the number is not divisible by 2 (like 25),
     the loop stops early.

4. Final Check:
   - If the number becomes 1 → True (power of 2)
   - Otherwise → False

5. Why we check n <= 0:
   - 0 and negative numbers are not powers of 2
   - They do not follow the form 2^k

Key Insight:
Only numbers that can be reduced to exactly 1 by dividing by 2 repeatedly
are powers of 2.
"""
