# Problem: Binary to Decimal Conversion + Common Bit Tricks

# Description:
# This program converts a binary (base-2) string into its decimal (base-10) equivalent using a manual approach (without using built-in functions).

# It also includes commonly used bit manipulation tricks useful in competitive programming.


class Solution:
    def binary_to_decimal(self, s: str) -> int:
        # Edge case: if input is "0"
        if s == "0":
            return 0

        num = 0
        power = 0

        # Traverse from right to left (LSB to MSB)
        for index in range(len(s) - 1, -1, -1):
            # Convert character to int and multiply with 2^power
            num += int(s[index]) * 2**power

            # Increase power for next bit
            power += 1

        return num


obj = Solution()

dec1 = "1101"
print(obj.binary_to_decimal(dec1))  # Output: 13

dec2 = "1000"
print(obj.binary_to_decimal(dec2))  # Output: 8

"""
Approach (Binary to Decimal):
- Traverse the binary string from right to left (Least Significant Bit to Most Significant Bit).
- Each bit contributes a value based on its position (power of 2).
- Multiply each bit with 2^power and add to the result.
- Increment power at each step.

Example:
Input: "1101"
= 1*(2^3) + 1*(2^2) + 0*(2^1) + 1*(2^0)
= 8 + 4 + 0 + 1 = 13

Input: "1000"
= 1*(2^3) = 8

Time Complexity: O(n)
Space Complexity: O(1)

------------------------------------------------------------
Common Bit Tricks Used in Competitive Programming
------------------------------------------------------------

1) Check if number is odd
   Expression: n & 1

   Logic:
   - The last bit (Least Significant Bit) determines odd/even.
   - If last bit = 1 → number is odd
   - If last bit = 0 → number is even

   Example:
   5 → 101 → 5 & 1 = 1 (odd)
   6 → 110 → 6 & 1 = 0 (even)

------------------------------------------------------------

2) Divide by 2
   Expression: n >> 1

   Logic:
   - Right shift removes the last bit of the number.
   - This is equivalent to integer division by 2.

   Example:
   10 → 1010 → 0101 → 5

------------------------------------------------------------

3) Find mid in Binary Search
   Expression: (low + high) >> 1

   Logic:
   - Same as (low + high) // 2
   - Uses bit operation, slightly faster

   Better Version (avoids overflow):
   low + ((high - low) >> 1)
"""
