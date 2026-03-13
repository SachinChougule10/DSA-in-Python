# Leetcode : 3. Longest Substring Without Repeating Characters (Brute Force Solution)
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
        max_length = 0  # Stores the maximum length of valid substring found

        # Start index of substring
        for i in range(0, n):
            freq_list = [0] * 256  # Frequency array for ASCII characters
            curr_length = 0  # Length of current substring

            # Expand substring from index i
            for j in range(i, n):
                # If character already appeared, break (duplicate found)
                if freq_list[ord(s[j])] == 1:
                    break
                # Mark character as visited
                freq_list[ord(s[j])] += 1
                # Increase current substring length
                curr_length += 1

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
Logic Explanation (Brute Force Approach)

Goal:
Find the length of the longest substring that contains no repeating characters.

Approach:
1. Iterate through each index i of the string and assume it as the starting point of a substring.
2. For every starting index, create a frequency array of size 256 (ASCII characters).
3. Start another loop from index j = i and expand the substring character by character.
4. For every character:
   - Convert the character to its ASCII value using ord().
   - Check if it already appeared in the current substring using freq_list.
5. If the character already exists:
   - Stop expanding (break the inner loop).
6. Otherwise:
   - Mark the character as visited in freq_list.
   - Increase the current substring length.
7. After finishing the inner loop, update max_length if the current substring is longer.
8. Continue this process for every starting index.

Time Complexity:
Outer loop runs n times and inner loop can run up to n times.
Worst case: O(n²)

Space Complexity:
O(1) because the frequency array size is fixed (256).
"""
