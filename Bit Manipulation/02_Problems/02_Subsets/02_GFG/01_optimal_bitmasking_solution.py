# GFG : Power Set (Optimal Solution)
# Given a string s of length n, find all the possible non-empty subsequences of the string s in lexicographically-sorted order.

# Example 1:
# Input :
# s = "abc"
# Output:
# a ab abc ac b bc c
# Explanation :
# There are a total 7 number of subsequences possible for the given string, and they are mentioned above in lexicographically sorted order.

# Example 2:
# Input:
# s = "aa"
# Output:
# a a aa
# Explanation :
# There are a total 3 number of subsequences possible for the given string, and they are mentioned above in lexicographically sorted order.

# Expected Time Complexity: O( n*2n  )
# Expected Space Complexity: O( n * 2n )

# Constraints:
# 1 <= n <= 16
# s constitutes of lower case english alphabets


class Solution:
    def all_possible_strings(self, s: str):
        # Length of the string
        n = len(s)

        # Total subsets = 2^n
        no_of_subsets = 1 << n

        # To store all subsequences
        result = []

        # Loop from 1 to (2^n - 1) to avoid empty subset
        for ch in range(1, no_of_subsets):
            subset = ""  # Store current subsequence

            # Check each bit position
            for i in range(n):
                # If ith bit is set, include s[i]
                if ch & (1 << i):
                    subset += s[i]

            # Add subsequence to result
            result.append(subset)

        result.sort()  # Sort lexicographically
        return result


obj = Solution()
s = "abc"
print(obj.all_possible_strings(s))  # ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']

"""
Logic Explanation:

1. Total Subsequences:
   - For a string of length n, total possible subsequences = 2^n.
   - Each subsequence corresponds to a binary number from 0 to (2^n - 1).

2. Bitmasking Idea:
   - Treat each number as a bitmask.
   - Example for "abc" (n = 3):
        1 (001) -> "a"
        2 (010) -> "b"
        3 (011) -> "ab"
        4 (100) -> "c"
        5 (101) -> "ac"
        6 (110) -> "bc"
        7 (111) -> "abc"

   - If ith bit is set → include s[i] in subsequence.

3. Why start from 1?
   - 0 (000) represents empty subsequence.
   - Problem asks for non-empty subsequences, so skip 0.

4. Sorting:
   - After generating all subsequences, sort them lexicographically.

5. Complexity:
   - Time: O(n * 2^n)
   - Space: O(n * 2^n)

This is an optimal approach using bit manipulation for generating power set.
"""
