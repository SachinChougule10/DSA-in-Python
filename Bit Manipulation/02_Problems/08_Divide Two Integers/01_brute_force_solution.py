# Leetcode : 29. Divide Two Integers : Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator (Brute Force Solution)
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2³¹, 2³¹ - 1].
# For this problem, if the quotient is strictly greater than 2³¹ - 1, then return 2³¹ - 1, and if the quotient is strictly less than -2³¹, then return -2³¹.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.

# Constraints:
# -2³¹ <= dividend, divisor <= 2³¹ - 1
# divisor != 0


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle sign of result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)

        #  This will store the quotient
        count = 0
        total = divisor

        # Keep subtracting divisor from dividend
        while dividend >= divisor:
            dividend -= divisor  # Reduce dividend
            count += 1  # Increment quotient

        return sign * count  # Apply sign to result


obj = Solution()

dividend = 10
divisor = 3

print(obj.divide(dividend, divisor))

"""BRUTE FORCE LOGIC:

Goal:
Perform division without using *, /, %

Idea:
Division is repeated subtraction.

Steps:
1. Convert both dividend and divisor to positive numbers.
2. Repeatedly subtract divisor from dividend.
3. Count how many times subtraction is possible.
4. That count is the quotient.
5. Apply the correct sign at the end.

--------------------------------------------------

Example:
dividend = 10, divisor = 3

10 - 3 = 7   (count = 1)
7 - 3 = 4    (count = 2)
4 - 3 = 1    (count = 3)
1 < 3 → stop

Result = 3

--------------------------------------------------

Handling Negative Numbers:
- If signs are different → result is negative
- If signs are same → result is positive

--------------------------------------------------

Time Complexity: O(dividend / divisor)
Space Complexity: O(1)

--------------------------------------------------

Limitation:
- Very slow for large numbers (TLE for big inputs)
- Does not meet optimal constraints

This is why we later optimize using bit manipulation."""
