# LeetCode : 1832. Check if the Sentence Is Pangram (Optimal Solution)
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

        # Store unique letters
        letter = set()

        # Traverse each character
        for ch in sentence:

            # Check if character is alphabet
            if "a" <= ch <= "z":

                # Add character to set
                letter.add(ch)

        # Pangram if all 26 letters exist
        return len(letter) == 26


obj = Solution()

sentence1 = "thequickbrownfoxjumpsoverthelazydog"
print(obj.check_if_pangram(sentence1))  # Output : True

sentence2 = "leetcode"
print(obj.check_if_pangram(sentence2))  # Output : False

"""
LOGIC EXPLANATION

A pangram is a sentence containing all 26 English lowercase letters at least once.

Approach:
1. Convert string to lowercase
2. Traverse each character
3. Store unique alphabets in a set
4. If set size becomes 26:
      return True
   else:
      return False

Why set?
- Set stores only unique values
- Duplicate letters are ignored automatically

TIME COMPLEXITY:
O(n)

SPACE COMPLEXITY:
O(1)
because at most 26 letters are stored
"""
