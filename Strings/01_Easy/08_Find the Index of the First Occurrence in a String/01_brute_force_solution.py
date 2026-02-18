# Leetcode : 28. Find the Index of the First Occurrence in a String (Brute Force Solution)
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

        # If needle is empty, return 0 as per problem requirement
        if needle == "":
            return 0

        # Traverse till last valid starting index
        # (len(haystack) - len(needle)) ensures we don't go out of bounds
        for i in range(len(haystack) - len(needle) + 1):
            # Compare each character of needle
            for j in range(len(needle)):
                # If characters do not match, stop checking this index
                if haystack[i + j] != needle[j]:
                    break
                # If we reached the last character of needle it means full match is found
                if j == len(needle) - 1:
                    return i
        # If no match found after full traversal
        return -1


obj = Solution()

haystack1, needle1 = "sadbutsad", "sad"
print(obj.strStr(haystack1, needle1))  # output : 0

haystack2, needle2 = "leetcode", "leeto"
print(obj.strStr(haystack2, needle2))  # output : -1

"""
Logic:

Approach Used: Brute Force String Matching

1. If needle is empty:
   Return 0 (as per problem statement).

2. Outer Loop (i):
   Runs from 0 to len(haystack) - len(needle)
   This ensures there are enough characters left in haystack to compare with needle.

3. Inner Loop (j):
   Compares characters one by one:
       haystack[i + j] with needle[j]

4. If mismatch occurs:
   Break the inner loop and move to next i.

5. If we reach the last character of needle
   (j == len(needle) - 1):
   That means all characters matched, so return the starting index i.

6. If no match is found after checking all possible positions:
   Return -1.

--------------------------------
Time Complexity:
O(n * m)

Where:
n = length of haystack
m = length of needle

Worst case:
Every character of haystack is compared with every character of needle.

--------------------------------
Space Complexity:
O(1)

No extra space is used.
"""
