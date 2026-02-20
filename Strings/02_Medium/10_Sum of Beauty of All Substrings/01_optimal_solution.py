# Leetcode : 1781. Sum of Beauty of All Substrings : The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

# Example 1:
# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

# Example 2:
# Input: s = "aabcbaa"
# Output: 17


class Solution:
    def beauty_sum(self, s: str) -> int:
        n = len(s)
        total_beauty = 0

        # Outer loop: fix starting index of substring
        for i in range(n):
            # Create fresh frequency array for new starting index, 26 because only lowercase letters (a–z)
            freq = [0] * 26

            # Inner loop: extend substring from i to j
            for j in range(i, n):
                # Update frequency of current character
                freq[ord(s[j]) - ord("a")] += 1

                max_freq = 0
                min_freq = float("inf")

                # Find max and min frequency among non-zero characters
                # We ignore zero frequencies because beauty is defined only among characters present in the substring.
                for f in freq:
                    if f > 0:
                        max_freq = max(max_freq, f)
                        min_freq = min(min_freq, f)

                # Compute and add beauty for each substring s[i:j+1]
                beauty = max_freq - min_freq
                total_beauty += beauty

        return total_beauty


obj = Solution()

s1 = "aabcb"
print(obj.beauty_sum(s1))  # output: 5

s2 = "aabcbaa"
print(obj.beauty_sum(s2))  # output: 17

"""
Logic:

We need to generate ALL substrings.
Number of substrings = n(n+1)/2 → O(n²)

Outer loop (i)  → starting index
Inner loop (j)  → ending index

WHY DO WE CREATE A NEW freq ARRAY AFTER EVERY NEW i?

Because:
- Each new i means we are starting a completely new substring.
- So frequency counting must start fresh.

Example:
i = 0 → substrings: "a", "aa", "aab", ...
i = 1 → substrings: "a", "ab", ...

These are different starting points. So frequency must reset.

WHY DON'T WE RESET freq AFTER EVERY j?

Because:
- j only extends the current substring.
- We are building on previous frequency.

Example:
"a" → "aa" → "aab" → "aabc"

If we reset every j:
- We would recompute frequency from scratch.
- That would increase time complexity to O(n³).
Keeping the same freq makes it efficient: O(n²).

WHY SIZE 26?

Because:
- String contains only lowercase English letters.
- 'a' to 'z' → total 26 characters.
- We map characters using: index = ord(character) - ord('a')

WHY IGNORE ZERO FREQUENCY?

Characters that don't appear in the substring should not be considered for min frequency.
So we only check f > 0.

------------------------------------------------------------

Time Complexity:

Outer loop → O(n)
Inner loop → O(n)
Frequency scan → 26 (constant)

Total = O(n² * 26) ≈ O(n²)

------------------------------------------------------------
Space Complexity: 

Frequency array size = 26 → O(1)
"""
