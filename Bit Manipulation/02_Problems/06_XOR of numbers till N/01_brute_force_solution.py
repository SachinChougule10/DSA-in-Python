# XOR of Numbers in a Given Range (Brute Force Solution)
# Problem Statement: Given an integer N, find the XOR of all numbers from 1 to N.

# Input :  N = 5
# Output :  1
# Explanation :  The XOR of all numbers from 1 to 5 is: 1^2^3^4^5 = 1

# Input :  N = 10
# Output :  11
# Explanation :  The XOR of all numbers from 1 to 10 is: 1^2^3^4^5^6^7^8^9^10 = 11


class Solution:
    def xor_in_range(self, n: int) -> int:
        # Initialize result
        XOR = 0

        # Iterate from 0 to n (0 doesn't affect XOR, so it's fine)
        for i in range(n + 1):
            # XOR current number with result
            XOR = XOR ^ i

        # Final XOR from 1 to n
        return XOR


obj = Solution()

n1 = 5
print(obj.xor_in_range(n1))  # Output: 1

n2 = 10
print(obj.xor_in_range(n2))  # Output: 11

"""
LOGIC (Brute Force):

- Initialize a variable XOR = 0.
- Traverse all numbers from 0 to n (or 1 to n).
- For each number i, update:
      XOR = XOR ^ i
- Keep accumulating the XOR value step by step.
- After the loop ends, XOR contains the result of:
      1 ^ 2 ^ 3 ^ ... ^ n

Why it works:
- XOR operation combines all numbers sequentially.
- Since XOR is associative and commutative, order does not matter.
- Starting from 0 is safe because 0 ^ x = x, so it does not affect the result.

Time Complexity: O(n)
Space Complexity: O(1)
"""
