# Leetcode : 367. Valid Perfect Square : Given a positive integer num, return true if num is a perfect square or false otherwise (Brute Force Solution)
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

# Example 1:
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

# Example 2:
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

# Constraints:
# 1 <= num <= 231 - 1


class Solution:
    def is_perfect_square(self, num: int) -> bool:

        # Try all possible numbers from 1 to num
        for i in range(1, num + 1):
            square = i * i

            # If match found
            if square == num:
                return True

            # If square exceeds num → no need to continue
            if square > num:
                break

        return False


obj = Solution()

num1 = 16
print(obj.is_perfect_square(num1))  # Output : True

num2 = 14
print(obj.is_perfect_square(num2))  # Output : False

"""
Logic (Brute Force):

- Iterate i from 1 to num
- For each i:
    - Compute i * i
    - If i*i == num → return True
    - If i*i > num → stop early (no need to check further)

Time Complexity: O(n) → worst case
(Optimized brute force becomes ~O(√n) due to early break)

Space Complexity: O(1)

Why it's inefficient:
- We check many unnecessary values.
- Binary Search reduces this to O(log n).
"""
