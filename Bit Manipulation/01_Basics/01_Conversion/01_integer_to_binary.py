# Problem: Convert Integer to Binary

# Description:
# This program converts a given decimal (base-10) integer into its binary (base-2) representation without using any built-in conversion functions like bin().


class Solution:
    def int_to_binary(self, num: int) -> str:
        result = ""

        # Continue until the number becomes 0
        while num > 0:
            # If remainder is 1 → odd number → binary bit is '1'
            if num % 2 == 1:
                result += "1"
            else:
                result += "0"

            # Divide number by 2 (integer division)
            num //= 2

        # Reverse the result since bits are collected from LSB to MSB
        return result[::-1]


obj = Solution()

num1 = 13
print(obj.int_to_binary(num1))  # Output: 1101

num2 = 8
print(obj.int_to_binary(num2))  # Output: 1000

"""
Convert a decimal (integer) number into its binary representation.

    Approach:
    - Repeatedly divide the number by 2.
    - Store the remainder (0 or 1) at each step.
    - Append remainder to result string.
    - Reverse the result at the end since remainders are collected in reverse order.

    Time Complexity: O(log n)
    Space Complexity: O(log n)
"""
