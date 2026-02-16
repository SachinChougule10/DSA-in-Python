# LeetCode 1614 : Maximum Nesting Depth of the Parentheses
#
# Given a valid parentheses string s, return the nesting depth of s.
# The nesting depth is the maximum number of nested parentheses.
#
# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
#
# Example 2:
# Input: s = "()(())((()()))"
# Output: 3
#
# Constraints:
# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that s is a valid parentheses string (VPS).


class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0   # Tracks how many parentheses are currently open
        max_depth = 0       # Stores the maximum nesting depth found
        
        # Traverse each character in the string
        for ch in s:
            
            # If we see an opening bracket '(',
            # we go one level deeper (increase nesting)
            if ch == "(":
                current_depth += 1
                
                # Update max_depth if current depth is greater
                max_depth = max(max_depth, current_depth)
            
            # If we see a closing bracket ')',
            # it means we are closing one open parenthesis
            # so we go one level up (decrease nesting level)
            elif ch == ")":
                current_depth -= 1
        
        # Return the maximum nesting depth encountered
        return max_depth


"""
Logic Explanation:

1. Initialize two variables:
   - current_depth → keeps track of how many '(' brackets are currently open.
   - max_depth → stores the maximum nesting level reached.

2. Traverse each character in the string:
   - If the character is '(':
        → Increase current_depth by 1.
        → This means we go one level deeper inside nested parentheses.
        → Update max_depth if needed.
   
   - If the character is ')':
        → Decrease current_depth by 1.
        → This means we encountered a closing bracket ')'
          and we are closing one open parenthesis.
        → So we go one level up (reduce nesting level).

   - Ignore digits and operators.

3. Since the string is guaranteed to be valid (VPS),
   we do not need to handle invalid cases.

4. The highest value reached by current_depth
   during traversal is the maximum nesting depth.

Time Complexity: O(n)
Space Complexity: O(1)
"""