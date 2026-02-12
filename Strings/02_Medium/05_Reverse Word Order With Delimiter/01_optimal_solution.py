# Geeks For Geeks : Reverse Words
# Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).

# Note: The string may contain leading or trailing dots(.) or multiple dots(.) between two words. The returned string should only have a single dot(.) separating the words, and no extra dots should be included.

# Examples :

# Input: s = "i.like.this.program.very.much"
# Output: "much.very.program.this.like.i"
# Explanation: The words in the input string are reversed while maintaining the dots as separators, resulting in "much.very.program.this.like.i".

# Input: s = "..geeks..for.geeks."
# Output: "geeks.for.geeks"
# Explanation: After removing extra dots and reversing the whole string, the input string becomes "geeks.for.geeks".

# Input: s = "..home....."
# Output: "home"
# Explanation: The input string contains only one word with extra dots around it. After removing the extra dots, the output is "home".


class Solution:
    def reverse_words(self, s: str) -> str:
        # Step 1: Split the string using '.' as delimiter
        # This creates a list of words (including empty strings if multiple dots exist)
        words = s.split(".")

        # Step 2: Remove empty strings caused by leading, trailing, or multiple consecutive dots
        valid = []
        for word in words:
            if word != "":  # Ignore empty strings
                valid.append(word)

        # Step 3: Reverse the list of valid words
        valid.reverse()

        # Step 4: Join the reversed words using a single dot. This ensures only one dot between words
        result = ".".join(valid)

        return result


obj = Solution()

s1 = "..geeks..for.geeks."
print(obj.reverse_words(s1))  # Output: geeks.for.geeks

s2 = "i.like.this.program.very.much"
print(obj.reverse_words(s2))  # Output: much.very.program.this.like.i

"""
Logic : 

Problem Understanding:
----------------------
We are given a string where words are separated by dots (.).
The task is to:
1) Reverse the order of words.
2) Remove leading, trailing, and multiple consecutive dots.
3) Ensure only a single dot separates words in the final output.

Approach:
---------
1) Split the string using '.' as delimiter:
   - This gives us a list of words.
   - Multiple dots create empty strings in the list.

   Example:
   "..geeks..for.geeks."
   -> ["", "", "geeks", "", "for", "geeks", ""]

2) Remove empty strings:
   - Ignore "" while collecting valid words.
   - This removes unwanted dots.

3) Reverse the list of valid words:
   - We reverse the word order (not individual characters).

4) Join using ".":
   - Ensures exactly one dot between words.
   - Prevents extra dots in output.

Time Complexity:
----------------
O(n)
- split() takes O(n)
- filtering takes O(n)
- reverse() takes O(n)
- join() takes O(n)

Overall: O(n)

Space Complexity:
-----------------
O(n)
- We store words in a list.

Why This Approach is Good:
--------------------------
- Clean and readable.
- Handles edge cases (leading/trailing/multiple dots).
- Linear time complexity.
"""
