# Leetcode : 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def valid_anagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Sort both strings- sorted() returns a list of characters in ascending order
        sort_s = sorted(s)
        sort_t = sorted(t)

        # Step 3: Compare the sorted character lists
        if sort_s == sort_t:
            return True

        # Step 4: If sorted lists don't match, not an anagram
        return False


s = "anagram"
t = "nagaram"

u = "rat"
v = "car"

obj = Solution()
print(obj.valid_anagram(s, t))  # output: True
print(obj.valid_anagram(u, v))  # output: False

"""
Logic (Brute Force Approach):

1. An anagram must contain the same characters with the same frequency.
   Therefore, both strings must be of equal length.

2. Both strings are sorted alphabetically.
   - If two strings are anagrams, their sorted forms will be identical.

3. The sorted character lists are compared.
   - If they match → return True
   - Otherwise → return False

TIME COMPLEXITY:
- O(n log n), where n is the length of the string (due to sorting)

SPACE COMPLEXITY:
- O(n), for storing sorted character lists

"""
