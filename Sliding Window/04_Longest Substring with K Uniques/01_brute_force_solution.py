# GeeksForGeeks : Longest Substring with K Uniques. You are given a string s consisting only lowercase alphabets and an integer k (Brute Force Solution)
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
        # stores the answer (default = -1 if not found)
        max_length = -1

        # Outer loop → starting index of substring
        for i in range(n):
            # to store unique characters in current substring
            my_set = set()

            # Inner loop → ending index of substring
            for j in range(i, n):
                # add current character
                my_set.add(s[j])

                # If unique characters exceed k → stop expanding this substring
                if len(my_set) > k:
                    break

                # If exactly k unique characters → update max length
                if len(my_set) == k:
                    curr_length = j - i + 1
                    max_length = max(max_length, curr_length)

        return max_length


obj = Solution()

s1 = "aabacbebebe"
print(obj.longest_k_substr(s1, 3))  # Output : 7

s2 = "aaaa"
print(obj.longest_k_substr(s2, 2))  # Output : -1

"""
LOGIC (Brute Force Approach):

1. We generate all possible substrings using two loops:
   - Outer loop (i) → starting index
   - Inner loop (j) → ending index

2. For each substring s[i:j+1]:
   - Maintain a set (my_set) to track unique characters.

3. While expanding substring:
   - Add current character s[j] to set.

4. Cases:
   a) If number of unique characters > k:
      → Break (no need to expand further, it will only increase)

   b) If number of unique characters == k:
      → Calculate substring length = (j - i + 1)
      → Update max_length

5. After checking all substrings:
   - Return max_length
   - If no valid substring found → return -1


TIME COMPLEXITY:
- O(n^2) → Two nested loops
- Set operations are O(1) average

SPACE COMPLEXITY:
- O(k) → Set stores at most k characters
"""
