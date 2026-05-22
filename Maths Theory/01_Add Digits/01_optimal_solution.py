# LeetCode : 258. Add Digits (Optimal Solution)
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input: num = 38

# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0

# Constraints:
# 0 <= num <= 231 - 1
# Follow up: Could you do it without any loop/recursion in O(1) runtime?


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        # find first occurrence of character
        index = word.find(ch)

        # if character does not exist
        if index == -1:
            return word

        # reverse prefix and append remaining string
        return word[: index + 1][::-1] + word[index + 1 :]


# Example Usage
obj = Solution()

print(obj.reversePrefix("abcdefd", "d"))  # Output : dcbaefd
print(obj.reversePrefix("xyxzxe", "z"))  # Output : zxyxxe
print(obj.reversePrefix("abcd", "z"))  # Output : abcd


"""
Logic (Optimal Approach):
1. Use find() to get first occurrence of ch.
2. If character is not found, return original string.
3. Otherwise:
   - take substring from start to index
   - reverse it using slicing [::-1]
   - append remaining substring
4. Return final string.

Why This Is Optimal:
- Python slicing performs reversal efficiently.
- No manual traversal for reversal is needed.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
