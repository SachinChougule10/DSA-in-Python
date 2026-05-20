# 824. Goat Latin (Brute Force Solution)
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

        # final answer string
        result = ""

        # traverse every word
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

            # add word into result string
            result += new_word

            # avoid extra space after last word
            if i != len(words) - 1:
                result += " "

        # return final Goat Latin sentence
        return result


# Example Usage
obj = Solution()

print(obj.toGoatLatin("I speak Goat Latin"))
# Output : Imaa peaksmaaa oatGmaaaa atinLmaaaaa

print(obj.toGoatLatin("The quick brown fox jumped over the lazy dog"))
# Output : heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa


"""
Logic (Brute Force Approach):
1. Split the sentence into words.
2. Traverse every word one by one.
3. If word starts with vowel:
   - append "ma"
4. Otherwise:
   - move first character to end
   - append "ma"
5. Append 'a' characters according to word position.
6. Build final string using repeated string concatenation.

Why It Is Brute Force:
- Uses repeated string concatenation with '+' operator.
- Since strings are immutable in Python,
  new strings are created repeatedly.

Time Complexity:
O(n^2)

Space Complexity:
O(n)
"""
