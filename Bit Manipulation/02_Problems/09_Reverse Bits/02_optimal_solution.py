# Leetcode : 190. Reverse Bits (Optimal Solution)
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
        # This will store the reversed bits
        result = 0

        # We iterate exactly 32 times (since integer is 32-bit)
        for _ in range(32):
            # Extract the last (rightmost) bit of n
            last_bit = n & 1

            # Shift result left to make space for new bit
            result = result << 1

            # Add extracted bit to result
            result = result | last_bit

            # Shift n right to process next bit
            n = n >> 1

        return result


obj = Solution()

n1 = 2147483644
print(obj.reverseBits(n1))  # Output : 1073741822

n2 = 43261596
print(obj.reverseBits(n2))  # Output : 964176192

"""
LOGIC EXPLANATION:

Goal:
------
Reverse the bits of a 32-bit integer.

Key Idea:
----------
We process the number bit by bit from right to left and build
the reversed number from left to right.

Step-by-step intuition:
------------------------
1. Extract last bit:
   - Use (n & 1)
   - This gives the rightmost bit (0 or 1)

2. Shift result left:
   - result << 1
   - This creates space for the new bit

3. Add extracted bit:
   - result | last_bit
   - Places the bit in result

4. Move to next bit in n:
   - n >> 1 (right shift)

We repeat this 32 times because:
- The problem guarantees a 32-bit integer
- Even if leading bits are 0, we must include them

Dry Run Example (n = 5 → binary: 000...0101):
--------------------------------------------
Iteration 1:
    last_bit = 1
    result = 1

Iteration 2:
    last_bit = 0
    result = 10

Iteration 3:
    last_bit = 1
    result = 101

... continues until 32 bits are processed

Final result = reversed binary

Time Complexity:
----------------
O(32) → O(1) (constant time)

Space Complexity:
-----------------
O(1)

Follow-up Optimization:
------------------------
If called multiple times:
- Precompute reversed values for 8-bit chunks (0 - 255)
- Break number into 4 bytes
- Reverse each using lookup table
- Combine results

This reduces repeated computation significantly.
"""
