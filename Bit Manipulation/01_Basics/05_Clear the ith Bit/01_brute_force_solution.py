# Problem: Clear i-th Bit (Brute Force using Binary Conversion)

# Description:
# This program clears (sets to 0) the i-th bit (0-based index from right) of a given integer by converting it to binary,
# modifying the bit, and converting it back to decimal.

# If the i-th bit does not exist, the number remains unchanged.

# Example:
# Input: n = 9 (1001), i = 2 → Output: 9 (1001)
# Input: n = 13 (1101), i = 2 → Output: 9 (1001)

# Time Complexity: O(log n)
# Space Complexity: O(log n)


class Solution:
    def clear_ith_bit(self, n: int, i: int) -> int:
        # Convert integer to binary string and remove '0b' prefix
        binary = bin(n)[2:]

        # Reverse binary and convert to list
        # This makes LSB at index 0 (easy indexing)
        binary = list(binary[::-1])

        # If i-th index exists, set it to '0'
        # If it doesn't exist, do nothing
        if i < len(binary):
            binary[i] = "0"

        # Reverse back to original order (MSB → LSB)
        binary = binary[::-1]

        # Join list into string and convert binary string to decimal
        return int("".join(binary), 2)


obj = Solution()
print(obj.clear_ith_bit(9, 2))  # Output : 9
print(obj.clear_ith_bit(13, 2))  # Output : 9

"""
Logic: Clear i-th Bit (Brute Force)

Goal:
Set the i-th bit of a number to 0.

Key Idea:
- Convert number to binary
- Modify the required bit manually
- Convert back to decimal

------------------------------------------------------------
Step-by-Step Breakdown
------------------------------------------------------------

1) Convert number to binary:
   n = 13 → '1101'

2) Reverse binary:
   '1101' → '1011'
   - LSB becomes index 0 → easier access

3) Check if index exists:
   - If i < length → modify
   - Else → no change needed

4) Clear the i-th bit:
   - Set binary[i] = '0'

5) Reverse back:
   - Restore original bit order

6) Convert to decimal:
   - Join → string
   - int(string, 2)

------------------------------------------------------------
Example Walkthrough
------------------------------------------------------------

n = 13 → '1101'
i = 2

Step 1: '1101'
Step 2: reverse → '1011'
Step 3: index 2 exists
Step 4: set index 2 → '1001'
Step 5: reverse → '1001'
Step 6: decimal → 9

------------------------------------------------------------
Edge Case:
------------------------------------------------------------

n = 9 → '1001'
i = 2

- Bit at index 2 is already 0
- So number remains unchanged → 9

------------------------------------------------------------
Why this is Brute Force?
------------------------------------------------------------

- Uses string conversion
- Uses extra space (list)
- Multiple steps involved

------------------------------------------------------------
Time Complexity: O(log n)
Space Complexity: O(log n)
"""
