# Problem: Toggle i-th Bit (Brute Force Approach)

# Description:
# This program toggles (flips) the i-th bit (0-based index from right)
# of a given integer by converting it into a binary string.

# If the bit is 0 → it becomes 1
# If the bit is 1 → it becomes 0

# If the i-th position does not exist, the binary is extended and the bit is set to 1.

# Example:
# Input: n = 9 (1001), i = 2 → Output: 13 (1101)
# Input: n = 13 (1101), i = 2 → Output: 9 (1001)


class Solution:
    def toggle_ith_bit(self, n: int, i: int):
        # Convert integer to binary string and remove '0b' prefix
        binary = bin(n)[2:]

        # Reverse binary string and convert to list
        # Reason: makes indexing easier (LSB at index 0)
        binary = list(binary[::-1])

        # If i-th index exists, toggle the bit
        if i < len(binary):
            if binary[i] == "0":
                binary[i] = "1"  # Change 0 → 1
            else:
                binary[i] = "0"  # Change 1 → 0
        else:
            # If i-th index does not exist, extend the binary
            while len(binary) <= i:
                binary.append("0")  # Append zeros
            binary[i] = "1"  # Set the i-th bit to 1

        # Reverse back to original order and join into string
        binary = "".join(binary[::-1])

        # Convert binary string back to integer
        return int(binary, 2)


obj = Solution()
print(obj.toggle_ith_bit(9, 2))  # Output: 13
print(obj.toggle_ith_bit(13, 2))  # Output: 9

"""
Logic Explanation:

1. Convert to Binary:
   Convert the number into a binary string and remove the '0b' prefix.

2. Reverse for Easy Indexing:
   Reverse the binary string so that the least significant bit (LSB)
   comes at index 0. This makes accessing the i-th bit straightforward.

3. Toggle the Bit:
   - If the i-th index exists:
       Flip the bit manually:
       0 → 1
       1 → 0
   - If the i-th index does not exist:
       Extend the binary with zeros until that position is reached,
       then set that bit to 1.

4. Restore Original Order:
   Reverse the binary string back to its original form.

5. Convert Back to Integer:
   Convert the modified binary string into an integer.

Time Complexity: O(k), where k = number of bits in n
Space Complexity: O(k)
"""
