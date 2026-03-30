# Problem: Set i-th Bit (Brute Force using Binary Conversion)

# Description:
# This program sets the i-th bit (0-based index from right) of a given integer by converting the number into binary,
# modifying the required bit, and then converting it back to decimal.

# This is a brute-force approach and is less efficient compared to bitwise methods.

# Example:
# Input: n = 9 (1001), i = 2 → Output: 13 (1101)
# Input: n = 13 (1101), i = 2 → Output: 13 (1101)

# Time Complexity: O(log n)
# Space Complexity: O(log n)


class Solution:
    def set_ith_bit(self, n: int, i: int) -> int:
        # Convert integer to binary string and remove '0b' prefix
        binary = bin(n)[2:]

        # Reverse the binary string and convert it to a list
        # Reason: makes it easier to access i-th bit (LSB at index 0)
        binary = list(binary[::-1])

        # If i is greater than current length, extend the list with zeros
        # This ensures that index i exists and avoids index out-of-range error
        while len(binary) <= i:
            binary.append(0)  # note: 0 will be converted to string later

        # Set the i-th bit to '1'
        binary[i] = "1"

        # Reverse back to original order (MSB → LSB)
        binary = binary[::-1]

        # Join list into string and convert binary string to decimal
        return int("".join(binary), 2)


obj = Solution()
print(obj.set_ith_bit(9, 2))  # Output : 13
print(obj.set_ith_bit(13, 2))  # Output : 13

"""
Logic: Set i-th Bit (Brute Force)

Goal:
Set the i-th bit of a number to 1 by manipulating its binary representation.

Key Idea:
- Convert number to binary
- Modify the required bit manually
- Convert back to decimal

------------------------------------------------------------
Step-by-Step Breakdown
------------------------------------------------------------

1) Convert number to binary:
   bin(n) gives string like '0b1001'
   Remove '0b' → '1001'

2) Reverse the binary:
   '1001' → '1001' (in this case same, but important generally)
   Why?
   - Rightmost bit (LSB) becomes index 0
   - Makes indexing easier

3) Extend binary if needed:
   - If i is larger than length of binary
   - Add '0's until index i exists

   Example:
   n = 3 → '11'
   i = 4 → extend → '00011'

4) Set the i-th bit:
   - Replace binary[i] with '1'
   - Ensures that bit is set

5) Reverse back:
   - Convert from LSB-first to MSB-first

6) Convert to decimal:
   - Join list → string
   - Use int(binary_string, 2)

------------------------------------------------------------
Example Walkthrough
------------------------------------------------------------

n = 9 → binary = '1001'
i = 2

Step 1: '1001'
Step 2: reverse → '1001'
Step 3: no extension needed
Step 4: set index 2 → '1011'
Step 5: reverse → '1101'
Step 6: decimal → 13

------------------------------------------------------------
Why this is Brute Force?
------------------------------------------------------------

- Uses string conversion (extra overhead)
- Uses extra space (list)
- Multiple steps involved

Time Complexity: O(log n)
Space Complexity: O(log n)
"""
