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

        # Handle overflow case (only problematic case in 32-bit range)
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        # Determine sign of result using XOR
        # Result is negative if exactly one of dividend or divisor is negative
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert both numbers to positive for easy calculation
        dividend = abs(dividend)
        divisor = abs(divisor)

        # This will store the final quotient
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

print(obj.divide(dividend, divisor))  # Output : 3


"""
LOGIC EXPLANATION (Brute Force Approach):

Goal:
Divide two integers without using multiplication (*), division (/), or modulus (%).

--------------------------------------------------

CORE IDEA:
Division can be represented as repeated subtraction.

Instead of:
    dividend / divisor

We do:
    keep subtracting divisor from dividend
    and count how many times we can subtract

--------------------------------------------------

STEP-BY-STEP:

1. Handle Overflow Case:
   - If dividend = -2^31 and divisor = -1
   - Result becomes 2^31, which exceeds 32-bit range
   - So return 2^31 - 1 (INT_MAX)

--------------------------------------------------

2. Determine Sign:
   - Use XOR to check if signs are different
   - If exactly one is negative → result is negative
   - Else → result is positive

   sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

--------------------------------------------------

3. Convert to Positive:
   - Work with absolute values for easier subtraction
   - Sign will be applied at the end

--------------------------------------------------

4. Repeated Subtraction:
   - Keep subtracting divisor from dividend
   - Count how many times this happens
   - That count is the quotient

--------------------------------------------------

EXAMPLE:

dividend = 10, divisor = 3

10 - 3 = 7   (count = 1)
7 - 3 = 4    (count = 2)
4 - 3 = 1    (count = 3)
1 < 3 → stop

Result = 3

--------------------------------------------------

Handling Negative Case:

dividend = 7, divisor = -3

- Convert to positive → 7, 3
- Perform subtraction → count = 2
- Apply sign → result = -2

--------------------------------------------------

Time Complexity:
O(dividend / divisor) → very slow for large inputs

Space Complexity:
O(1)

--------------------------------------------------

LIMITATION:
- Not efficient for large numbers (can cause TLE)
- Optimized solution uses bit manipulation

--------------------------------------------------

KEY TAKEAWAY:
Division = repeated subtraction + sign handling
"""
