# 441. Arranging Coins : You have n coins and you want to build a staircase with these coins (Optimal Solution)
# The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Example 2:
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.

# Constraints:
# 1 <= n <= 231 - 1


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Search space: possible number of rows (1 to n)
        left = 1
        right = n

        # To store the last valid answer
        result = 0

        while left <= right:
            # Find mid (candidate number of rows)
            mid = (left + right) // 2

            # Total coins needed to build 'mid' rows
            coins = (mid * (mid + 1)) // 2

            if coins > n:
                # Too many coins needed → reduce rows
                right = mid - 1
            else:
                # Valid case → store answer
                result = mid

                # Try to find a larger valid number of rows
                left = mid + 1

        return result


obj = Solution()

n1 = 5
print(obj.arrangeCoins(n1))  # Output : 2

n2 = 8
print(obj.arrangeCoins(n2))  # Output : 3

"""
LOGIC EXPLANATION:

We need to find the maximum k such that:
1 + 2 + 3 + ... + k ≤ n

Instead of subtracting coins (brute force), we use Binary Search:

- We "guess" a value mid (number of rows)
- Compute coins needed: mid(mid + 1) / 2
- If coins > n → mid is too large
- If coins ≤ n → valid, try bigger value

We store the last valid mid as result.

----------------------------------------
WHY WE DON'T UPDATE n?

We are not simulating the process.
We are checking:
"How many coins are needed for mid rows?"

n stays constant (it's the limit), and we adjust mid.

----------------------------------------
TIME COMPLEXITY:

Binary Search → O(log n)

----------------------------------------
SPACE COMPLEXITY:

O(1)
"""
