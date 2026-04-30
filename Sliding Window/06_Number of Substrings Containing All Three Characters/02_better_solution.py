# Leetcode : 1358. Number of Substrings Containing All Three Characters. Given a string s consisting only of characters a, b and c (Better Solution)
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
        # Length of string
        n = len(s)

        # To store total valid substrings
        count = 0

        # Iterate over all starting indices
        for i in range(n):
            # Track presence of 'a', 'b', 'c'
            hash_list = [0] * 3

            # Expand substring from i to j
            for j in range(i, n):
                # Mark current character as present
                hash_list[ord(s[j]) - ord("a")] = 1

                # If all three characters are present
                if hash_list[0] + hash_list[1] + hash_list[2] == 3:
                    #  All substrings from j to end will also be valid
                    count += n - j
                    # No need to check further for this i
                    break

        return count


obj = Solution()

s1 = "abcabc"
print(obj.no_of_substrings(s1))  # Output : 10

s2 = "aaacb"
print(obj.no_of_substrings(s2))  # Output : 3

s3 = "abc"
print(obj.no_of_substrings(s3))  # Output : 1

"""
Logic Explanation (Better Approach)

1. Use two loops:
   - Outer loop (i) represents the starting index
   - Inner loop (j) represents the ending index

2. Maintain a list of size 3 to track whether 'a', 'b', and 'c' are present.

3. As we expand the substring from i to j:
   - Mark each character as seen in hash_list.

4. Once all three characters are present:
   - Any substring starting at i and ending from j to n-1 will also contain all three characters.
   - So instead of checking each one, directly add (n - j) to the count.

5. Break the inner loop since further expansion is unnecessary.

Time Complexity:
O(n^2) in worst case, but faster than brute force due to early termination.

Space Complexity:
O(1), as only a fixed-size list is used.
"""
