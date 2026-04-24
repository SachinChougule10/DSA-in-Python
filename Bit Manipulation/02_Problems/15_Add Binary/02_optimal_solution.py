# LeetCode : 67. Add Binary (Optimal Solution)
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1  # pointer starting from end of string a
        j = len(b) - 1  # pointer starting from end of string b
        carry = 0  # stores carry from previous addition
        result = []  # to store result bits (in reverse order)

        # Loop runs until all digits and carry are processed
        while i >= 0 or j >= 0 or carry:
            total = carry  # start with carry

            # Add current bit from a if available
            if i >= 0:
                total += int(a[i])
                i -= 1

            # Add current bit from b if available
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Current bit = remainder when divided by 2
            result.append(str(total % 2))

            # Carry = quotient when divided by 2
            carry = total // 2

        # Reverse result because we built it from LSB → MSB
        return "".join(result[::-1])


obj = Solution()

a1 = "11"
b1 = "1"
print(obj.add_binary(a1, b1))  # Output : 100

a2 = "1010"
b2 = "1011"
print(obj.add_binary(a2, b2))  # Output : 10101

"""
LOGIC (Optimal Solution - Binary Addition):

1. We simulate binary addition similar to decimal addition.
2. Start from the rightmost digits of both strings.
3. Maintain a carry variable initialized to 0.
4. Loop until:
   - both strings are fully traversed AND
   - no carry remains

5. At each step:
   - Add current digits from both strings (if available) + carry
   - Current result bit = total % 2
   - Update carry = total // 2

6. Append result bits in reverse order (LSB to MSB).
7. Reverse the result at the end to get final binary string.

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
"""
