# Leetcode : 20. Valid Parentheses : Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def is_valid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:
            # If character is a closing bracket
            if ch in mapping:
                # Case 1: Stack is empty → extra closing bracket
                # Case 2: Top of stack does not match expected opening bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                # If matched correctly → remove the opening bracket
                stack.pop()
            else:
                # If character is opening bracket → push to stack
                stack.append(ch)

        # If stack is empty → all brackets matched
        # If not empty → extra opening brackets
        return not stack


obj = Solution()

s1 = "()[]{}"
print(obj.is_valid(s1))  # Output : True

s2 = "([)]"
print(obj.is_valid(s2))  # Output : False

"""
Logic:
Approach: Stack-Based Matching

1. Use a stack to track opening brackets.
2. Maintain a dictionary that maps closing brackets to their corresponding opening brackets.
3. Traverse the string:
   - If an opening bracket appears → push it to stack.
   - If a closing bracket appears:
       • If stack is empty → invalid (extra closing bracket).
       • If top of stack does not match → invalid (wrong type).
       • Otherwise → pop from stack (valid match).
4. After processing all characters:
   - If stack is empty → valid string.
   - If stack still contains elements → unmatched opening brackets → invalid.

Edge Cases Covered:
✔ Extra closing bracket → ")("
✔ Wrong matching type → "(]"
✔ Wrong order nesting → "([)]"
✔ Extra opening brackets → "((("
✔ Proper nested structure → "({[]})"

Time Complexity: O(n)
    - Each character is pushed and popped at most once.

Space Complexity: O(n)
    - In worst case (all opening brackets), stack size = n.
"""
