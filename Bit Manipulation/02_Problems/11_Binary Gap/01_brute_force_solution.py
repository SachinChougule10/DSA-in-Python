# Leetcode : 868. Binary Gap (Brute Force Solution)
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
        # Convert number to binary string (remove '0b' prefix)
        binary = bin(n)[2:]

        prev_index = -1  # stores index of previous '1'
        max_gap = 0  # stores maximum gap

        for i in range(len(binary)):
            if binary[i] == "1":
                # If not first '1', calculate gap
                if prev_index != -1:
                    gap = i - prev_index
                    max_gap = max(max_gap, gap)

                # Update previous index
                prev_index = i

        return max_gap


# Example usage
obj = Solution()

print(obj.binary_gap(8))  # Output: 0
print(obj.binary_gap(5))  # Output: 2

"""
Brute Force Approach (String-Based):

1. Convert the given integer n into its binary representation
   using bin(n)[2:] to remove the '0b' prefix.

2. Initialize:
   - prev_index = -1 → to store the index of the previous '1'
   - max_gap = 0 → to store the maximum distance

3. Traverse the binary string using a loop:
   - For each index i:
       • If binary[i] == '1':
            - If prev_index is not -1:
                gap = i - prev_index
                update max_gap = max(max_gap, gap)
            - Update prev_index = i

4. Continue until the entire string is processed.

5. Return max_gap.
   - If there are fewer than two '1's, max_gap remains 0.


Example:
n = 22 → binary = "10110"

Indices:   0 1 2 3 4
Binary:    1 0 1 1 0

Steps:
- i = 0 → '1' → prev_index = 0
- i = 2 → '1' → gap = 2 → max_gap = 2
- i = 3 → '1' → gap = 1 → max_gap = 2

Final Answer = 2


Time Complexity: O(log n)
- Length of binary string is proportional to log(n)

Space Complexity: O(log n)
- Binary string storage
"""
