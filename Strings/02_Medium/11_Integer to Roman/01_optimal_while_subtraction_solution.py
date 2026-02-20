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

        # List of (value, symbol) pairs in descending order
        # Includes subtractive cases like 900 (CM), 400 (CD), etc.
        value_symbol_pair = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = ""  # Final Roman numeral string

        # Iterate from largest value to smallest
        for value, symbol in value_symbol_pair:
            # Repeat adding the symbol as long as its value can be deducted from num
            # This ensures correct handling of repeating numerals like III, XXX, CCC, MMM
            while num >= value:
                result += symbol
                num -= value

        return result


obj = Solution()

num1 = 3749
print(obj.intToRoman(num1))  # output : MMMDCCXLIX

num2 = 58
print(obj.intToRoman(num2))  # output : LVIII

"""
Logic Explanation:

1. Roman numerals are formed from largest to smallest values.

2. We maintain a list of (value, symbol) pairs including subtractive cases:
   4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), 900 (CM).

3. We iterate through the list from largest to smallest value.

4. For each value:
   - While the current value is less than or equal to num:
       - Append the corresponding Roman symbol
       - Subtract the value from num

5. Why do we use "while" instead of "if"?

   Some Roman symbols can appear multiple times consecutively.

   Example:
   3000 = MMM
   30 = XXX
   3 = III

   If we used "if", the symbol would be added only once.
   But we need to add it as many times as it fits.
   Therefore, we use "while" to repeatedly subtract and append until the value no longer fits.

6. The loop continues until num becomes 0.

------------------------------------------------------------

Example: num = 58

50 -> L  (58 - 50 = 8)
5  -> V  (8 - 5 = 3)
1  -> III (3 - 1 - 1 - 1 = 0)

Result = LVIII

------------------------------------------------------------

Time Complexity (TC): O(1)
- The list contains only 13 fixed Roman values.
- Maximum input is 3999.
- Total operations are bounded by a constant.

Space Complexity (SC): O(1)
- We use a fixed list of 13 pairs.
- Output length is bounded (max Roman length is small).
"""
