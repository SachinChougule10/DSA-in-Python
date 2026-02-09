# Leetcode : 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.


class Solution:
    def reverse_words(self, s: str) -> str:
        # Step 1: Split the string by whitespace
        # split() automatically removes leading, trailing, and extra spaces between words
        words = s.split()

        # Step 2: Reverse the list of words in-place
        words.reverse()

        # Step 3: Join the reversed words using a single space
        result = " ".join(words)

        return result


# Driver code for testing
s = "the sky is blue"

obj = Solution()
print(obj.reverse_words(s))

"""
Logic: 
1. The input string may contain:
   - Leading spaces
   - Trailing spaces
   - Multiple spaces between words

2. Using s.split():
   - Splits the string into words based on whitespace
   - Automatically removes extra spaces
   - Example:
       "  the   sky is  blue  " → ["the", "sky", "is", "blue"]

3. Reverse the list of words:
   - ["the", "sky", "is", "blue"] → ["blue", "is", "sky", "the"]

4. Join the words using a single space:
   - Ensures the output has exactly one space between words

Time Complexity:
O(n), where n is the length of the string.

Space Complexity:
O(n), for storing the list of words.
"""
