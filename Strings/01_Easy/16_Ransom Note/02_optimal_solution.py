# 383. Ransom Note (Optimal Solution)
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters

from collections import Counter


class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:

        # store frequency of characters from magazine
        freq = Counter(magazine)

        # traverse every character in ransomNote
        for ch in ransomNote:

            # if character frequency becomes 0
            # character is not available
            if freq[ch] <= 0:
                return False

            # use one occurrence of character
            freq[ch] -= 1

        # all characters are available
        return True


# Example Usage
obj = Solution()

print(obj.can_construct("a", "b"))  # Output : False
print(obj.can_construct("aa", "ab"))  # Output : False
print(obj.can_construct("aa", "aab"))  # Output : True

"""
Logic (Optimal HashMap Approach):
1. Store frequency of all characters from magazine using Counter.
2. Traverse ransomNote character by character.
3. For every character:
   - check if frequency is greater than 0
   - if not, return False
   - otherwise decrease frequency
4. If all characters are successfully used, return True.

Why This Is Optimal:
- HashMap provides O(1) average lookup time.
- Avoids repeated searching in the string/list.

Time Complexity:
O(n + m)

Space Complexity:
O(m)
for frequency hashmap.
"""
