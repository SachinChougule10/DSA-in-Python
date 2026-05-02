# Leetcode : 424. Longest Repeating Character Replacement : You are given a string s and an integer k (Better Solution)
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
        left = 0  # Left pointer of sliding window
        hash_map = {}  # Stores frequency of characters in current window
        max_length = 0  # Stores maximum valid substring length
        max_freq = 0  # Stores frequency of most frequent character in window

        for right in range(n):
            # Add current character to hashmap
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            # Update max frequency of any character in current window
            max_freq = max(max_freq, hash_map[s[right]])

            # If replacements needed > k, shrink window
            while (right - left + 1) - max_freq > k:
                # Reduce frequency of left character
                hash_map[s[left]] -= 1

                # Recalculate max_freq after shrinking (costly step)
                max_freq = max(hash_map.values())

                # Move left pointer
                left += 1

            # Update maximum valid window size
            max_length = max(max_length, right - left + 1)

        return max_length


obj = Solution()

s1 = "AABABBA"
k1 = 1
print(obj.characterReplacement(s1, k1))  # Output: 4

s2 = "ABAB"
k2 = 2
print(obj.characterReplacement(s2, k2))  # Output: 4


"""
Logic (Better Sliding Window Approach):

1. Goal:
   Find the longest substring where at most k characters can be replaced
   to make all characters the same.

2. Key Idea:
   Use sliding window + track most frequent character.

3. Important Formula:
   changes_needed = window_size - max_freq

   - window_size = right - left + 1
   - max_freq = frequency of most repeating character

4. Condition:
   - If changes_needed <= k → valid window
   - If changes_needed > k → shrink window from left

5. Steps:
   - Expand window using 'right'
   - Update frequency map
   - Track max_freq
   - If invalid, shrink window using 'left'
   - Update answer at each valid step

6. Why recalculate max_freq?
   - When shrinking, previous max_freq may become invalid
   - So we recompute using max(hash_map.values())

7. Complexity:
   - Time: O(26 * n) ≈ O(n)
   - Space: O(26) ≈ O(1)

8. Example:
   s = "AABABBA", k = 1
   - Longest valid substring length = 4

"""
