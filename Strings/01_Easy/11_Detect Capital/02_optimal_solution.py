# LeetCode : 520 : Detect Capital. We define the usage of capitals in a word to be right when one of the following cases holds:   (Optimal Solution)

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
        # Return True if:
        # 1. All letters are uppercase
        # 2. All letters are lowercase
        # 3. Only first letter is uppercase
        return word.isupper() or word.islower() or word.istitle()


obj = Solution()

word1 = "FlaG"
print(obj.detect_capital_use(word1))  # Output : False

word2 = "USA"
print(obj.detect_capital_use(word2))  # Output : True

word3 = "Google"
print(obj.detect_capital_use(word3))  # Output : True

"""
Logic:
1. word.isupper()
   - Checks whether all characters are uppercase.

2. word.islower()
   - Checks whether all characters are lowercase.

3. word.istitle()
   - Checks whether only the first character is uppercase
     and remaining characters are lowercase.

4. If any one condition is True,
   then the capital usage is correct.

Time Complexity  : O(n)
Space Complexity : O(1)
"""
