# Problem - Remove Last Set Bit (Brute Force Solution)

# Description:
# This brute force approach removes the rightmost set bit (1) from a number.
# It converts the number to binary, finds the first '1' from the right (LSB),
# changes it to '0', and converts the result back to an integer.

# Example:
# n = 40 (101000) → result = 32 (100000)
# n = 84 (1010100) → result = 80 (1010000)


class Solution:
    def remove_last_set_bit(self, n: int):
        binary = bin(n)[2:]  # Convert number to binary string (remove '0b')

        binary = list(binary[::-1])  # Reverse to access LSB at index 0

        for i in range(len(binary)):  # Traverse bits from LSB to MSB
            if binary[i] == "1":  # Find first set bit (rightmost 1)
                binary[i] = "0"  # Turn it into 0
                break  # Stop after removing only one set bit

        binary = binary[::-1]  # Reverse back to original order

        binary_str = "".join(binary)  # Convert list back to string

        return int(binary_str, 2)  # Convert binary string to integer


obj = Solution()
print(obj.remove_last_set_bit(40))  # Output : 32
print(obj.remove_last_set_bit(84))  # Output : 80


"""
Logic Explanation:

Step 1: Convert integer to binary string
- bin(n) gives binary with '0b' prefix, so we remove it

Step 2: Reverse the binary string
- This allows direct access to the least significant bit (LSB) at index 0

Step 3: Traverse and find first '1'
- This represents the rightmost set bit
- Change it to '0' and stop

Step 4: Reverse back and reconstruct number
- Convert list → string → integer

Time Complexity:
- O(log n) (number of bits)

Space Complexity:
- O(log n) (binary representation)

Drawback:
- Uses extra space and conversions

Better Approach:
- Use n & (n - 1) for O(1) time and O(1) space
"""
