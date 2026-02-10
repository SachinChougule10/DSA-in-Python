# Leetcode : 14. Longest Common Prefix : Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:

        # If the list is empty, no common prefix exists
        if not strs:
            return ""

        # Sort the list of strings lexicographically
        strs.sort()

        result = []  # To store the common prefix characters
        first = strs[0]  # First string after sorting
        last = strs[-1]  # Last string after sorting

        # Compare characters of first and last string
        for i in range(0, len(first)):
            if first[i] != last[i]:
                break
            result.append(first[i])

        # Convert list of characters to string
        return "".join(result)


# Driver code
obj = Solution()
strs1 = ["flower", "flow", "flight"]
print(obj.longest_common_prefix(strs1))  # output : fl

strs2 = ["dog", "racecar", "car"]
print(obj.longest_common_prefix(strs2))  # output : ""

"""
Logic:

Why Sorting Works:
- When strings are sorted lexicographically, strings with similar prefixes come closer together.
- The longest common prefix of the entire array must be the common prefix between the first and last strings after sorting.
- Any mismatch between these two means the prefix cannot exist in the strings between them.

Full Logic:
1. If the list is empty, return an empty string.
2. Sort the array of strings.
3. Take the first and last strings from the sorted list.
4. Compare characters at the same index in both strings.
5. Keep adding characters while they match.
6. Stop at the first mismatch and return the prefix formed.

Time Complexity (TC): O(n log n)
- Sorting m strings takes O(m log m).
- Comparing first and last strings takes O(n),
  where n is the length of the shortest string.
- Overall complexity is dominated by sorting: O(m log m).

Space Complexity (SC): O(1)
- No extra data structures are used.
- Sorting is done in-place (Python uses Timsort).
- Only a few variables are used for comparison.
"""
