# Problem - Remove Last Set Bit (Using Bit Manipualtion)

# Description:
# This function removes the rightmost set bit (1) from a given integer.
# It uses the bit manipulation trick: n & (n - 1).

# A set bit refers to a bit with value 1 in the binary representation.

# Key Idea:
# - Subtracting 1 from n flips the rightmost 1 to 0
#   and all bits to its right become 1.
# - Performing AND with the original number removes that rightmost 1.

# Example:
# n = 40 (101000) → result = 32 (100000)
# n = 84 (1010100) → result = 80 (1010000)


class Solution:
    def remove_last_set_bit(self, n: int):
        return n & (n - 1)  # AND with (n-1) removes the rightmost set bit


obj = Solution()
print(obj.remove_last_set_bit(40))  # Output : 32
print(obj.remove_last_set_bit(84))  # Output : 80

# n - 1 → flips the rightmost 1 to 0 and all bits after it to 1
# n & (n - 1) → removes that rightmost 1

"""
Logic Explanation:

Step 1: Compute (n - 1)
- This flips the rightmost set bit (1 → 0)
- All bits after it become 1

Step 2: Perform bitwise AND with original number
- n & (n - 1) removes the rightmost set bit
- Only common bits between both numbers remain

Key Insight:
- Each application of (n & (n - 1)) removes exactly one set bit

Time Complexity:
- O(1) for a single operation

Use Cases:
- Counting set bits efficiently (Brian Kernighan’s Algorithm)
- Checking if a number is a power of 2
- Bitmasking problems in DSA
"""
