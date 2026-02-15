# Leetcode : 796. Rotate String : Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s (Brute Force Solution)
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
        # If lengths are different, rotation is impossible
        if len(s) != len(goal):
            return False

        # Copy original string
        my_str = s

        # Try all possible rotations (at most len(s) times)
        for i in range(len(s)):
            # If current rotated string equals goal → return True
            if my_str == goal:
                return True
            # Perform one left rotation: Remove first character and append it at the end
            my_str = my_str[1:] + my_str[0]

        # If no rotation matched goal
        return False


obj = Solution()

s1, goal1 = "abcde", "cdeab"
print(obj.rotate_string(s1, goal1))  # output : True

s2, goal2 = "abcde", "abced"
print(obj.rotate_string(s2, goal2))  # output : False

"""
Logic:

1. If lengths of s and goal are different, return False immediately.
   (Rotation does not change string length.)

2. Create a temporary string 'my_str' initialized to s.

3. Perform at most len(s) rotations:
   - Check if current string equals goal.
     If yes → return True.
   - Otherwise, rotate left by one position:
       my_str = my_str[1:] + my_str[0]

4. If after all rotations no match is found, return False.

Time Complexity: O(n^2)
- We rotate n times.
- Each rotation takes O(n) due to slicing.

Space Complexity: O(n)
- Because slicing creates a new string.
"""
