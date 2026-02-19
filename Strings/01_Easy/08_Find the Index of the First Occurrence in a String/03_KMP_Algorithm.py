# Leetcode : 28. Find the Index of the First Occurrence in a String (KMP Algorithm - Knuth-Morris-Pratt)
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0 as per problem statement
        if needle == "":
            return 0
        # Step 1: Build LPS (Longest Prefix Suffix) array
        # lps_array[i] = length of longest proper prefix, which is also a suffix for substring needle[0:i+1]
        lps_array = [0] * len(needle)

        prevLPS = 0  # length of previous longest prefix suffix
        i = 1  # we start from index 1 (0 always has LPS = 0)

        while i < len(needle):
            if needle[prevLPS] == needle[i]:
                # If characters match, extend the prefix
                lps_array[i] = prevLPS + 1  # prevLPS refers to index
                i += 1
                prevLPS += 1
            else:
                if prevLPS == 0:
                    # No prefix match possible
                    lps_array[i] = 0
                    i += 1
                else:
                    # Fall back to previous LPS value
                    # lps_array[prevLPS - 1] refers to value in lps_array
                    prevLPS = lps_array[prevLPS - 1]

        # Step 2: Pattern searching using LPS array
        i = 0  # pointer for haystack
        j = 0  # pointer for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                # Characters match → move both pointers
                i += 1
                j += 1
            else:
                if j == 0:
                    # If no match and j is at start → move i
                    i += 1
                else:
                    # Jump j using LPS (avoid rechecking characters)
                    j = lps_array[j - 1]

            # If we matched full needle
            if j == len(needle):
                return i - len(needle)

        # If no match found
        return -1


obj = Solution()

haystack1, needle1 = "sadbutsad", "sad"
print(obj.strStr(haystack1, needle1))  # output : 0

haystack2, needle2 = "leetcode", "leeto"
print(obj.strStr(haystack2, needle2))  # output : -1

haystack3, needle3 = "alexbob", "bob"
print(obj.strStr(haystack3, needle3))  # output : 4

"""
Logic (KMP Algorithm - Knuth-Morris-Pratt) :

Problem:
Find the first occurrence of 'needle' in 'haystack'.

Why not brute force?
Brute force takes O(n * m) time because we restart comparison from next index every time mismatch happens.

KMP improves this to O(n + m) using LPS array.

---------------------------------------------------------
STEP 1: Build LPS (Longest Prefix Suffix) Array
---------------------------------------------------------
LPS[i] stores the length of the longest proper prefix which is also a suffix for substring needle[0:i+1].

Example:
needle = "ababaca"

LPS = [0, 0, 1, 2, 3, 0, 1]

Meaning:
At index 4 ("ababa"), longest prefix = "aba" which is also suffix → length = 3

This helps us skip unnecessary comparisons.

---------------------------------------------------------
STEP 2: Search Using Two Pointers
---------------------------------------------------------
i → pointer for haystack
j → pointer for needle

If characters match:
    Move both pointers forward

If mismatch:
    If j != 0:
        Jump j back using LPS[j-1]
    Else:
        Move i forward

This avoids re-checking characters that are already matched.

---------------------------------------------------------
Time Complexity:
    O(n + m)
    n = len(haystack)
    m = len(needle)

Space Complexity:
    O(m) for LPS array

---------------------------------------------------------
Why KMP is Optimal:
It prevents re-comparing characters by using previous pattern knowledge stored in LPS.
"""
