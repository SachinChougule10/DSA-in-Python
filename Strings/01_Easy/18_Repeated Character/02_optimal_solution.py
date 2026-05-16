# Repeated Character - Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string (Optimal Solution)

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

        # dictionary to store frequency
        freq = {}

        # count frequency of every character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # traverse string again
        # to find first repeating character
        for ch in s:

            # if frequency is greater than 1
            if freq[ch] > 1:

                # return first repeating character
                return ch

        # no repeating character found
        return "#"


# Example Usage
obj = Solution()

print(obj.firstRep("geeksforgeeks"))  # Output : g
print(obj.firstRep("abcde"))  # Output : #

"""
Logic (Optimal HashMap Approach):
1. Create a hashmap to store frequency of characters.
2. Traverse the string and count frequency of every character.
3. Traverse the string again:
   - if frequency of character is greater than 1,
     return that character immediately.
4. If no repeating character exists, return '#'.

Why This Is Optimal:
- Frequency lookup in hashmap works in O(1).
- Avoids repeated comparisons using nested loops.

Time Complexity:
O(n)

Space Complexity:
O(n)
for hashmap storage.
"""
