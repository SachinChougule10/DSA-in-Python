# Leetcode : 12. Integer to Roman : Seven different symbols represent Roman numerals with the following values:

# Symbol	Value
# I	          1
# V	          5
# X	          10
# L	          50
# C	          100
# D	          500
# M	          1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX.
# Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10.
# You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form. Given an integer, convert it to a Roman numeral.

# Example 1:
# Input: num = 3749
# Output: "MMMDCCXLIX"

# Explanation:
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

# Constraints: 1 <= num <= 3999


class Solution:
    def intToRoman(self, num: int) -> str:

        # Value-symbol pairs including subtractive cases. Stored in ascending order (we will traverse in reverse)
        value_symbol_pair = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M"),
        ]

        result = ""  # Final Roman numeral string

        # Traverse from largest value to smallest
        for value, symbol in reversed(value_symbol_pair):
            # Check if current value fits into num
            if num // value:
                # Determine how many times the value fits
                count = num // value
                # Append the symbol 'count' times
                result += count * symbol
                # Reduce num by removing the processed Roman value
                num = num % value

        return result


obj = Solution()

num1 = 3749
print(obj.intToRoman(num1))  # output : MMMDCCXLIX

num2 = 58
print(obj.intToRoman(num2))  # output : LVIII

"""
Logic Explanation:

1. Roman numerals are constructed from largest value to smallest value.

2. We maintain a list of (value, symbol) pairs including subtractive cases like:
   4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), 900 (CM).

3. We iterate from the largest value to the smallest using reversed().

4. For each value:
   - We compute how many times it fits into num using:
         count = num // value
   - We append the symbol count times.
   - Then we reduce num using modulus:
         num = num % value

5. Why is "while" not needed here?

   In the previous approach, we used:

       while num >= value

   because we were subtracting one value at a time.

   In this approach, integer division already calculates
   how many times the value fits.

   So instead of repeated subtraction, we handle
   repetition mathematically in one step.

   Division version = compressed form of while loop.

------------------------------------------------------------

Example: num = 58

58 // 50 = 1  → add "L"
num = 58 % 50 = 8

8 // 5 = 1 → add "V"
num = 8 % 5 = 3

3 // 1 = 3 → add "III"
num = 0

Final Result: LVIII

------------------------------------------------------------

Time Complexity (TC): O(1)
- Only 13 fixed value-symbol pairs.
- Maximum input is 3999.
- Total operations are bounded.

Space Complexity (SC): O(1)
- Constant extra space.
- Output size is bounded.
"""
