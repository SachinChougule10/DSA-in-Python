# Repeated Character - Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string (Brute Force Solution)

# NOTE - If there are no repeating characters return '#'.

# Example 1:

# Input:
# S = "geeksforgeeks"
# Output: g
# Explanation: g, e, k and s are the repeating
# characters. Out of these, g occurs first.
# Example 2:

# Input:
# S = "abcde"
# Output: -1
# Explanation: No repeating character present. (You need to return '#')

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function firstRep() which takes the string S as input and returns the the first repeating character in the string. In case there's no repeating character present, return '#'.

# Expected Time Complexity: O(|S|).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1<=|S|<=105


class Solution:
    def firstRep(self, s):

        # length of string
        n = len(s)

        # traverse every character
        for i in range(n):

            # compare current character
            # with all next characters
            for j in range(i + 1, n):

                # if repeating character found
                if s[i] == s[j]:

                    # return first repeating character
                    return s[i]

        # no repeating character found
        return "#"


# Example Usage
obj = Solution()

print(obj.firstRep("geeksforgeeks"))  # Output : g
print(obj.firstRep("abcde"))  # Output : #


"""
Logic (Brute Force Approach):
1. Traverse every character in the string.
2. For each character, compare it with all characters after it.
3. If a match is found:
   - return that character immediately
   because it is the first repeating character by position.
4. If no repeating character exists, return '#'.

Why It Is Brute Force:
- Uses nested loops for comparison.
- Every character checks remaining characters.

Time Complexity:
O(n^2)

Space Complexity:
O(1)
"""
