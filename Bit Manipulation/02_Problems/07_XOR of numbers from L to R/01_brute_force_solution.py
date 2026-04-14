# GFG : Find XOR of numbers from L to R (Brute Force Solution)
# You are given two integers L and R, your task is to find the XOR of elements of the range [L, R]

# Example:
# Input:
# L = 4, R = 8
# Output:
# 8
# Explanation:
# 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8

# Your Task:
# Your task is to complete the function findXOR() which takes two integers l and r and returns the XOR of numbers from l to r.

# Expected Time Complexity: O(1).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1<=l<=r<=109


class Solution:
    def xor_in_range(self, l: int, r: int) -> int:
        # Initialize result
        XOR = 0

        # Traverse all numbers from l to r (inclusive)
        for i in range(l, r + 1):
            # Continuously XOR each number
            XOR = XOR ^ i

        # Final XOR of all numbers in range [l, r]
        return XOR


obj = Solution()

l1 = 4
r1 = 8
print(obj.xor_in_range(l1, r1))  # Output: 8

l2 = 1
r2 = 3
print(obj.xor_in_range(l2, r2))  # Output: 0

"""
LOGIC EXPLANATION (Brute Force):

- Initialize a variable XOR = 0.
- Iterate from l to r (inclusive).
- For each number i in this range, update:
      XOR = XOR ^ i
- After the loop completes, XOR contains:
      l ^ (l+1) ^ (l+2) ^ ... ^ r

Why it works:
- XOR operation combines all numbers sequentially.
- XOR is associative and commutative, so order does not matter.
- We simply accumulate the XOR of all values in the given range.

Example:
l = 4, r = 8
→ 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8

Time Complexity: O(r - l + 1)
Space Complexity: O(1)
"""
