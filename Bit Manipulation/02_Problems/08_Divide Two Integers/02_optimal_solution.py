# Leetcode : 29. Divide Two Integers : Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator (Optimal Solution)
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

        # Edge case: overflow (only case where result exceeds INT_MAX)
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        # Quick check: if both are same → result is 1
        if dividend == divisor:
            return 1

        # Stores final quotient
        ans = 0

        # Determine sign of result
        sign = True  # True → positive, False → negative

        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = False

        # Work with absolute values
        n = abs(dividend)
        d = abs(divisor)

        # Main logic: subtract largest possible multiples of divisor
        while n >= d:
            count = 0

            # Find maximum power such that (d * 2^count) <= n
            while n >= d << (count + 1):  # OR while n >= (d * (2 ** (count + 1))):
                count += 1

            # Add corresponding multiple to answer
            ans += 1 << count  # OR ans += 2**count

            # Subtract that multiple from n
            n = n - (d << count)  # OR n = n - (d * (2**count))

        # 32-bit constraints
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Handle overflow (safety check)
        if ans >= 2**31:
            return INT_MIN if sign == False else INT_MAX

        # Apply sign
        return -ans if sign == False else ans


obj = Solution()

dividend = 10
divisor = 3

print(obj.divide(dividend, divisor))  # Output : 3


"""
Logic:

GOAL: Divide two numbers without using *, /, %
--------------------------------------------------

CORE IDEA:
Instead of subtracting divisor one by one (slow),
we subtract the largest possible multiples using powers of 2.

--------------------------------------------------

KEY INSIGHT:
d << k  = d * (2^k)

So instead of:
    n - d - d - d - d ...
We do:
    n - (d * 8), n - (d * 4), etc.

This speeds up the process.

--------------------------------------------------

STEP-BY-STEP EXAMPLE:

dividend = 10, divisor = 3

n = 10, d = 3

Step 1:
Find largest multiple of 3 using powers of 2

3 << 0 = 3
3 << 1 = 6
3 << 2 = 12 (too big)

So use:
3 << 1 = 6

Update:
n = 10 - 6 = 4
ans = 2   (because 2^1 = 2)

--------------------------------------------------

Step 2:

n = 4

3 << 0 = 3
3 << 1 = 6 (too big)

So use:
3 << 0 = 3

Update:
n = 4 - 3 = 1
ans = 2 + 1 = 3

--------------------------------------------------

Step 3:
n = 1 < 3 → stop

Final Answer = 3

--------------------------------------------------

WHY THIS IS FAST:

Instead of subtracting one by one:
→ We subtract in chunks (powers of 2)

Time Complexity:
O(log N * log N) ≈ O(log N)

Space Complexity:
O(1)

--------------------------------------------------

SIGN HANDLING:

- If signs differ → negative result
- Else → positive result

--------------------------------------------------

OVERFLOW CASE:

dividend = -2^31, divisor = -1

Result = 2^31 → exceeds INT_MAX

So we return:
INT_MAX = 2^31 - 1

--------------------------------------------------

KEY TAKEAWAYS:

1. Use bit shifting to simulate multiplication
2. Always subtract largest possible chunk
3. Handle sign separately
4. Watch out for overflow edge case

--------------------------------------------------

This is the standard optimal solution for LC 29.
"""

# Why overflow happens for -2^31 (32-bit signed integer):

# Range of 32-bit signed integer:
# -2^31 to 2^31 - 1
# = -2147483648 to 2147483647

# Observation:
# There is one extra negative number.
# Positive max = 2147483647
# Negative min = -2147483648

# Reason:
# Numbers are stored using Two’s Complement.
# With 32 bits:
# - 1 bit for sign
# - 31 bits for value

# Total values = 2^32
# Distribution:
# Positive side: 0 to 2^31 - 1
# Negative side: -1 to -2^31

# Problem case:
# dividend = -2^31 = -2147483648
# divisor  = -1

# Mathematically:
# -2147483648 / -1 = 2147483648

# Overflow:
# 2147483648 > 2147483647 (INT_MAX)
# So result cannot be stored in 32-bit integer.

# Additional issue:
# In C++/Java:
# abs(-2147483648) = 2147483648 (overflow)
# Because +2^31 is not representable.

# In Python:
# Works fine due to arbitrary precision integers,
# but problem requires 32-bit constraint handling.

# Fix:
# Handle this edge case before computation:

# if dividend == -2**31 and divisor == -1:
#     return 2**31 - 1

# Key takeaway:
# - -2^31 has no positive counterpart in 32-bit
# - Negating it causes overflow
# - This is the only division case that exceeds range
