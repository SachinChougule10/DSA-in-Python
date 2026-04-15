# GFG : Find XOR of numbers from L to R (Optimal Solution)
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
    def xor_till_n(self, n: int):
        # XOR from 1 to n follows a repeating pattern of 4

        if n % 4 == 1:
            return 1  # Pattern result when remainder is 1

        elif n % 4 == 2:
            return n + 1  # Pattern result when remainder is 2

        elif n % 4 == 3:
            return 0  # Pattern result when remainder is 3

        elif n % 4 == 0:  # OR else: return n
            return n  # Pattern result when remainder is 0

    def xor_in_range(self, l: int, r: int) -> int:
        # XOR(L → R) = XOR(1 → R) ^ XOR(1 → L-1)
        return self.xor_till_n(l - 1) ^ self.xor_till_n(r)


obj = Solution()

l1 = 4
r1 = 8
print(obj.xor_in_range(l1, r1))  # Output: 8

l2 = 1
r2 = 3
print(obj.xor_in_range(l2, r2))  # Output: 0

"""
LOGIC EXPLANATION (Optimal Approach):

Goal:
Find XOR of numbers from L to R in O(1) time.

Key Identity:
    XOR(L → R) = XOR(1 → R) ^ XOR(1 → L-1)

--------------------------------------------------

Why this works (Detailed Cancellation):

Example:
L = 4, R = 8

XOR(1 → R):
= 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8

XOR(1 → L-1):
= 1 ^ 2 ^ 3

Now XOR both:

(1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8)
^
(1 ^ 2 ^ 3)

Rearranging (since XOR is commutative):

= (1 ^ 1) ^ (2 ^ 2) ^ (3 ^ 3) ^ 4 ^ 5 ^ 6 ^ 7 ^ 8

Using XOR property:
a ^ a = 0

= 0 ^ 0 ^ 0 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8

Since 0 ^ x = x:

Final result:
= 4 ^ 5 ^ 6 ^ 7 ^ 8  → XOR(L → R)

--------------------------------------------------

Key Insight:
- Numbers from 1 to (L-1) appear twice → they cancel out
- Only numbers from L to R remain

--------------------------------------------------

How XOR(1 → N) is computed:

n % 4 == 0 → n
n % 4 == 1 → 1
n % 4 == 2 → n + 1
n % 4 == 3 → 0

--------------------------------------------------

Steps:
1. Compute XOR(1 → R)
2. Compute XOR(1 → L-1)
3. XOR both results

--------------------------------------------------

Time Complexity: O(1)
Space Complexity: O(1)

This is the optimal approach used in range XOR problems.
"""
