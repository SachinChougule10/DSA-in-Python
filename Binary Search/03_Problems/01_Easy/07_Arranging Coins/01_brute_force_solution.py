# 441. Arranging Coins : You have n coins and you want to build a staircase with these coins (Brute Force Solution)
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
        # Start from first row
        curr_row = 1

        # To count how many complete rows we can build
        total_rows = 0

        # Keep forming rows while we have enough coins
        while n >= curr_row:
            # Use coins to fill current row
            n = n - curr_row

            # One complete row formed
            total_rows += 1

            # Move to next row (needs more coins)
            curr_row += 1

        # Return total complete rows formed
        return total_rows


obj = Solution()

n1 = 5
print(obj.arrangeCoins(n1))  # Output : 2

n2 = 8
print(obj.arrangeCoins(n2))  # Output : 3

"""
LOGIC EXPLANATION:

We are given 'n' coins and need to build a staircase such that:
- 1st row has 1 coin
- 2nd row has 2 coins
- 3rd row has 3 coins
- ...
- kth row has k coins

We must return the number of COMPLETE rows.

----------------------------------------
BRUTE FORCE IDEA:

We simulate the process row by row:

1. Start with row = 1
2. Check if we have enough coins to fill this row
3. If yes:
   - Deduct those coins from n
   - Increase completed row count
   - Move to next row
4. Stop when we cannot fill the next row

----------------------------------------
DRY RUN:

Example: n = 5

Row 1 → need 1 → remaining = 4
Row 2 → need 2 → remaining = 2
Row 3 → need 3 → NOT possible

Answer = 2 rows

----------------------------------------
TIME COMPLEXITY:

O(k), where k is number of rows formed
In worst case: k ≈ √(2n)

WHY TIME COMPLEXITY IS O(√n)?

Sum of first k numbers:
k(k + 1) / 2 ≈ n

Approx:
k² ≈ 2n  →  k ≈ √(2n)

So loop runs about √n times, not n.

----------------------------------------
SPACE COMPLEXITY:

O(1) (constant space)

----------------------------------------
NOTE:
This is the brute force solution.
Optimal solution uses Binary Search or Mathematical Formula.
"""
