# Leetcode : 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer (Brute Force Solution)
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
        # Handle small edge cases directly
        if x < 2:
            return x

        i = 1  # Start checking from 1

        # Keep increasing i while i*i is within x
        while i * i <= x:
            i += 1

        # When loop stops, i*i > x
        # So the answer is previous value
        return i - 1


x = 8
obj = Solution()
print(obj.sqrt(x))  # Output : 2

"""
Approach: Brute Force (Simulation)

Logic:
- We iterate from i = 1 upwards.
- For each i, we check if i * i <= x.
- As long as this condition holds, we keep increasing i.
- The moment i * i becomes greater than x, we stop.
- Since i exceeded the valid value, the correct answer is (i - 1).

Example:
x = 8
i = 1 -> 1*1 = 1 <= 8
i = 2 -> 2*2 = 4 <= 8
i = 3 -> 3*3 = 9 > 8 (stop)
Return 2

Time Complexity: O(√x)
- Because i goes up to approximately √x

Space Complexity: O(1)
- No extra space used
"""
