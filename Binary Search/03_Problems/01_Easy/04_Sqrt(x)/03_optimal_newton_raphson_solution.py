# Leetcode : 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer (Optimal Solution - Newton-Raphson Method)
# The returned integer should be non-negative as well. You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Constraints:
# 0 <= x <= 231 - 1


class Solution:
    def sqrt(self, x: int) -> int:
        # Edge case: square root of 0 is 0
        if x == 0:
            return 0

        # Initial guess (can be any positive number, x is simple choice)
        t = x

        while True:
            # Apply Newton formula to get better approximation
            root = 0.5 * (t + x / t)

            # If change is very small, we have reached desired precision
            if abs(root - t) < 1e-6:
                r = int(root)  # Convert to integer (truncate decimal part)

                # Safety check to avoid floating-point precision issues
                return r if r * r <= x else r - 1

            # Update guess for next iteration
            t = root


x = 8
obj = Solution()
print(obj.sqrt(x))  # Output: 2

"""
    Compute the integer square root of a non-negative integer x using Newton-Raphson Method.

    Logic:
    - We want to find √x → i.e., a number t such that t^2 = x
    - Convert it into a function: f(t) = t^2 - x
    - Apply Newton-Raphson method to iteratively improve guess:
        t_new = (t + x / t) / 2

    Steps:
    1. Start with an initial guess t = x
    2. Iteratively update t using Newton's formula
    3. Stop when the difference between consecutive values is very small (precision reached)
    4. Convert the result to integer (truncate decimal part)

    Why it works:
    - If t is too large → x/t becomes small → average reduces t
    - If t is too small → x/t becomes large → average increases t
    - This quickly converges to √x

    Time Complexity: O(log n) (very fast convergence)
    Space Complexity: O(1)

    Note:
    - We return integer part (floor of √x)
"""
