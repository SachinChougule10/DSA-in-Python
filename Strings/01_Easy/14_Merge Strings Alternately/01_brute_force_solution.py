# LeetCode : 1768. Merge Strings Alternately. You are given two strings word1 and word2 (Brute Force Solution)
# Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # final merged string
        result = ""

        # lengths of both strings
        n = len(word1)
        m = len(word2)

        # maximum length among both strings
        max_len = max(n, m)

        # traverse till maximum length
        for i in range(max_len):

            # add character from word1 if index exists
            if i < n:
                result += word1[i]

            # add character from word2 if index exists
            if i < m:
                result += word2[i]

        # return merged string
        return result


# Example Usage
obj = Solution()

print(obj.mergeAlternately("abc", "pqr"))  # Output : apbqcr
print(obj.mergeAlternately("ab", "pqrs"))  # Output : apbqrs
print(obj.mergeAlternately("abcd", "pq"))  # Output : apbqcd


"""
Logic (Brute Force Approach):
1. Find the maximum length among both strings.
2. Traverse from index 0 to max length - 1.
3. At every index:
   - add character from word1 if index exists
   - add character from word2 if index exists
4. Continue until all characters are merged.

Why It Is Brute Force:
- String concatenation is done repeatedly using '+' operator.
- Since strings are immutable in Python, every concatenation creates a new string.
- This increases overall time complexity.

Time Complexity:
O((n + m)^2)

Space Complexity:
O(n + m)
"""
