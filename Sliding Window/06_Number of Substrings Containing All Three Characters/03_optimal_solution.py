# Leetcode : 1358. Number of Substrings Containing All Three Characters. Given a string s consisting only of characters a, b and c (Optimal Solution)
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

# Example 2:
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

# Example 3:
# Input: s = "abc"
# Output: 1

# Constraints:
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.


class Solution:
    def no_of_substrings(self, s: str) -> int:
        n = len(s)

        # Stores last seen index of 'a', 'b', 'c'
        last_seen = [-1] * 3

        # Stores total valid substrings
        count = 0

        # Traverse the string
        for i in range(n):
            # Update last seen index for current character
            last_seen[ord(s[i]) - ord("a")] = i

            # Check if all three characters have been seen at least once
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:

                # Find the smallest last seen index among 'a', 'b', 'c'
                # This gives how many valid substrings can end at index i
                count += min(last_seen[0], last_seen[1], last_seen[2]) + 1

        return count


obj = Solution()

s1 = "abcabc"
print(obj.no_of_substrings(s1))  # Output : 10

s2 = "aaacb"
print(obj.no_of_substrings(s2))  # Output : 3

s3 = "abc"
print(obj.no_of_substrings(s3))  # Output : 1

"""
Logic:

1. We track the last seen positions of 'a', 'b', and 'c' using an array.

2. For every index i:
   - Update the last seen index of the current character.

3. When all three characters have been seen:
   - Take the minimum of their last seen indices.
   - This minimum index tells how many substrings ending at i
     will contain all three characters.

4. Why +1?
   - Because substring can start from index 0 up to min_index.

5. So for each i:
   valid substrings = min(last_seen) + 1

6. Add this to total count.

Time Complexity: O(n)
Space Complexity: O(1)
"""
