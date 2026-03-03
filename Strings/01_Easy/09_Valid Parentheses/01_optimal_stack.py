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
        stack = []

        for ch in s:
            # If opening bracket, push its corresponding closing bracket
            if ch == "(":
                stack.append(")")
            elif ch == "{":
                stack.append("}")
            elif ch == "[":
                stack.append("]")

            # If closing bracket, check for validity
            elif not stack or stack.pop() != ch:
                # Case 1: stack empty → extra closing bracket
                # Case 2: mismatch → wrong bracket type
                return False

        # If stack is empty → all brackets matched correctly
        return len(stack) == 0


obj = Solution()

s1 = "()[]{}"
print(obj.is_valid(s1))  # Output : True

s2 = "([)]"
print(obj.is_valid(s2))  # Output : False


"""
Logic:

Algorithm Intuition:

1. Opening brackets are stored in a stack.
2. Instead of pushing the opening bracket, we push the expected closing bracket.
3. When we encounter a closing bracket:
   - It must match the top of the stack.
   - Otherwise, the string is invalid.
4. After processing all characters:
   - If stack is empty → valid.
   - If stack still has elements → unmatched opening brackets → invalid.

Edge Cases Handled:
✔ Extra closing bracket → ")("
✔ Wrong matching order → "([)]"
✔ Extra opening bracket → "((("
✔ Proper nested structure → "({[]})"

Example Dry Run:
Input: "([)]"

Stack progression:
'(' → push ')'
'[' → push ']'
')' → expected ']' → mismatch → return False

Final Result: False
"""
