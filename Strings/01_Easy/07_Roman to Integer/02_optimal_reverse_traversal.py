# Leetcode : 13. Roman to Integer - Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

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

        # Mapping Roman symbols to their integer values
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        previous = 0  # Stores value of previous numeral (from right side)
        total = 0  # Stores final integer result

        # Traverse the string in reverse (right → left)
        for ch in reversed(s):
            # Get integer value of current symbol
            curr = roman_map[ch]

            # If current value is less than previous value, it means we encountered a subtractive case
            # Example: IV → when processing I after V → subtract 1
            if curr < previous:
                total -= curr
            else:
                total += curr

            # Update previous for next iteration
            previous = curr

        return total


obj = Solution()
s = "MCMXCIV"
print(obj.roman_to_int(s))  # Output: 1994

s1 = "III"
print(obj.roman_to_int(s1))  # Output: 3

"""
Logic :

1. Roman numerals follow addition and subtraction rules.

2. Normally, symbols are written from largest to smallest (left to right).

3. If a smaller value appears before a larger value, it should be subtracted.
   Examples:
   IV  → 5 - 1 = 4
   IX  → 10 - 1 = 9
   CM  → 1000 - 100 = 900

4. Approach Used:
   - Create a hashmap to store Roman symbol → integer value.
   - Traverse the string from right to left.
   - Keep track of the previous numeral value.
   - If current value < previous value → subtract.
   - Otherwise → add.

5. Why reverse traversal works:
   Subtraction depends on the next larger value.
   By traversing from right to left, we already know whether to subtract or add based on the previous value.

Time Complexity (TC):
O(n)
We traverse the string once, where n is the length of the Roman numeral.

Space Complexity (SC):
O(1)
We use a fixed-size hashmap of 7 Roman symbols and a few variables.
No extra space grows with input size.
"""
