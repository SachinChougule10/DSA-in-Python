# GFG : Nearest Perfect Square
# Given an integer n, determine the nearest perfect square and compute the absolute difference between n and that perfect square (Brute Force Solution)

# Examples:
# Input: n = 25
# Output: [25, 0]
# Explanation: Since 25 is a perfect square, it is the closest perfect square to itself and absolute difference is 25 - 25 = 0

# Input: n = 86
# Output: [81, 5]
# Explanation:The closest perfect square to 86 is 81.Thus, the absolute difference between them is 86 - 81 = 5.

# Constraints:
# 1≤  n ≤ 109


class Solution:
    def square_difference(self, n):
        i = 1  # start checking from 1

        # Keep increasing i until i^2 becomes greater than or equal to n
        # This finds the first perfect square that is >= n
        while i * i < n:
            i += 1

        # Edge case: when n = 1
        # (i - 1)^2 becomes 0, so directly return 1 as nearest square
        if i == 1:
            return [1, n - 1]

        # Perfect square just greater than or equal to n
        upper_square = i * i

        # Perfect square just smaller than n
        lower_square = (i - 1) * (i - 1)

        # Compare which square is closer to n
        # If both are equal distance, we return the smaller one (lower_square)
        if abs(n - lower_square) <= abs(n - upper_square):
            return [lower_square, abs(n - lower_square)]
        else:
            return [upper_square, abs(n - upper_square)]


obj = Solution()

num1 = 25
print(obj.square_difference(num1))  # Output: [25, 0]

num2 = 86
print(obj.square_difference(num2))  # Output: [81, 5]

"""
LOGIC EXPLANATION

Goal:
Find the nearest perfect square to a number n and return:
[closest_perfect_square, absolute_difference]

Step 1: Start from i = 1
We increase i until i^2 becomes >= n.

This guarantees:
(i - 1)^2 < n <= i^2

Step 2: Identify two possible closest squares
lower_square = (i - 1)^2   -> just smaller than n
upper_square = i^2         -> just greater than or equal to n

Step 3: Compare which is closer
difference with lower = |n - lower_square|
difference with upper = |n - upper_square|

Step 4: Return the square with the smaller difference
If both are equally close, return the smaller square.

Edge Case:
When n = 1, the loop does not run and (i - 1)^2 becomes 0.
So we directly return [1, 0].

Time Complexity:
O(√n)

Space Complexity:
O(1)
"""
