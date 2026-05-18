# 859. Buddy Strings (Optimal Solution)
# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

# Constraints:
# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # lengths must be same
        if len(s) != len(goal):
            return False

        # if strings are already equal
        if s == goal:

            # duplicate character must exist
            # so swapping same characters keeps string unchanged
            return len(set(s)) < len(s)

        # store indices where characters differ
        diff = []

        # traverse both strings
        for i in range(len(s)):

            # if characters mismatch
            if s[i] != goal[i]:

                # store mismatch index
                diff.append(i)

        # exactly two mismatches are required
        if len(diff) != 2:
            return False

        # extract mismatch indices
        i, j = diff

        # check if swapping makes strings equal
        return s[i] == goal[j] and s[j] == goal[i]


# Example Usage
obj = Solution()

print(obj.buddyStrings("ab", "ba"))  # Output : True
print(obj.buddyStrings("ab", "ab"))  # Output : False
print(obj.buddyStrings("aa", "aa"))  # Output : True

"""
Logic (Optimal Approach):
1. If lengths are different, return False.
2. If strings are already equal:
   - duplicate character must exist
   because swapping identical characters keeps string unchanged.
3. Otherwise find all mismatch positions.
4. Valid buddy strings must have exactly 2 mismatches.
5. Check if swapping those two characters in s
   makes it equal to goal.

Why This Is Optimal:
- Only one traversal is needed to find mismatches.
- Avoids trying every possible swap.

Time Complexity:
O(n)

Space Complexity:
O(1)
excluding mismatch storage.
"""
