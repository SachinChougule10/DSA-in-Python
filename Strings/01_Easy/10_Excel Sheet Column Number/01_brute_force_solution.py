# LeetCode 171 : Excel Sheet Column Number. Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number (Brute Force Solution)

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


import string


class Solution:
    def title_to_number(self, columnTitle: str) -> int:

        # string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # index() gives 0-based position, so +1 makes it 1-based: A=1, B=2...Z=26
        alphabet = string.ascii_uppercase  # built-in ordered letter string

        result = 0
        n = len(columnTitle)

        # Iterate over each character with its index
        for i, char in enumerate(columnTitle):

            # Find 1-based value of character using index lookup
            char_value = alphabet.index(char) + 1  # 'A'->1, 'B'->2, ..., 'Z'->26

            # Positional power: leftmost letter gets the highest power
            # "AB" -> 'A' gets 26^1, 'B' gets 26^0
            power = n - i - 1

            # Use ** directly — simpler than a manual loop
            result += char_value * (26**power)

        return result


obj = Solution()

columnTitle1 = "A"
print(obj.title_to_number(columnTitle1))  # Output: 1

columnTitle2 = "AB"
print(obj.title_to_number(columnTitle2))  # Output: 28

columnTitle3 = "ZY"
print(obj.title_to_number(columnTitle3))  # Output: 701


"""
LOGIC EXPLANATION
=================

Core Idea:
    Same base-26 positional logic, but stripped down to bare essentials:
    - Use string.ascii_uppercase to avoid building a manual dictionary
    - Use ** operator to avoid the inner power-computation loop

Formula applied directly:
    result = sum( char_value * 26^power )   for each character

Trace for "AB" (n=2):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    i=0, char='A':  char_value = 0+1 = 1,  power = 1,  contribution = 1*26 = 26
    i=1, char='B':  char_value = 1+1 = 2,  power = 0,  contribution = 2* 1 =  2
                                                         result              = 28 ✓

Trace for "ZY" (n=2):
    i=0, char='Z':  char_value = 25+1 = 26, power = 1,  contribution = 26*26 = 676
    i=1, char='Y':  char_value = 24+1 = 25, power = 0,  contribution = 25* 1 =  25
                                                          result               = 701 ✓

3-Way Comparison:
    ┌──────────────────┬────────────────────┬────────────────────┬──────────────────┐
    │ Aspect           │ Brute Force 1      │ Brute Force 2      │ Optimal          │
    ├──────────────────┼────────────────────┼────────────────────┼──────────────────┤
    │ Letter mapping   │ Manual dict+chr()  │ ascii_uppercase    │ ord() arithmetic │
    │ Power calc       │ Inner loop         │ ** operator        │ None (Horner's)  │
    │ Time Complexity  │ O(n²)              │ O(n)               │ O(n)             │
    │ Space            │ O(26) for dict     │ O(26) for string   │ O(1)             │
    │ Simplicity       │ Most verbose       │ Clean & readable   │ Most concise     │
    └──────────────────┴────────────────────┴────────────────────┴──────────────────┘
"""
