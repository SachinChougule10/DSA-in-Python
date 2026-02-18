# Leetcode : 28. Find the Index of the First Occurrence in a String (Brute Force Solution - Slicing)
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

        # m = length of haystack
        # n = length of needle
        m = len(haystack)
        n = len(needle)

        # Iterate through possible starting indices
        # We stop at (m - n) to avoid index out of bounds
        for i in range(m - n + 1):
            # Compare substring of length n with needle
            # haystack[i : i+n] gives substring starting at i
            if haystack[i : n + i] == needle:
                return i  # Return first matching index

        # If no match found
        return -1


obj = Solution()

haystack1, needle1 = "sadbutsad", "sad"
print(obj.strStr(haystack1, needle1))  # output : 0

haystack2, needle2 = "leetcode", "leeto"
print(obj.strStr(haystack2, needle2))  # output : -1

"""
Logic: 
Problem:
Find the first occurrence of 'needle' inside 'haystack'.
Return its starting index.
If not found, return -1.

----------------------------------------
Approach Used:
Brute Force using String Slicing
----------------------------------------

1. If needle is empty:
   Return 0 (as per problem requirement).

2. Let:
      m = length of haystack
      n = length of needle

3. Traverse from index 0 to (m - n):
   This ensures enough characters remain to compare a substring of length n.

4. At each index i:
   Extract substring:
        haystack[i : i + n]

5. Compare this substring with needle:
      If equal → return i

6. If loop completes without match:
      Return -1

----------------------------------------
Why (m - n + 1)?

Because the last valid starting index for a substring of length n inside a string of length m is (m - n).

----------------------------------------
Time Complexity:
O((m - n + 1) * n)
≈ O(m * n) in worst case

Since slicing creates a new substring of length n at each iteration.

----------------------------------------
Space Complexity:
O(n)

Because slicing creates a new substring of size n at every iteration.
"""
