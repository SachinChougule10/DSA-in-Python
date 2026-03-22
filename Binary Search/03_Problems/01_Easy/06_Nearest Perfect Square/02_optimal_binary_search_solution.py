# GFG : Nearest Perfect Square
# Given an integer n, determine the nearest perfect square and compute the absolute difference between n and that perfect square (Optimal Solution)

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
        l = 0
        r = n
        root = 0  # will store floor value of sqrt(n)

        # Binary search to find floor(sqrt(n))
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            # If exact perfect square is found
            if square == n:
                return [square, 0]

            # If mid^2 is less than n, move right
            elif square < n:
                root = mid  # store possible sqrt
                l = mid + 1

            # If mid^2 is greater than n, move left
            else:
                r = mid - 1

        # After loop:
        # root = floor(sqrt(n))

        # Largest perfect square <= n
        lower_square = root * root

        # Smallest perfect square > n
        upper_square = (root + 1) * (root + 1)

        # Compare which square is closer to n
        # If equal distance, smaller square is preferred
        if abs(n - lower_square) < abs(n - upper_square):
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

Approach (Binary Search):

1. Use binary search in range [0, n] to find sqrt(n)
   - We are not using built-in sqrt function
   - Instead, we find the largest number 'root' such that:
        root^2 <= n

2. Binary Search Steps:
   - mid = (l + r) // 2
   - If mid^2 == n → exact perfect square → return immediately
   - If mid^2 < n → store mid as possible root and move right
   - If mid^2 > n → move left

3. After loop:
   - root = floor(sqrt(n))

4. Find two nearest perfect squares:
   - lower_square = root^2
   - upper_square = (root + 1)^2

5. Compare distances:
   - |n - lower_square|
   - |n - upper_square|

6. Return the closer one
   - If both are equal, return the smaller (lower_square)

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""
