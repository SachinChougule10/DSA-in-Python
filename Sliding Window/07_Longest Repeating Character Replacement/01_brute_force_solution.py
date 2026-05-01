# Leetcode : 424. Longest Repeating Character Replacement : You are given a string s and an integer k (Brute Force Solution)
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        # Stores the maximum valid substring length
        max_length = 0

        # Outer loop: starting index of substring
        for i in range(n):
            # Stores frequency of characters in current substring
            hash_map = {}
            # Stores frequency of most repeating character in window
            max_freq = 0

            # Inner loop: ending index of substring
            for j in range(i, n):
                # Update frequency of current character
                hash_map[s[j]] = hash_map.get(s[j], 0) + 1

                # Track the highest frequency character in current window
                max_freq = max(max_freq, hash_map[s[j]])

                # Current window size
                window_size = j - i + 1

                # Number of changes required to make all characters same
                changes = window_size - max_freq

                # If required changes are within limit k, it's a valid substring
                if changes <= k:
                    max_length = max(max_length, window_size)
                else:
                    # If more than k changes needed, no point expanding further
                    break

        return max_length


obj = Solution()

s1 = "AABABBA"
k1 = 1
print(obj.characterReplacement(s1, k1))  # Output : 4

s2 = "ABAB"
k2 = 2
print(obj.characterReplacement(s2, k2))  # Output : 4

"""
Logic (Brute Force Approach):

1. Goal:
   Find the longest substring where you can replace at most k characters
   to make all characters in the substring the same.

2. Approach:
   - Generate all substrings using two loops (i → start, j → end).
   - Track frequency of characters using a hashmap.

3. Key Idea:
   - In any substring, we want all characters to become the same.
   - Best strategy: convert all characters to the most frequent character.

4. Formula:
   changes_needed = window_size - max_frequency_character

5. Condition:
   - If changes_needed <= k → valid substring
   - Else → break (further expansion will only increase changes)

6. Why break?
   - Because increasing window size will increase changes_needed,
     so no need to check further for this starting index.

7. Time Complexity:
   - O(n^2)

8. Space Complexity:
   - O(26) ≈ O(1)

Example:
s = "AABABBA", k = 1
- Longest valid substring length = 4 ("AABA" or "BBBB")
"""
