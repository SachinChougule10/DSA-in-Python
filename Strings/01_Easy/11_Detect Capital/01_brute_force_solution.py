# LeetCode : 520 : Detect Capital. We define the usage of capitals in a word to be right when one of the following cases holds:   (Brute Force Solution)

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.


# Example 1:
# Input: word = "USA"
# Output: true

# Example 2:
# Input: word = "FlaG"
# Output: false

# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.


class Solution:
    def detect_capital_use(self, word: str) -> bool:

        # Count uppercase letters
        capital_count = 0

        # Traverse every character in the word
        for ch in word:

            # Check whether character is uppercase
            if "A" <= ch <= "Z":
                capital_count += 1

        # Case 1:
        # All letters are uppercase
        if capital_count == len(word):
            return True

        # Case 2:
        # All letters are lowercase
        if capital_count == 0:
            return True

        # Case 3:
        # Only first letter is uppercase
        if capital_count == 1 and "A" <= word[0] <= "Z":
            return True

        # Otherwise invalid capital usage
        return False


obj = Solution()

word1 = "FlaG"
print(obj.detect_capital_use(word1))  # Output : False

word2 = "USA"
print(obj.detect_capital_use(word2))  # Output : True

word3 = "Google"
print(obj.detect_capital_use(word3))  # Output : True

"""
Logic:
1. Traverse the string and count uppercase letters.
2. If uppercase count equals word length,
   then all letters are capital.
3. If uppercase count is 0,
   then all letters are lowercase.
4. If uppercase count is 1 and first letter is uppercase,
   then only first letter is capital.
5. Otherwise return False.

Time Complexity  : O(n)
Space Complexity : O(1)
"""
