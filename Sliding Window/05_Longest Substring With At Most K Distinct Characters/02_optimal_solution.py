# Leetcode : 340 : Longest Substring With At Most K Distinct Characters (Optimal Solution)
# Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.


# Example 1
# Input : s = "aababbcaacc" , k = 2
# Output : 6
# Explanation : The longest substring with at most two distinct characters is "aababb".
# The length of the string 6.

# Example 2
# Input : s = "abcddefg" , k = 3
# Output : 4
# Explanation : The longest substring with at most three distinct characters is "bcdd".
# The length of the string 4.


class Solution:
    def atmost_k(self, s: str, k: int) -> int:
        n = len(s)
        # Left pointer of sliding window
        left = 0
        # Stores maximum valid substring length
        max_length = 0
        # Stores frequency of characters in current window
        hash_map = {}

        # Right pointer expands the window
        for right in range(n):
            # Add current character to hashmap
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            # If distinct characters exceed k, shrink window from left
            while len(hash_map) > k:
                # Decrease frequency
                hash_map[s[left]] -= 1

                # If frequency becomes 0, remove character from map
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]

                # Move left pointer
                left += 1

            # Calculate current valid window length
            curr_length = right - left + 1

            # Update maximum length
            max_length = max(max_length, curr_length)

        return max_length


obj = Solution()

s1 = "aababbcaacc"
print(obj.atmost_k(s1, 2))  # Output : 6

s2 = "abcddefg"
print(obj.atmost_k(s2, 3))  # Output : 4


"""
Logic Explanation (Optimal Sliding Window):

1. Goal:
   Find the longest substring with at most k distinct characters.

2. Key Idea:
   Use Sliding Window (Two Pointers):
   - 'left' → start of window
   - 'right' → end of window
   - Expand window using 'right'
   - Shrink window using 'left' when invalid

3. Data Structure:
   - Use a hashmap (dictionary) to store frequency of characters
   - Helps track number of distinct characters efficiently

4. Steps:
   - Move 'right' pointer and add character to hashmap
   - If number of distinct characters > k:
        → shrink window by moving 'left'
        → decrease frequency
        → remove character if frequency becomes 0
   - At every valid step (<= k distinct), calculate window length

5. Why it works:
   - Ensures window always has at most k distinct characters
   - Maximizes window size dynamically

6. Time Complexity:
   - O(n) → each character is added and removed at most once

7. Space Complexity:
   - O(k) → hashmap stores at most k characters

8. Example:
   s = "aababbcaacc", k = 2
   - Longest substring: "aababb"
   - Length = 6
"""
