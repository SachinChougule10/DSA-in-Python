# LeetCode : 1662. Check If Two String Arrays are Equivalent (Brute Force Solution)
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

        str1 = ""
        str2 = ""

        # Manually concatenate strings from word1
        for word in word1:
            str1 += word

        # Manually concatenate strings from word2
        for word in word2:
            str2 += word

        # Compare final strings
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
Logic Explanation (Brute Force Solution):

1. Create two empty strings: str1 and str2.

2. Traverse word1 array and append each string
   into str1 using += operator.

3. Traverse word2 array and append each string
   into str2.

4. Compare both generated strings.

5. Return True if both are equal,
   otherwise return False.

Time Complexity: O(n + m)

Space Complexity: O(n + m)
"""
