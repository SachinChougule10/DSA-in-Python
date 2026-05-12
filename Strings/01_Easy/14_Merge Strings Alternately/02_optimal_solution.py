# LeetCode : 1768. Merge Strings Alternately. You are given two strings word1 and word2 (Optimal Solution)
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

        # pointers for both strings
        i = 0
        j = 0

        # list to store merged characters
        result = []

        # lengths of strings
        n = len(word1)
        m = len(word2)

        # traverse both strings together
        while i < n and j < m:

            # add character from word1
            result.append(word1[i])

            # add character from word2
            result.append(word2[j])

            # move both pointers
            i += 1
            j += 1

        # add remaining part of word1 if any
        result.append(word1[i:])

        # add remaining part of word2 if any
        result.append(word2[j:])

        # convert list into string
        return "".join(result)


# Example Usage
obj = Solution()

print(obj.mergeAlternately("abc", "pqr"))  # Output : apbqcr
print(obj.mergeAlternately("ab", "pqrs"))  # Output : apbqrs
print(obj.mergeAlternately("abcd", "pq"))  # Output : apbqcd

"""
Logic (Optimal Approach):
1. Use two pointers:
   - i for word1
   - j for word2

2. Traverse both strings simultaneously.
3. Add one character from each string alternately.
4. After one string ends:
   - append remaining substring of word1
   - append remaining substring of word2

Why This Is Optimal:
- List append operation works in O(1).
- join() combines all characters efficiently in one step.
- Avoids repeated string concatenation.

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)
"""
