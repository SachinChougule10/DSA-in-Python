# Leetcode : 3. Longest Substring Without Repeating Characters (Optimal Solution)
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # Stores the maximum length of substring without repeating characters
        max_length = 0
        l = 0  # Left pointer of sliding window
        last_seen = {}  # Dictionary to store last index where each character appeared

        # Right pointer expands the sliding window
        for r in range(n):

            # If character already exists in the current window
            if s[r] in last_seen and last_seen[s[r]] >= l:
                # Move left pointer to one position after the previous occurrence
                l = last_seen[s[r]] + 1

            # Update the last seen index of the current character
            last_seen[s[r]] = r

            # Calculate current window length
            curr_length = r - l + 1

            # Update maximum length found so far
            max_length = max(max_length, curr_length)

        return max_length


obj = Solution()

s1 = "abcabcbb"
print(obj.lengthOfLongestSubstring(s1))  # Output : 3

s2 = "bbbbb"
print(obj.lengthOfLongestSubstring(s2))  # Output : 1

s3 = "abcdefgh"
print(obj.lengthOfLongestSubstring(s3))  # Output : 8

"""
Logic Explanation (Optimal Sliding Window Approach)

Goal:
Find the length of the longest substring without repeating characters.

Approach:
1. Use the Sliding Window technique with two pointers:
   - l (left pointer)
   - r (right pointer)

2. Expand the window by moving r one step at a time.

3. Maintain a dictionary (last_seen) that stores the last index where each character appeared.

4. When a duplicate character is encountered:
   - Check if the previous occurrence is inside the current window.
   - If yes, move the left pointer to last_seen[char] + 1 to remove the duplicate.

5. Update the last seen position of the current character.

6. Compute the current window length:
      length = r - l + 1

7. Update max_length if the current window is longer.

Example (s = "abcabcbb"):
Window expands until duplicate 'a' appears. Then left pointer jumps forward to remove duplicate.

Time Complexity:
O(n) → Each character is processed at most once.

Space Complexity:
O(min(n, charset)) → Dictionary stores characters and their last positions.
"""
