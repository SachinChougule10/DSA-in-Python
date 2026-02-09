# Leetcode : 1903. Largest Odd Number in String : You are given a string num, representing a large integer.
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.


class Solution:
    def largest_odd_number(self, num: str) -> str:
        n = len(num)  # Length of the string

        # Traverse the string from right to left
        for i in range(n - 1, -1, -1):
            # Check if the current digit is odd
            if int(num[i]) % 2 == 1:
                # Return substring from start till this index (inclusive)
                return num[0 : i + 1]

        # If no odd digit is found
        return ""


# Driver code
obj = Solution()

num1 = "35427"
print(obj.largest_odd_number(num1))  # output : 35427

num2 = "4206"
print(obj.largest_odd_number(num2))  # output : ""

num3 = "252958888"
print(obj.largest_odd_number(num3))  # output : 25295


"""
Logic:

Why do we traverse from right to left?
- A number is odd only if its last digit is odd.
- To get the largest possible odd number, we must keep as many digits as possible.
- The rightmost odd digit allows us to keep the maximum prefix.
- Any digit after this position would make the number even.

Full Logic:
1. Traverse the string from the last character to the first.
2. Check each digit to see if it is odd.
3. When an odd digit is found:
   - Return the substring from index 0 to that position (inclusive).
4. This substring represents the largest-valued odd number.
5. If no odd digit is found, return an empty string.

Time Complexity (TC): O(n)
- The string is scanned once from right to left.

Space Complexity (SC): O(1)
- No extra space is used apart from variables.
- The returned substring is part of the original input.
"""
