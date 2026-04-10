# GFG : Single Number
# Given an array arr[] of positive integers where every element appears even times except for one (Optimal Solution)
# Find that number occurring an odd number of times.

# Examples:
# Input: arr[] = [1, 1, 2, 2, 2]
# Output: 2
# Explanation: In the given array all element appear two times except 2 which appears thrice.

# Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
# Output: 1
# Explanation: In the given array all element appear two times except 1 which appears once.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ arr.size() ≤ 106
# 0 ≤ arri ≤ 105


class Solution:
    def single_number(self, arr: list[int]) -> int:
        # Initialize result (XOR identity element)
        result = 0

        for num in arr:
            # XOR current number with result
            # even occurrences cancel out (a ^ a = 0)
            result = result ^ num  # ((((4 ^ 1) ^ 2) ^ 1) ^ 2)

        # Remaining number is the one with odd occurrences
        return result


arr = [1, 1, 2, 2, 2]

obj = Solution()
print(obj.single_number(arr))  # Output : 2

"""
Logic: Optimal XOR Approach (Odd Occurrences)

Basic XOR Rules:
- a ^ a = 0
- a ^ 0 = a

XOR Properties:
1. Commutative:
   a ^ b = b ^ a

2. Associative:
   (a ^ b) ^ c = a ^ (b ^ c)

Key Observations:
- Elements appearing even number of times cancel out → a ^ a = 0
- Only the element with odd occurrences remains

Why this works:
- XOR of all elements = (pairs cancel) + (odd occurring element)
- Since all even occurrences vanish, only the odd one stays

Example:
arr = [1, 1, 2, 2, 2]

Step-by-step:
result = 0
result ^ 1 = 1
result ^ 1 = 0
result ^ 2 = 2
result ^ 2 = 0
result ^ 2 = 2

Final Answer = 2


Another Example:
arr = [8, 8, 7, 7, 6, 6, 1]

All pairs cancel:
(8 ^ 8) ^ (7 ^ 7) ^ (6 ^ 6) ^ 1
= 0 ^ 0 ^ 0 ^ 1
= 1


One-line intuition:
XOR removes even-frequency elements → only odd-frequency element remains


Time Complexity: O(n)
Space Complexity: O(1)
"""
