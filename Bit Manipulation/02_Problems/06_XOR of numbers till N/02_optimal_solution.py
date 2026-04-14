# XOR of Numbers in a Given Range
# Problem Statement: Given an integer N, find the XOR of all numbers from 1 to N.

# Input :  N = 5
# Output :  1
# Explanation :  The XOR of all numbers from 1 to 5 is: 1^2^3^4^5 = 1

# Input :  N = 10
# Output :  11
# Explanation :  The XOR of all numbers from 1 to 10 is: 1^2^3^4^5^6^7^8^9^10 = 11


class Solution:
    def xor_in_range(self, n: int) -> int:

        # XOR from 1 to n repeats in a cycle of 4

        # When n leaves remainder 1 → result is always 1
        if n % 4 == 1:
            return 1

        # When remainder is 2 → result becomes n + 1
        elif n % 4 == 2:
            return n + 1

        # When remainder is 3 → all values cancel out
        elif n % 4 == 3:
            return 0

        # When divisible by 4 → result equals n
        elif n % 4 == 0:  # OR else: return n
            return n


obj = Solution()

n1 = 5
print(obj.xor_in_range(n1))  # Output : 1

n2 = 10
print(obj.xor_in_range(n2))  # Output : 11

"""
LOGIC EXPLANATION (Optimized Approach):

Instead of computing XOR from 1 to n using a loop (O(n)),
we observe a repeating pattern in results:

n      XOR(1 → n)
-----------------
n % 4 == 0 → n
n % 4 == 1 → 1
n % 4 == 2 → n + 1
n % 4 == 3 → 0

Why this works:
- XOR has properties like:
  1. a ^ a = 0  (cancels out)
  2. a ^ 0 = a
- When we compute XOR sequentially, values cancel in a pattern.
- This pattern repeats every 4 numbers.

Example:
n = 5 → 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1
n = 10 → result = 11

Time Complexity: O(1)
Space Complexity: O(1)

This is the optimal approach and commonly used in:
- Range XOR problems
- Bit manipulation questions
- Missing number problems
"""
