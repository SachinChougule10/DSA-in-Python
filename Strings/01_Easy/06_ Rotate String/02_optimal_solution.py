# Leetcode : 796. Rotate String : Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s (Optimal Solution)
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false


class Solution:
    def rotate_string(self, s: str, goal: str) -> bool:
        # If lengths are not equal, rotation is impossible
        if len(s) != len(goal):
            return False

        # Concatenate string with itself
        # All possible rotations of s will exist inside s + s
        double_s = s + s

        # Check if goal is a substring of double_s
        # If yes, goal is a valid rotation of s
        if goal in double_s:
            return True
        return False


obj = Solution()

s1, goal1 = "abcde", "cdeab"
print(obj.rotate_string(s1, goal1))  # output : True

s2, goal2 = "abcde", "abced"
print(obj.rotate_string(s2, goal2))  # output : False

"""
Approach: Optimal Solution using String Concatenation

Key Idea:
If a string s is rotated, the result will always be a substring of s + s.

Example:
s = "abcde"
s + s = "abcdeabcde"

All rotations:
"abcde"
"bcdea"
"cdeab"
"deabc"
"eabcd"

All of these appear inside "abcdeabcde".

Steps:
1. If lengths of s and goal are different → return False.
2. Create double_s = s + s.
3. Check if goal exists inside double_s.
   - If yes → return True.
   - Otherwise → return False.

Time Complexity: O(n)
- Concatenation takes O(n).
- Substring search takes O(n).

Space Complexity: O(n)
- Because of creating s + s.
"""
