# 383. Ransom Note (Brute Force Solution)
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


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # convert magazine string into list
        # so used characters can be removed
        magazine = list(magazine)

        # traverse every character in ransomNote
        for ch in ransomNote:

            # check if character exists in magazine
            if ch in magazine:

                # remove first occurrence of character
                magazine.remove(ch)

            else:
                # character not found
                return False

        # all characters matched successfully
        return True


# Example Usage
obj = Solution()

print(obj.canConstruct("a", "b"))  # Output : False
print(obj.canConstruct("aa", "ab"))  # Output : False
print(obj.canConstruct("aa", "aab"))  # Output : True


"""
Logic (Brute Force Approach):
1. Convert magazine into a list.
2. Traverse every character of ransomNote.
3. For each character:
   - search it inside magazine
   - if found, remove it so it cannot be reused
   - otherwise return False
4. If all characters are matched successfully, return True.

Why It Is Brute Force:
- Searching and removing from list takes O(n) time.
- This process repeats for every character.

Time Complexity:
O(n * m)

Space Complexity:
O(m)
because magazine is converted into a list.
"""
