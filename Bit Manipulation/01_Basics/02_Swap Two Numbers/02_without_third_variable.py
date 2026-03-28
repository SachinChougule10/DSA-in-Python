# Problem: Swap Two Numbers Using XOR (Without Temporary Variable)

# Description:
# This program swaps two integer values using the XOR (^) bitwise operator, without using any extra space (temporary variable).

# Example:
# Input: num1 = 5, num2 = 6
# Output: num1 = 6, num2 = 5

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def swap_using_temp(self, num1: int, num2: int):

        # Print original values
        print(f"old num1: {num1}")  # Output : 5
        print(f"old num2: {num2}")  # Output : 6

        # Step 1: XOR both numbers and store in num1
        # num1 now holds XOR of num1 and num2
        num1 = num1 ^ num2

        # Step 2: XOR new num1 with num2 to get original num1
        # num2 becomes original num1
        num2 = num1 ^ num2

        # Step 3: XOR new num1 with new num2 to get original num2
        # num1 becomes original num2
        num1 = num1 ^ num2

        print(f"new num1: {num1}")  # Output : 6
        print(f"new num2: {num2}")  # Output : 5


obj = Solution()
obj.swap_using_temp(5, 6)

"""
Logic: Swap Using XOR

Goal:
Swap two numbers without using a temporary variable.

Key Concept:
XOR (^) has special properties:
- a ^ a = 0
- a ^ 0 = a
- a ^ b ^ b = a

Steps:
Let num1 = a, num2 = b

Step 1: num1 = num1 ^ num2
        → num1 = a ^ b

Step 2: num2 = num1 ^ num2
        → num2 = (a ^ b) ^ b = a

Step 3: num1 = num1 ^ num2
        → num1 = (a ^ b) ^ a = b

Final Result:
num1 = b, num2 = a (values swapped)

Example:
a = 5 (101), b = 6 (110)

Step 1: a = 101 ^ 110 = 011
Step 2: b = 011 ^ 110 = 101 (5)
Step 3: a = 011 ^ 101 = 110 (6)

Time Complexity: O(1)
Space Complexity: O(1)
"""
