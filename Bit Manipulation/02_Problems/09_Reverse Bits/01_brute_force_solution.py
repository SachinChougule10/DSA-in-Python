# Leetcode : 190. Reverse Bits (Brute Force Solution)
# Reverse bits of a given 32 bits signed integer.

# Example 1:
# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Example 2:
# Input: n = 2147483644
# Output: 1073741822
# Explanation:
# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110

# Constraints:
# 0 <= n <= 231 - 2
# n is even.

# Follow up: If this function is called many times, how would you optimize it?


class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert integer to binary string (remove '0b')
        binary = bin(n)[2:]

        # Pad with leading zeros to make it 32 bits
        binary = binary.zfill(32)

        # Reverse the binary string
        reversed_binary = binary[::-1]

        # Convert back to integer
        return int(reversed_binary, 2)


obj = Solution()

n1 = 2147483644
print(obj.reverseBits(n1))  # Output : 1073741822

n2 = 43261596
print(obj.reverseBits(n2))  # Output : 964176192

"""
LOGIC EXPLANATION (Brute Force Approach):

Goal:
------
Reverse the bits of a 32-bit integer.

Approach:
----------
Instead of manipulating bits directly, we treat the number as a string.

Steps:
-------
1. Convert integer to binary string:
   - Use bin(n) to get binary representation
   - Remove '0b' prefix using slicing [2:]

2. Ensure 32-bit representation:
   - Use zfill(32) to pad leading zeros
   - This is important because the problem requires exactly 32 bits

3. Reverse the binary string:
   - Use slicing [::-1] to reverse the string
   - This effectively reverses all bits

4. Convert reversed binary back to integer:
   - Use int(binary_string, 2)

Example:
---------
n = 5

Binary conversion:
    '101'

After padding:
    '00000000000000000000000000000101'

After reversing:
    '10100000000000000000000000000000'

Final result:
    2684354560

Time Complexity:
----------------
O(32) → O(n), where n = number of bits (constant 32)

Space Complexity:
-----------------
O(32) → Extra space used for storing binary string
"""
