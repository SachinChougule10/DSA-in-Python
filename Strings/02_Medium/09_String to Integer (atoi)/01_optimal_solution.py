# Leetcode : 8. String to Integer (atoi) : Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range.
# Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

# Example 1:
# Input: s = "42"
# Output: 42
# Explanation:
# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^

# Example 2:
# Input: s = "1337c0d3"
# Output: 1337
# Explanation:
# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^

# Example 3:
# Input: s = "words and 987"
# Output: 0
# Explanation: Reading stops at the first non-digit character 'w'.


class Solution:
    def my_atoi(self, s: str) -> int:
        i = 0  # Pointer to traverse the string
        n = len(s)
        num = 0  # Final number being built
        sign = 1  # Default sign is positive

        # Step 1: Ignore leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check for optional sign
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1  # If negative sign found
            i += 1  # Move pointer after sign

        # Step 3: Convert digits and build the number
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")  # Convert char to integer
            num = num * 10 + digit  # Shift left and add digit
            i += 1

        # Apply sign to the number
        num *= sign

        # Step 4: Clamp to 32-bit signed integer range
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return -(2**31)
        if num > INT_MAX:
            return 2**31 - 1

        return num


obj = Solution()

s1 = "1337c0d3"
print(obj.my_atoi(s1))  # output : 1337

s2 = "-42"
print(obj.my_atoi(s2))  # output : -42

s3 = "words and 987"
print(obj.my_atoi(s3))  # output : 0


"""
Logic -

Goal: Convert a string into a 32-bit signed integer.

------------------------------------------------------------
STEP 1: Skip Leading Whitespaces
------------------------------------------------------------
Move pointer 'i' forward while encountering spaces.
Example:
"   -42"
   ^
After skipping spaces:
"-42"
 ^

------------------------------------------------------------
STEP 2: Determine Sign
------------------------------------------------------------
If current character is '+' → sign = +1
If current character is '-' → sign = -1
If neither → assume positive.

------------------------------------------------------------
STEP 3: Convert Characters to Number
------------------------------------------------------------
Keep reading characters while they are digits (0-9).

To convert char to digit:
digit = ord(char) - ord('0')

Number building logic:
num = num * 10 + digit

Example:
"123"
num = 0
num = 0*10 + 1 = 1
num = 1*10 + 2 = 12
num = 12*10 + 3 = 123

Stop when:
- Non-digit encountered
- End of string reached

------------------------------------------------------------
STEP 4: Apply Sign
------------------------------------------------------------
Multiply final number by sign.

------------------------------------------------------------
STEP 5: Handle Overflow
------------------------------------------------------------
Valid 32-bit signed integer range:
[-2^31, 2^31 - 1]
[-2147483648, 2147483647]

If number < INT_MIN → return INT_MIN
If number > INT_MAX → return INT_MAX

------------------------------------------------------------
Time Complexity:
O(n)  → We traverse the string once.

Space Complexity:
O(1)  → No extra space used.

------------------------------------------------------------
Edge Cases Covered:
✔ Leading spaces
✔ Optional + / -
✔ Non-digit stopping condition
✔ Empty or invalid string
✔ Overflow handling
"""
