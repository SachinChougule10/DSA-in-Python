# GeeksForGeeks : Longest Substring with K Uniques. You are given a string s consisting only lowercase alphabets and an integer k (Optimal Solution)
# Your task is to find the length of the longest substring that contains exactly k distinct characters.

# Note : If no such substring exists, return -1.

# Examples:

# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

# Input: s = "aaaa", k = 2
# Output: -1
# Explanation: There's no substring with 2 distinct characters.

# Input: s = "aabaaab", k = 2
# Output: 7
# Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.

# Constraints:
# 1 ≤ s.size() ≤ 105
# 1 ≤ k ≤ 26


class Solution:
    def longest_k_substr(self, s, k):
        n = len(s)
        # left pointer of window
        left = 0

        # frequency map to store count of characters
        hash_map = {}

        # stores final answer
        max_length = -1

        # right pointer expands the window
        for right in range(n):
            # Add current character to hashmap
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            # If distinct characters exceed k → shrink window
            while len(hash_map) > k:
                hash_map[s[left]] -= 1  # decrease frequency

                # If frequency becomes 0 → remove from map
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left += 1  # move left pointer forward

            # If window has exactly k distinct characters → update answer
            if len(hash_map) == k:
                curr_length = right - left + 1
                max_length = max(max_length, curr_length)

        return max_length


obj = Solution()

s1 = "aabacbebebe"
print(obj.longest_k_substr(s1, 3))  # Output : 7

s2 = "aaaa"
print(obj.longest_k_substr(s2, 2))  # Output : -1


"""
LOGIC (Optimal Sliding Window Approach):

1. Use two pointers:
   - left → start of window
   - right → end of window

2. Use a hashmap (frequency map):
   - Stores count of characters in current window
   - Number of keys = number of distinct characters

3. Expand window:
   - Move right pointer forward
   - Add s[right] to hashmap

4. Shrink window when invalid:
   - If distinct characters > k:
     → Move left pointer forward
     → Decrease frequency of s[left]
     → Remove character if its count becomes 0

5. Valid condition:
   - When len(hash_map) == k:
     → Window has exactly k distinct characters
     → Calculate length (right - left + 1)
     → Update max_length

6. Continue until entire string is processed

7. Return max_length
   - If no valid substring found → returns -1


TIME COMPLEXITY:
- O(n) → Each element is processed at most twice

SPACE COMPLEXITY:
- O(k) → Hashmap stores at most k characters


IMPORTANT SLIDING WINDOW PATTERN

There are 3 common variations:

1. At most K distinct
   while len(freq) > k:
       shrink window
   → Update answer every time

2. Exactly K distinct
   while len(freq) > k:
       shrink window
   if len(freq) == k:
       update answer

3. Number of substrings with exactly K distinct
   → Use:
     atMostK(k) - atMostK(k-1)
   (very common interview trick)


CORE CONCEPT

We maintain:
→ Window always has ≤ k distinct characters

But we update answer only when:
→ Window has exactly k distinct characters

So:

Condition        Meaning
--------------------------------
> k              Invalid → shrink window
== k             Valid → update answer
< k              Not valid yet → keep expanding
"""
