# Leetcode : 1021. Remove Outermost Parentheses
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


class Solution:
    def remove_outer_parantheses(self, s: str) -> str:
        result = []  # Stores the final characters after removing outer parentheses
        depth = 0  # Tracks current nesting level of parentheses

        for ch in s:
            # If opening parenthesis is found
            if ch == "(":
                depth += 1  # Increase depth since we go one level deeper
                if depth > 1:  # Ignore the outermost '(' (depth == 1)
                    result.append(ch)

            # If closing parenthesis is found
            else:
                depth -= 1  # Decrease depth since we close a level
                if depth > 0:  # Ignore the outermost ')' (depth == 0)
                    result.append(ch)

        # Convert list of characters to string
        return "".join(result)


# Driver code
s = "(()())(())(()(()))"
obj = Solution()
print(obj.remove_outer_parantheses(s))  # output : ()()()()(())

"""
Logic : 

Problem Summary:
- The input is a valid parentheses string.
- The string is composed of multiple primitive parentheses substrings.
- A primitive substring cannot be split further into smaller valid parts.
- For each primitive substring, we must remove its outermost '(' and ')'.

Key Idea:
- Use a depth counter to track nesting levels.
- The outermost parentheses of a primitive always occur when:
  - '(' increases depth from 0 → 1
  - ')' decreases depth from 1 → 0
- These parentheses should be skipped.

How the Algorithm Works:
1. Initialize:
   - depth = 0 to track nesting
   - result list to store valid characters

2. Traverse each character in the string:
   - When '(' is encountered:
     - Increase depth
     - Append '(' only if depth > 1
       (means it's not the outermost opening parenthesis)
   - When ')' is encountered:
     - Decrease depth
     - Append ')' only if depth > 0
       (means it's not the outermost closing parenthesis)

3. Join the result list to form the final string.

Time Complexity:
- O(n), where n is the length of the string
- The string is traversed exactly once.
- Each character is processed in constant time.
- Therefore, total time complexity grows linearly with the input size.

Space Complexity:
- O(n), for storing the result
- An extra list is used to store the resulting parentheses string.
- In the worst case, almost all characters except the outermost ones are stored in the result.
- The depth variable uses constant space O(1), but overall space is dominated by the output list.
"""
