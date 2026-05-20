# 824. Goat Latin (Optimal Solution)
# You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
# For example, the word "apple" becomes "applema".
# If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
# Return the final sentence representing the conversion from sentence to Goat Latin.

# Example 1:

# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# Example 2:

# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

# Constraints:

# 1 <= sentence.length <= 150
# sentence consists of English letters and spaces.
# sentence has no leading or trailing spaces.
# All the words in sentence are separated by a single space.

# LeetCode 824 : Goat Latin (Brute Force Solution)


class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        # store vowels
        vowels = "aeiouAEIOU"

        # split sentence into words
        words = sentence.split()

        # list to store final transformed words
        result = []

        # traverse all words
        for i in range(len(words)):

            word = words[i]

            # if word starts with vowel
            if word[0] in vowels:

                # append "ma"
                new_word = word + "ma"

            else:
                # move first character to end
                # then append "ma"
                new_word = word[1:] + word[0] + "ma"

            # append required number of 'a'
            new_word += "a" * (i + 1)

            # store transformed word
            result.append(new_word)

        # join all words efficiently
        return " ".join(result)


# Example Usage
obj = Solution()

print(obj.toGoatLatin("I speak Goat Latin"))
# Output : Imaa peaksmaaa oatGmaaaa atinLmaaaaa

print(obj.toGoatLatin("The quick brown fox jumped over the lazy dog"))
# Output : heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa

"""
Logic (Optimal Approach):
1. Split sentence into words.
2. Traverse every word:
   - if starts with vowel, append "ma"
   - otherwise move first character to end and append "ma"
3. Append increasing number of 'a' characters.
4. Store transformed words inside list.
5. Use join() to combine all words efficiently.

Why This Is Optimal:
- List append works in O(1).
- join() combines strings efficiently in one operation.
- Avoids repeated string concatenation.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
