# LeetCode : 345. Reverse Vowels of a String. Given a string s, reverse only all the vowels in the string and return it (Brute Force Solution)
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters


class Solution:
    def reverse_vowels(self, s: str) -> str:

        # store all vowels
        vowels = "aeiouAEIOU"

        # convert string into list because strings are immutable
        s = list(s)

        # list to store vowels present in string
        temp = []

        # collect all vowels from string
        for ch in s:
            if ch in vowels:
                temp.append(ch)

        # pointer for last vowel in temp
        j = len(temp) - 1

        # replace vowels in string using reverse order
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = temp[j]
                j -= 1

        # convert list back to string
        return "".join(s)


# Example Usage
obj = Solution()

s1 = "hello"
print(obj.reverse_vowels(s1))  # holle

s2 = "leetcode"
print(obj.reverse_vowels(s2))  # leotcede


"""
Output:

Logic (Brute Force Approach):
1. Traverse the string and store all vowels in a separate list.
2. Since we need reversed vowels, start taking vowels from the end of that list.
3. Traverse the original string again:
   - whenever a vowel is found, replace it with the last vowel from temp.
4. Join the list back into a string and return it.

Time Complexity:
O(n)

Space Complexity:
O(n)
because extra list is used to store vowels.
"""
