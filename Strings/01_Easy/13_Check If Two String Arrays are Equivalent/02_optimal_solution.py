# LeetCode : 1662. Check If Two String Arrays are Equivalent (Optimal Solution)
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Example 2:
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false

# Example 3:
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true

# Constraints:
# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.

# LeetCode : 1662 : Check If Two String Arrays are Equivalent (Brute Force Solution)


class Solution:
    def array_strings_are_equal(self, word1: list[str], word2: list[str]) -> bool:
        # Join all strings from word1 into a single string
        str1 = "".join(word1)

        # Join all strings from word2 into a single string
        str2 = "".join(word2)

        # Compare both final strings
        return str1 == str2


obj = Solution()

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(obj.array_strings_are_equal(word1, word2))  # Output : True

word3 = ["abc", "d", "defg"]
word4 = ["abcddefg"]
print(obj.array_strings_are_equal(word3, word4))  # Output : True

word5 = ["a", "cb"]
word6 = ["ab", "c"]
print(obj.array_strings_are_equal(word5, word6))  # Output : False

"""
Logic Explanation (Optimal Solution):

1. Each array represents a string formed by concatenating all its elements.
   Example:
   ["ab", "c"] -> "abc"

2. We use "".join(array) to combine all strings in the array.

3. After forming both complete strings,
   compare them directly using ==.

4. If both strings are equal, return True.
   Otherwise, return False.

Time Complexity: O(n + m)
- n = total characters in word1
- m = total characters in word2

Space Complexity: O(n + m)
- Extra space used for storing concatenated strings.
"""
