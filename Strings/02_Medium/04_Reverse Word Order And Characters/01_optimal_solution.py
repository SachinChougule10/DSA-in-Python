# Geeks For Geeks : Reverse Words and Characters in a String
# Problem Statement: Given a string s, reverse the order of the words in the string and also reverse the characters of each word.

# A word is defined as a sequence of non-space characters.
# Words in the string may be separated by one or more spaces.

# Return a string where:
# The order of words is reversed.
# Each word’s characters are reversed.
# Words are separated by exactly one space.
# No leading or trailing spaces exist in the output.

# Example:
# Input:  s = "the sky is blue"
# Output: "eulb si yks eht"


class Solution:
    def reverse_words(self, s: str) -> str:
        # Split the string into words.
        # split() automatically removes extra spaces
        words = s.split()

        # Reverse the order of words in-place
        words.reverse()

        # List to store each reversed word
        reversed_words = []

        # Reverse characters of each word
        for word in words:
            reversed_words.append(word[::-1])

        # Join all reversed words with a single space
        result = " ".join(reversed_words)

        return result


s = "the sky is blue"

obj = Solution()
print(obj.reverse_words(s))

"""
Logic:

Goal:
1. Reverse the order of words.
2. Reverse characters inside each word.
3. Ensure exactly one space between words.
4. No leading/trailing spaces in output.

Step-by-step Approach:

1. Use s.split()
   - Converts string into list of words.
   - Automatically removes extra spaces.
   - Example:
       "the sky is blue" → ["the", "sky", "is", "blue"]

2. Reverse the list of words:
       ["blue", "is", "sky", "the"]

3. Reverse each word individually using slicing:
       word[::-1]
   - Example:
       "blue" → "eulb"

4. Store reversed words in a list.

5. Use " ".join(list)
   - Joins words with exactly one space.
   - Efficient: O(n) time (single string allocation).

Time Complexity:
O(n) — Each character is processed a constant number of times.

Let:
n = total number of characters
k = number of words

1) s.split()            → O(n)
2) words.reverse()      → O(k)
3) Reverse each word    → O(n)
4) " ".join(...)        → O(n)

Total:
O(n + k + n + n)

Since k ≤ n,
Overall Time Complexity = O(n)

Space Complexity:
O(n) — Extra list used to store words and final result.

Why This Is Efficient:
- Avoids string concatenation inside loop (which would cause O(n^2)).
- Uses list + join pattern, which is optimal in Python.
"""
