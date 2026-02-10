# Leetcode : 14. Longest Common Prefix : Write a function to find the longest common prefix string amongst an array of strings (Brute Force Solution)
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:

        # If the input list is empty, no common prefix exists
        if not strs:
            return ""

        base = strs[0]  # Take the first string as reference
        n = len(base)
        result = ""  # Stores the common prefix

        # Iterate character by character over the base string
        for i in range(n):
            # Compare the current character with all other strings
            for word in strs:
                # If index exceeds word length or characters don't match
                if i == len(word) or word[i] != base[i]:
                    return result
            # If all strings match at index i, add character to result
            result += base[i]

        return result


# Driver code
obj = Solution()
strs1 = ["flower", "flow", "flight"]
print(obj.longest_common_prefix(strs1))  # output : fl

strs2 = ["dog", "racecar", "car"]
print(obj.longest_common_prefix(strs2))  # output : ""

"""
Logic:

Problem Summary:
- Given a list of strings, find the longest prefix that is common to all strings.
- If no common prefix exists, return an empty string.

Approach (Brute Force / Vertical Scanning):
1. If the input list is empty, return an empty string.
2. Take the first string as the reference (base string).
3. Compare each character of the base string with the character at the same index in all other strings.
4. If a mismatch is found or any string ends, stop immediately and return the prefix formed so far.
5. If all characters match, continue building the prefix.

Why this works:
- A common prefix must have the same characters at the same indices in every string.
- The moment one string fails to match, the prefix cannot grow further.

Time Complexity (TC): O(n * m)
- n = length of the shortest string
- m = number of strings
- For each character index (up to n), we compare that character with all m strings.

    Explanation:
    - The outer loop runs once for each character index (up to n).
    - The inner loop compares that character with all m strings.
    - So for:
        • 1 character → m comparisons
        • n characters → n x m comparisons
    - Therefore, total time complexity is O(n * m).

Space Complexity (SC): O(1)
- No additional data structures are used.
- Only a few variables are required to track the prefix.
- The output string does not count as extra space.

"""
