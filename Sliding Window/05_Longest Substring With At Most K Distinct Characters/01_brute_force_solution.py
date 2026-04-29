# Leetcode : 340 : Longest Substring With At Most K Distinct Characters (Brute Force Solution)
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
        # Length of the string
        n = len(s)

        # Stores the maximum valid substring length
        max_length = 0

        # Outer loop: choose starting index of substring
        for i in range(n):
            # To store distinct characters in current substring
            my_set = set()

            # Inner loop: extend substring from index i
            for j in range(i, n):
                # Add current character
                my_set.add(s[j])

                # If distinct characters exceed k, stop expanding
                if len(my_set) > k:
                    break

                # Calculate current valid substring length
                curr_length = j - i + 1

                # Update maximum length
                max_length = max(max_length, curr_length)

        return max_length


obj = Solution()

s1 = "aababbcaacc"
print(obj.atmost_k(s1, 2))  # Output : 6

s2 = "abcddefg"
print(obj.atmost_k(s2, 3))  # Output : 4

"""
Logic Explanation (Brute Force Approach):

1. Goal:
   Find the length of the longest substring that contains at most k distinct characters.

2. Approach:
   - Use two nested loops to generate all possible substrings.
   - Outer loop (i): starting index of substring.
   - Inner loop (j): ending index of substring.

3. Key Idea:
   - Use a set to track distinct characters in the current substring.
   - Add characters one by one as we expand the substring.

4. Condition:
   - If the number of distinct characters becomes greater than k,
     break the inner loop (since further expansion will also be invalid).

5. Length Calculation:
   - For every valid substring (<= k distinct characters),
     calculate length = j - i + 1.
   - Update max_length if this is the longest so far.

6. Time Complexity:
   - O(n^2) → because we check all substrings.

7. Space Complexity:
   - O(k) → set stores at most k characters.

8. Example:
   s = "aababbcaacc", k = 2
   - Longest valid substring: "aababb"
   - Length = 6
"""
