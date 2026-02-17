# Leetcode : 13. Roman to Integer - Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. (Forward Traversal Solution)

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def roman_to_int(self, s: str) -> int:

        # Dictionary mapping Roman symbols to their integer values
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        n = len(s)  # Length of input string
        total = 0  # Final result

        # Traverse the string from left to right
        for i in range(n):
            # Check for subtraction case:
            # If current value is less than next value, we subtract it instead of adding.
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add the current value
                total += roman_map[s[i]]

        return total


obj = Solution()
s = "MCMXCIV"
print(obj.roman_to_int(s))  # Output: 1994

s1 = "III"
print(obj.roman_to_int(s1))  # Output: 3


"""
Logic:

Roman numerals are usually written from largest to smallest (left to right). So normally, we just keep adding values.
But in some cases, a smaller value appears before a larger value.That means we subtract instead of add.

Example:
---------
IV = 4
I (1) comes before V (5)
So instead of 1 + 5, we do 5 - 1

How we detect subtraction?
----------------------------
If current value < next value:
    subtract current value
Else:
    add current value

Why this works?
----------------
When a smaller number appears before a larger one, we subtract it because it was already added conceptually, and this adjusts the value correctly.

Time Complexity:
----------------
O(n)  → We traverse the string once.

Space Complexity:
------------------
O(1)  → Only constant extra space (dictionary of fixed size).
"""
