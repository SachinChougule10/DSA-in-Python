# Leetcode : 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def valid_anagram(self, s: str, t: str) -> bool:

        # Dictionary to store frequency of characters in string s
        freq_map = {}

        # Step 1: If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Count frequency of each character in s
        for ch in s:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        # Step 3: Reduce frequency using characters from t
        for ch in t:
            # If character not found in freq_map, it's not an anagram
            if ch not in freq_map:
                return False
            else:
                # If frequency is already zero, extra character found
                if freq_map[ch] == 0:
                    return False
                else:
                    # Decrease frequency for matched character
                    freq_map[ch] -= 1

        # Step 4: If all checks pass, strings are anagrams
        return True


s = "anagram"
t = "nagaram"

u = "rat"
v = "car"

obj = Solution()
print(obj.valid_anagram(s, t))  # output: True
print(obj.valid_anagram(u, v))  # output: False

"""
Logic (Optimal Solution):

1. Two strings are anagrams if they contain the same characters with the same frequency.

2. First, the lengths of both strings are compared.
   - If lengths differ, they cannot be anagrams.

3. A frequency map (dictionary) is created for string s.
   - Each character is stored as a key with its count as value.

4. String t is then traversed:
   - If a character does not exist in the frequency map, the strings are not anagrams.
   - If a character's frequency becomes zero before all occurrences are matched, return False.
   - If a character's frequency becomes zero and we still encounter it again, it means the character 
     appears more times in t than in s, so the strings cannot be anagrams.
   - Otherwise, decrease the frequency count.

5. If all characters are matched correctly, return True.

TIME COMPLEXITY:
- O(n), where n is the length of the string

SPACE COMPLEXITY:
- O(1) (constant space, since only 26 lowercase letters are stored)
"""
