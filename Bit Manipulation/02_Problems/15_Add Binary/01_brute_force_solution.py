# LeetCode : 67. Add Binary (Brute Force Solution)
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        num1 = int(a, 2)
        num2 = int(b, 2)

        # Add integers
        total = num1 + num2

        # Convert result back to binary string
        return bin(total)[2:]


obj = Solution()

a1 = "11"
b1 = "1"
print(obj.add_binary(a1, b1))  # Output : 100

a2 = "1010"
b2 = "1011"
print(obj.add_binary(a2, b2))  # Output : 10101

"""
LOGIC (Brute Force):

1. Convert both binary strings into integers using base 2.
2. Add the two integers.
3. Convert the result back to a binary string using bin().
4. Remove '0b' prefix from the result.

Time Complexity: O(n)
Space Complexity: O(n)

Note:
- This method is simple but not optimal for very large inputs.
"""
