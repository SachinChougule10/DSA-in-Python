# GFG : Meta Strings (Optimal Solution)
# Given two strings s1 and s2 consisting of lowercase english alphabets, check whether these strings are meta strings or not.
# Note: Meta strings are the strings which can be made equal by exactly one swap in any of the strings. Equal string are not considered here as Meta strings.

# Examples:

# Input: s1 = "geeks", s2 = "keegs"
# Output: true
# Explanation: We can swap the 0th and 3rd character of s2 to make it equal to s1.

# Input: s1 = "geeks", s2 = "geeks"
# Output: false
# Explanation: Equal strings are not considered Meta strings.

# Input: s1 = "a", s2 = "b"
# Output: false
# Explanation: Since there is only character, we cannot do any swap.

# Constraints:
# 1 ≤ |s1|, |s2| ≤ 105

# GeeksForGeeks : Meta Strings (Brute Force Solution)


class Solution:
    def meta_strings(self, s1: str, s2: str) -> bool:

        # lengths must be same
        if len(s1) != len(s2):
            return False

        # equal strings are not meta strings
        if s1 == s2:
            return False

        # store mismatch indices
        diff = []

        # traverse both strings
        for i in range(len(s1)):

            # if characters mismatch
            if s1[i] != s2[i]:

                # store mismatch index
                diff.append(i)

        # exactly two mismatches required
        if len(diff) != 2:
            return False

        # extract mismatch positions
        i, j = diff

        # check if swapping works
        return s1[i] == s2[j] and s1[j] == s2[i]


# Example Usage
obj = Solution()

print(obj.meta_strings("geeks", "keegs"))  # Output : True
print(obj.meta_strings("geeks", "geeks"))  # Output : False
print(obj.meta_strings("a", "b"))  # Output : False

"""
Logic (Optimal Approach):
1. If lengths are different, return False.
2. If strings are already equal,
   return False because equal strings are not considered meta strings.
3. Traverse both strings and store mismatch positions.
4. Valid meta strings must have exactly 2 mismatches.
5. Check if swapping those two characters
   makes both strings equal.

Why This Is Optimal:
- Only one traversal is required.
- Avoids checking all possible swaps.

Time Complexity:
O(n)

Space Complexity:
O(1)
excluding mismatch storage.
"""
