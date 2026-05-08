# LeetCode 171 : Excel Sheet Column Number. Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number (Optimal Solution)

# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


# Example 1:

# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

# Constraints:

# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].


class Solution:
    def title_to_number(self, columnTitle: str) -> int:
        # Total number of characters in the column title
        n = len(columnTitle)

        # Accumulator for the final column number
        result = 0

        for i in range(n):
            # Convert the current character to its 1-based positional value:
            # 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
            value = ord(columnTitle[i]) - ord("A") + 1

            # Treat the title like a base-26 number:
            # Shift the current result left by one "base-26 digit" and add the new digit
            result = (result * 26) + value

        return result


obj = Solution()

columnTitle1 = "A"
print(obj.title_to_number(columnTitle1))  # Output: 1

columnTitle2 = "AB"
print(obj.title_to_number(columnTitle2))  # Output: 28

columnTitle3 = "ZY"
print(obj.title_to_number(columnTitle3))  # Output: 701

"""
LOGIC & ALGORITHM EXPLANATION
==============================

Problem:
    Excel columns are labelled using an alphabetic system that is similar to
    base-26 positional notation, except there is no zero digit — 'A' acts as 1,
    not 0.  We must convert a column label string into its integer equivalent.

Core Insight — Base-26 with a 1-Offset:
    The Excel column system is essentially base-26 where:
        A = 1, B = 2, ..., Z = 26

    This is analogous to how decimal (base-10) positional values work:
        "AB" = A * 26^1  +  B * 26^0
             = 1  * 26   +  2 *  1
             = 26 + 2
             = 28

    General formula for a title of length n:
        result = sum( value(title[i]) * 26^(n-1-i) )  for i in 0..n-1

Algorithm — Horner's Method (Left-to-Right Accumulation):
    Instead of computing powers of 26 explicitly, we use Horner's method which
    processes digits left-to-right:

        result = 0
        for each character c in columnTitle:
            value  = position of c in alphabet  (A=1 … Z=26)
            result = result * 26 + value

    Trace for "AB":
        Start:       result = 0
        i=0, 'A':    value  = 1
                     result = 0 * 26 + 1 = 1
        i=1, 'B':    value  = 2
                     result = 1 * 26 + 2 = 28   ✓

    Trace for "ZY":
        Start:       result = 0
        i=0, 'Z':    value  = 26
                     result = 0  * 26 + 26 = 26
        i=1, 'Y':    value  = 25
                     result = 26 * 26 + 25 = 701  ✓

Complexity:
    Time  — O(n): single pass over the string of length n.
    Space — O(1): only two integer variables are maintained regardless of input size.

Key Functions Used:
    ord(char)  — returns the Unicode code point of a character.
                 ord('A') = 65, ord('B') = 66, …, ord('Z') = 90
    ord(c) - ord('A') + 1  — maps 'A'->1, 'B'->2, …, 'Z'->26
"""
