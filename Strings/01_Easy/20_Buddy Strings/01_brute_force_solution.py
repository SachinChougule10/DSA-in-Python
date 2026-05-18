# 859. Buddy Strings (Brute Force Solution)
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

        # convert string into list
        # because strings are immutable
        s_list = list(s)

        # try every possible pair swap
        for i in range(len(s_list)):

            for j in range(i + 1, len(s_list)):

                # create copy for swapping
                temp = s_list[:]

                # swap characters
                temp[i], temp[j] = temp[j], temp[i]

                # convert back into string
                swapped = "".join(temp)

                # check if swapped string equals goal
                if swapped == goal:
                    return True

        # no valid swap found
        return False


# Example Usage
obj = Solution()

print(obj.buddyStrings("ab", "ba"))  # Output : True
print(obj.buddyStrings("ab", "ab"))  # Output : False
print(obj.buddyStrings("aa", "aa"))  # Output : True


"""
Logic (Brute Force Approach):
1. First check if lengths are same.
2. Try every possible pair swap in string s.
3. After every swap:
   - create new string
   - compare it with goal
4. If any swapped string becomes equal to goal,
   return True.
5. Otherwise return False.

Why It Is Brute Force:
- Every possible pair of characters is tested.
- Swapping and string creation happen repeatedly.

Time Complexity:
O(n^3)

Space Complexity:
O(n)
because copied list/string is created.
"""
