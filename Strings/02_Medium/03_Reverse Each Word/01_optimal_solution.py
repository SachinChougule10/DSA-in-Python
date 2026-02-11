# Geeks For Geeks : Reverse each word in a given string
# You are given a string s. You need to reverse each word in it where the words are separated by spaces and return the modified string.
# Note: The string may contain leading or trailing spaces, or multiple spaces between two words. The returned string should only have a single space separating the words, and no extra spaces should be included.

# Input: s = " i like this program very much "
# Output: "i ekil siht margorp yrev hcum"

# Explanation: The words are reversed as follows:
# "i" -> "i","like"->"ekil",
# "this"->"siht","program" -> "margorp",
# "very" -> "yrev","much" -> "hcum".


class Solution:
    def reverse_each_word(self, s: str) -> str:

        # Split string into words.
        # split() automatically:
        # - Removes leading/trailing spaces
        # - Handles multiple spaces between words
        words = s.split()

        # Create an empty list to store reversed words
        reversed_words = []

        # Reverse each word using slicing
        for word in words:
            reversed_words.append(word[::-1])

        # Join all reversed words with a single space. Ensures no extra spaces in final output
        result = " ".join(reversed_words)

        return result


s = " i like this program very much "

obj = Solution()
print(obj.reverse_each_word(s))  # output : i ekil siht margorp yrev hcum

"""
Logic: 
1. We use s.split() to break the string into words.
   - It removes unnecessary spaces automatically.
   - Example:
       "  i like   this  ".split()
       → ["i", "like", "this"]

2. We reverse each word using slicing:
       word[::-1]
   This creates a reversed copy of the word.

3. We store reversed words in a list.

4. We use " ".join() to:
   - Combine words with exactly one space.
   - Avoid leading or trailing spaces.


=============================
Why This Version Is Better
=============================

Previously, we used:

    result += word[::-1] + " "

Problem:
- Strings in Python are immutable.
- Every time we use +=, a new string is created.
- If there are many words, this results in repeated copying.
- Worst-case time complexity becomes O(n²).
- Because Python strings are immutable. Each concatenation creates a new string and copies existing content. 
  Repeated copying leads to quadratic time complexity.

In this version:
- We store reversed words in a list.
- We call " ".join() once at the end.
- join() efficiently allocates memory only once.

Therefore:
Time Complexity becomes O(n).


=============================
Time Complexity
=============================

Let n be the length of the string.

- split() → O(n)
- Reversing all characters → O(n)
- join() → O(n)

Overall Time Complexity: O(n)


=============================
Space Complexity
=============================

- words list → O(n)
- reversed_words list → O(n)
- final result string → O(n)

Overall Space Complexity: O(n)
"""
