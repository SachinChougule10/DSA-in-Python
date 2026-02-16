# LeetCode 1614. Maximum Nesting Depth of the Parentheses (Brute Force Solution)

# Given a valid parentheses string s, return the nesting depth of s.
# The nesting depth is the maximum number of nested parentheses.
#
# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
#
# Example 2:
# Input: s = "(1)+((2))+(((3)))"
# Output: 3
#
# Example 3:
# Input: s = "()(())((()()))"
# Output: 3
#
# Constraints:
# 1 <= s.length <= 100
# s consists of digits and operators along with '(' and ')'.
# It is guaranteed that s is a valid parentheses string (VPS).


class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        max_depth = 0   # Stores maximum nesting depth found

        # Outer loop: Try starting from every index
        for i in range(n):

            # Only start calculation if we see an opening bracket
            if s[i] == "(":
                depth = 0  # Tracks nesting depth starting from index i

                # Inner loop: scan forward from current index
                for j in range(i, n):

                    # If we encounter '(', we go one level deeper
                    if s[j] == "(":
                        depth += 1
                        max_depth = max(max_depth, depth)

                    # If we encounter ')', it means
                    # we are closing one open parenthesis
                    # so we go one level up (reduce depth)
                    elif s[j] == ")":
                        depth -= 1

                        # If depth becomes 0,
                        # it means the starting '(' is fully closed
                        # so we stop scanning further
                        if depth == 0:
                            break

        return max_depth


"""
Logic Explanation (Brute Force Approach):

1. We iterate through every character in the string.
   For each index i:
   - If s[i] is '(', we attempt to calculate the nesting depth
     starting from that opening bracket.

2. For each opening bracket found:
   - Initialize depth = 0.
   - Start scanning forward using another loop.

3. Inside the inner loop:
   - If we see '(':
        → Increase depth by 1.
        → This means we go one level deeper inside nested parentheses.
        → Update max_depth accordingly.
   - If we see ')':
        → Decrease depth by 1.
        → This means we encountered a closing bracket ')'
          and we are going one level up (closing one open parenthesis).

4. If depth becomes 0:
   - It means the current starting '(' is completely closed.
   - Break out of the inner loop.

5. Repeat this process for every '(' in the string.

Why This Is Brute Force:
- For every '(', we scan forward again.
- This causes repeated scanning of overlapping regions.
- Worst case time complexity becomes O(n^2).

Time Complexity: O(n^2)
Space Complexity: O(1)
"""