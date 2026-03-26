#  l eetcode : 441. Arranging Coins : You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins (Optimal Solution)
# The last row of the staircase may be incomplete. Given the integer n, return the number of complete rows of the staircase you will build.

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

import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Apply quadratic formula to directly compute number of rows
        # Derived from: k(k + 1) / 2 = n
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)


obj = Solution()

n1 = 5
print(obj.arrangeCoins(n1))  # Output : 2

n2 = 8
print(obj.arrangeCoins(n2))  # Output : 3

"""
LOGIC EXPLANATION:

We need to find maximum k such that:
1 + 2 + 3 + ... + k ≤ n

----------------------------------------
HOW THE FORMULA IS DERIVED:

Sum of first k natural numbers:
k(k + 1) / 2 = n

Multiply both sides by 2:
k(k + 1) = 2n

Expand:
k² + k = 2n

Bring all terms to one side:
k² + k - 2n = 0

This is a quadratic equation of form:
ax² + bx + c = 0

Here:
a = 1, b = 1, c = -2n

Using quadratic formula:
k = (-b ± √(b² - 4ac)) / (2a)

Substitute values:
k = (-1 ± √(1 + 8n)) / 2

We take only the positive root:
k = (-1 + √(1 + 8n)) / 2

----------------------------------------
WHY int()?

The result may be a decimal value.
We take floor (int) because only complete rows are counted.

Example:
n = 8 → k ≈ 3.56 → answer = 3

----------------------------------------
TIME COMPLEXITY:

O(1)

----------------------------------------
SPACE COMPLEXITY:

O(1)
"""
