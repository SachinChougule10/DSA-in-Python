# Leetcode : 14. Longest Common Prefix : Write a function to find the longest common prefix string amongst an array of strings (Vertical Scan)
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:

        # If the list is empty, no common prefix exists
        if not strs:
            return ""

        # This will store our final longest common prefix
        result = ""

        # zip(*strs) groups characters column-wise.
        # Example:
        # ["flower", "flow", "flight"]
        # becomes:
        # ('f','f','f'), ('l','l','l'), ('o','o','i'), ...
        # It automatically stops at the shortest string length.
        for ch in zip(*strs):
            # Convert tuple to set to remove duplicates.
            # If all characters are same, set length will be 1.
            if len(set(ch)) == 1:
                result += ch[0]
            else:
                # len(set(ch)) != 1
                # That means there are different characters in this column (more than one unique element).
                # Since prefix must be continuous from index 0, we stop immediately.
                break

        return result


# Driver code
obj = Solution()
strs1 = ["flower", "flow", "flight"]
print(obj.longest_common_prefix(strs1))  # output : fl

strs2 = ["dog", "racecar", "car"]
print(obj.longest_common_prefix(strs2))  # output : ""

"""
Logic:

This solution uses the Vertical Scanning approach.

1. zip(*strs) groups characters index-wise (column-wise).
   Example:
   ["flower", "flow", "flight"]
   → ('f','f','f'), ('l','l','l'), ('o','o','i'), ...

2. For each column:
   - Convert it to a set.
   - If set size == 1 → all characters are same → add to result.
   - If set size != 1 → characters differ → stop immediately.

3. The longest common prefix must start from index 0and be continuous. The moment we find different characters,
   the prefix ends.

4. zip() automatically stops at the shortest string, preventing index-out-of-range errors.

Time Complexity:
O(N x M)
N = number of strings
M = length of shortest string

Space Complexity:
O(1) (excluding output string)

Approach Name: Vertical Scanning
"""
