# GFG : Count type of Characters (Brute Force Solution)
# Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.
# Note: There are no white spaces in the string.

# Example 1:

# Input:
# S = "#GeeKs01fOr@gEEks07"
# Output:
# 5
# 8
# 4
# 2
# Explanation: There are 5 uppercase characters, 8 lowercase characters, 4 numeric characters
# and 2 special characters.

# Example 2:

# Input:
# S = "*GeEkS4GeEkS*"
# Output:
# 6
# 4
# 1
# 2
# Explanation: There are 6 uppercase characters, 4 lowercase characters, 1 numeric characters
# and 2 special characters.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function count() which takes the string S as input and returns an array of size 4 where arr[0] = number of uppercase characters, arr[1] = number of lowercase characters, arr[2] = number of numeric characters and arr[3] = number of special characters.

# Expected Time Complexity: O(|S|).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1<=|S|<=105


class Solution:
    def count(self, s):

        # counters for each type
        upper = 0
        lower = 0
        digit = 0
        special = 0

        # store all uppercase letters
        uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # store all lowercase letters
        lowercase_chars = "abcdefghijklmnopqrstuvwxyz"

        # store all digits
        digit_chars = "0123456789"

        # traverse every character
        for ch in s:

            # check uppercase manually
            if ch in uppercase_chars:
                upper += 1

            # check lowercase manually
            elif ch in lowercase_chars:
                lower += 1

            # check digit manually
            elif ch in digit_chars:
                digit += 1

            # otherwise special character
            else:
                special += 1

        # return all counts
        return upper, lower, digit, special


# Example Usage
obj = Solution()

print(obj.count("#GeeKs01fOr@gEEks07"))  # Output : (5, 8, 4, 2)


"""
Logic (Brute Force Approach):
1. Store uppercase letters, lowercase letters,
   and digits separately.
2. Traverse every character in the string.
3. For each character:
   - check if it exists in uppercase letters
   - otherwise check lowercase letters
   - otherwise check digits
   - else count it as special character
4. Return all counts.

Why It Is Brute Force:
- Membership checking using 'in' scans characters manually.
- Multiple sequential checks are performed for every character.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""
