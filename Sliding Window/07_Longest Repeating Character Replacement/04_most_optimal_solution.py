# Leetcode : 424. Longest Repeating Character Replacement : You are given a string s and an integer k (Optimal Solution)
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
        # Left pointer of sliding window
        left = 0

        # Stores frequency of characters in current window
        hash_map = {}

        # Stores maximum valid substring length
        max_length = 0

        # Stores max frequency of a single character in window
        max_freq = 0

        for right in range(n):
            # Add current character to hashmap
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            # Update maximum frequency seen so far
            max_freq = max(max_freq, hash_map[s[right]])

            # If replacements needed exceed k, shrink window
            if (right - left + 1) - max_freq > k:
                # Reduce frequency of left character
                hash_map[s[left]] -= 1
                # Move left pointer
                left += 1

            # Update maximum valid window length
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
Logic (Optimal Sliding Window - Single Shrink Step):

1. Goal:
   Find the longest substring where at most k characters can be replaced
   to make all characters the same.

2. Key Formula:
   changes_needed = window_size - max_freq

3. Idea:
   - Use sliding window (left, right)
   - Expand window using 'right'
   - Track frequency of characters using hashmap
   - Keep track of max_freq (most frequent character)

4. Condition:
   - If changes_needed <= k → valid window
   - If changes_needed > k → shrink window by 1 step

5. Important Optimization:
   - Instead of shrinking in a while loop, we shrink only once (if condition)
   - This works because window grows gradually and stays near valid range

6. Why no recomputation of max_freq?
   - max_freq may be slightly outdated
   - But it never causes incorrect answer
   - It only allows slightly larger window temporarily, still safe

7. Complexity:
   - Time: O(n)
   - Space: O(26) ≈ O(1)

8. Example:
   s = "AABABBA", k = 1
   - Longest valid substring length = 4

This is the most optimized version (clean + efficient).
"""
