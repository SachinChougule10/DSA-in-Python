# LeetCode : 345. Reverse Vowels of a String. Given a string s, reverse only all the vowels in the string and return it (Optimal Solution)
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

        # strings are immutable -> convert into list
        s = list(s)

        # set for fast vowel lookup
        vowels = set("aeiouAEIOU")

        # two pointers
        left = 0
        right = len(s) - 1

        # move until pointers meet
        while left < right:

            # move left pointer until vowel is found
            while left < right and s[left] not in vowels:
                left += 1

            # move right pointer until vowel is found
            while left < right and s[right] not in vowels:
                right -= 1

            # swap vowels
            s[left], s[right] = s[right], s[left]

            # move pointers inward
            left += 1
            right -= 1

        # convert list back to string
        return "".join(s)


# Example Usage
obj = Solution()

s1 = "hello"
print(obj.reverse_vowels(s1))  # holle

s2 = "leetcode"
print(obj.reverse_vowels(s2))  # leotcede

"""
Logic (Optimal Two Pointer Approach):
1. Use two pointers:
   - left starts from beginning
   - right starts from end

2. Move left pointer until a vowel is found.

3. Move right pointer until a vowel is found.

4. Swap both vowels.

5. Continue until left >= right.

Why This Works:
- Only vowels are swapped.
- Non-vowel characters remain in same position.
- Two pointers help reverse vowels efficiently in one traversal.

Time Complexity:
O(n)

Space Complexity:
O(1)
excluding output string conversion.
"""
