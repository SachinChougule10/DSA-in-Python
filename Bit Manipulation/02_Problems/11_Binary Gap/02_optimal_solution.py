# Leetcode : 868. Binary Gap (Optimal Solution)
# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions.
# For example, the two 1's in "1001" have a distance of 3.

# Example 1:
# Input: n = 22
# Output: 2
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

# Example 2:
# Input: n = 8
# Output: 0
# Explanation: 8 in binary is "1000".
# There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

# Example 3:
# Input: n = 5
# Output: 2
# Explanation: 5 in binary is "101".

# Constraints:
# 1 <= n <= 109


class Solution:
    def binary_gap(self, n: int) -> int:
        # stores position of previous '1' bit
        prev_pos = -1

        # tracks current bit position (starting from LSB)
        curr_pos = 0

        # stores maximum distance found
        max_gap = 0

        while n:
            # Check if current bit is 1 using bitwise AND
            if n & 1:
                # If this is not the first '1', calculate gap
                if prev_pos != -1:
                    # distance between two 1's
                    gap = curr_pos - prev_pos
                    # update maximum gap
                    max_gap = max(max_gap, gap)

                # Update previous position to current position
                prev_pos = curr_pos

            # Right shift n to process next bit
            n = n >> 1

            # Move to next bit position
            curr_pos += 1

        return max_gap


obj = Solution()

n1 = 8
print(obj.binary_gap(n1))  # Output : 0

n2 = 5
print(obj.binary_gap(n2))  #  Output : 2

"""
Logic Explanation:

1. We traverse the binary representation of the number using bit manipulation.
   - Instead of converting to a string, we use bitwise operations for efficiency.

2. We maintain:
   - prev_pos: Position of the last encountered '1'
   - curr_pos: Current bit position (starting from 0 for LSB)
   - max_gap: Maximum distance between two consecutive 1's

3. For every bit:
   - Check if it is 1 using (n & 1)
   - If it's the first '1', just store its position
   - If it's not the first:
        gap = curr_pos - prev_pos
        Update max_gap

4. Shift the number right (n >> 1) to process next bit.

5. Continue until n becomes 0.

6. Return max_gap.


Example Walkthrough (n = 22 → binary = 10110):

Position:   4 3 2 1 0
Binary:     1 0 1 1 0

Iteration:
- pos 1 → first '1' → store prev_pos = 1
- pos 2 → '1' → gap = 2 - 1 = 1 → max_gap = 1
- pos 4 → '1' → gap = 4 - 2 = 2 → max_gap = 2

Final Answer = 2


Time Complexity: O(log n)
- We process each bit once.

Space Complexity: O(1)
- No extra space used.
"""
