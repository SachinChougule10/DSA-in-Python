# Leetcode : 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer (Optimal Solution)
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
        l = 0
        r = x
        result = 0  # Stores the last valid value where mid*mid <= x

        # Perform binary search in the range [0, x]
        while l <= r:
            mid = (l + r) // 2  # Find middle element

            # Check if mid is exact square root
            if mid * mid == x:
                return mid

            # If mid^2 is less than x, mid can be a possible answer
            elif mid * mid < x:
                result = mid  # Store current valid result
                l = mid + 1  # Try to find a larger value on the right

            else:
                r = mid - 1  # Search in the left half

        # When loop ends, result holds floor(sqrt(x))
        return result


x = 8
obj = Solution()
print(obj.sqrt(x))  # Output : 2

"""
Approach: Binary Search (Optimal)

Logic:
- We need to find the largest integer k such that k*k <= x.
- The search space is from 0 to x.
- Since k*k increases as k increases (monotonic), we can apply binary search.

Steps:
1. Initialize l = 0 and r = x.
2. Compute mid = (l + r) // 2.
3. Compare mid*mid with x:
   - If mid*mid == x → exact square root found, return mid.
   - If mid*mid < x → mid is valid, store it and search right for a bigger value.
   - If mid*mid > x → mid is too large, search left.
4. Continue until l > r.
5. Return the last stored valid value (result).

Example:
x = 8
mid = 4 → 16 > 8 → move left
mid = 1 → 1 < 8 → store 1 → move right
mid = 2 → 4 < 8 → store 2 → move right
mid = 3 → 9 > 8 → move left → stop

Return 2

Time Complexity: O(log x)
- Binary search halves the search space each time

Space Complexity: O(1)
- No extra space used

Why Binary Search?
- The function k^2 increases as k increases
- This monotonic behavior allows efficient searching
"""
