# LeetCode : 1832. Check if the Sentence Is Pangram (Brute Force Solution)
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:
# Input: sentence = "leetcode"
# Output: false

# Constraints:
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters


class Solution:
    def check_if_pangram(self, sentence: str) -> bool:

        # Convert sentence to lowercase
        sentence = sentence.lower()

        # Traverse all alphabets from a to z
        for ch in "abcdefghijklmnopqrstuvwxyz":

            # Check if alphabet is missing
            if ch not in sentence:
                return False

        # All alphabets found
        return True


obj = Solution()

sentence1 = "thequickbrownfoxjumpsoverthelazydog"
print(obj.check_if_pangram(sentence1))  # Output : True

sentence2 = "leetcode"
print(obj.check_if_pangram(sentence2))  # Output : False


"""
LOGIC EXPLANATION (Brute Force)

A pangram is a sentence containing all 26 English lowercase letters at least once.

Approach:
1. Convert string to lowercase
2. Traverse all alphabets from 'a' to 'z'
3. For every alphabet:
      check whether it exists in sentence
4. If any alphabet is missing:
      return False
5. Otherwise:
      return True


TIME COMPLEXITY:
O(26 * n)

because for every alphabet, we search entire string.

SPACE COMPLEXITY:
O(1)
"""
