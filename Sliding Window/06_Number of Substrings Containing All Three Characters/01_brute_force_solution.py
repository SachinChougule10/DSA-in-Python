# Leetcode : 1358. Number of Substrings Containing All Three Characters. Given a string s consisting only of characters a, b and c (Brute Force Solution)
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
        # Length of the string
        n = len(s)

        # To store total valid substrings
        count = 0

        # Iterate over all possible starting points
        for i in range(n):
            # Track presence of 'a', 'b', 'c'
            hash_list = [0] * 3

            # Expand substring from index i to j
            for j in range(i, n):
                # Mark current character as seen
                hash_list[ord(s[j]) - ord("a")] = 1

                # Check if all three characters are present
                if hash_list[0] + hash_list[1] + hash_list[2] == 3:
                    # Valid substring found
                    count += 1

        return count


obj = Solution()

s1 = "abcabc"
print(obj.no_of_substrings(s1))  # Output : 10

s2 = "aaacb"
print(obj.no_of_substrings(s2))  # Output : 3

s3 = "abc"
print(obj.no_of_substrings(s3))  # Output : 1

"""
Logic Explanation (Brute Force Approach)

1. We generate all possible substrings using two loops:
   - Outer loop (i) → starting index
   - Inner loop (j) → ending index

2. For each substring s[i:j], we track whether:
   - 'a' is present → hash_list[0]
   - 'b' is present → hash_list[1]
   - 'c' is present → hash_list[2]

3. We use a list of size 3 initialized with 0:
   hash_list = [0, 0, 0]

4. While expanding the substring:
   - We mark the character as present using:
     hash_list[ord(s[j]) - ord('a')] = 1

5. If sum of hash_list becomes 3:
   → It means 'a', 'b', and 'c' are all present
   → So this substring is valid
   → Increment count

6. Continue checking all substrings.

Time Complexity:
    O(n^2) → Checking all substrings

Space Complexity:
   O(1) → Only a fixed size list of 3 elements used

Note:
This is a brute force solution. It works fine for small inputs but is not optimal.
An optimized Sliding Window solution can reduce time complexity to O(n).
"""
