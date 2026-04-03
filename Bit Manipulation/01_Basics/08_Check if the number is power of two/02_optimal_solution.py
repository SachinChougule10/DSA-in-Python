# Problem: Check if a Number is a Power of Two (Optimal - Bit Manipulation)

# Description:
# This program checks whether a given integer is a power of 2 using bitwise operations.
# A number is a power of 2 if it has exactly one set bit (1) in its binary representation.

# Approach:
# - Use the property: n & (n - 1) removes the lowest set bit
# - If a number has only one set bit, the result becomes 0
# - Also ensure n > 0 to handle edge cases like n = 0

# Example:
# Input: n = 16 → Output: True
# Input: n = 25 → Output: False

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def is_power_of_two(self, n: int):
        # Check if n is positive and has only one set bit
        if n > 0 and n & (n - 1) == 0:
            return True

        return False


obj = Solution()
print(obj.is_power_of_two(16))  # Output : True
print(obj.is_power_of_two(25))  # Output : False


"""
Logic Explanation:

1. Key Property:
   - A power of 2 has exactly one set bit in binary.
     Example:
     1  → 0001
     2  → 0010
     4  → 0100
     8  → 1000

2. Trick Used:
   - Expression: n & (n - 1)
   - This operation removes the lowest set bit from n.

   Example:
   n = 8  → 1000
   n - 1 = 7 → 0111

   n & (n - 1) = 0000

3. Observation:
   - If n has only one set bit → result becomes 0
   - If n has more than one set bit → result is non-zero

4. Edge Case:
   - n = 0:
     0 & (-1) = 0 → would incorrectly return True
   - But 0 is NOT a power of 2 (it has no set bits)

5. Fix:
   - Add condition: n > 0

6. Final Condition:
   - n > 0 and (n & (n - 1)) == 0

Key Insight:
This is the most efficient way to check for power of 2 using bit manipulation,
as it runs in constant time.
"""
