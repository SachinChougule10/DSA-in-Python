# Leetcode : 367. Valid Perfect Square : Given a positive integer num, return true if num is a perfect square or false otherwise (Optimal Solution)
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
        l = 0
        r = num

        while l <= r:
            # Find middle element
            mid = (l + r) // 2

            # Square of mid
            square = mid * mid

            # If exact match → perfect square
            if square == num:
                return True

            # If square is smaller → move right
            elif square < num:
                l = mid + 1

            # If square is larger → move left
            else:
                r = mid - 1

        # If no integer square found
        return False


obj = Solution()

num1 = 16
print(obj.is_perfect_square(num1))  # Output : True

num2 = 14
print(obj.is_perfect_square(num2))  # Output : False


"""
Logic (Binary Search Approach):

- We are searching for an integer `mid` such that:
        mid * mid == num

- The search space is from 0 to num.

- Steps:
    1. Calculate mid = (l + r) // 2
    2. Compute square = mid * mid
    3. Compare:
        - If square == num → return True
        - If square < num → search right half (l = mid + 1)
        - If square > num → search left half (r = mid - 1)

- If loop ends without finding such `mid`, return False.

Time Complexity: O(log n)
    → Because we halve the search space each time.

Space Complexity: O(1)
    → No extra space used.

Why this works:
- Perfect square means an integer root exists.
- Binary search efficiently finds that root without using sqrt().
"""
