# GFG : Total Hamming Distance (Optimal Solution)
# Given an integer array arr[], return the sum of Hamming distances between all the pairs of the integers in arr.
# Note: The answer is guaranteed to fit within a 32-bit integer.

# Examples:
# Input: arr[] = [1, 14]
# Output: 4
# Explanation: Binary representations of 1 is 0001, 14 is 1110. The answer will be:
# HammingDistance(1, 14) = 4.

# Input: arr[] = [4, 14, 4, 14]
# Output: 8
# Explanation: Binary representations of 4 is 0100, 14 is 1110. The answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 4) + HammingDistance(4, 14) + HammingDistance(14, 4) + HammingDistance(14, 14) + HammingDistance(4, 14) = 2 + 0 + 2 + 2 + 0 + 2 = 8.

# Constraints:
# 2 ≤ arr.size() ≤ 104
# 1 ≤ arr[i] ≤ 109


class Solution:
    def total_hamming_distance(self, arr):
        n = len(arr)
        total = 0  # final answer

        # check all 32 bits (for integers up to 10^9)
        for bit in range(32):
            count_1 = 0  # count of numbers with current bit = 1

            for num in arr:
                # check if 'bit'-th bit is set
                if num & (1 << bit):
                    count_1 += 1

            count_0 = n - count_1  # numbers with bit = 0

            # pairs with different bits contribute 1 each
            total += count_1 * count_0

        return total


obj = Solution()

arr1 = [4, 14, 4, 14]
print(obj.total_hamming_distance(arr1))  # Output : 8

arr2 = [1, 14]
print(obj.total_hamming_distance(arr2))  # Output : 4

"""
Logic:
- Instead of comparing all pairs, process each bit position independently
- For a given bit position:
   - Count how many numbers have that bit set (count_1)
   - Remaining numbers have that bit unset (count_0)
- Each pair with one 1 and one 0 contributes 1 to Hamming Distance
- Total contribution for that bit = count_1 * count_0
- Sum contributions for all bit positions

Steps:
1. Loop over all 32 bit positions (0 to 31)
2. For each bit:
   - Count numbers with bit = 1
   - Compute count_0 = n - count_1
   - Add count_1 * count_0 to result
3. Return the final sum

Time Complexity: O(32 * n) ≈ O(n)
Space Complexity: O(1)
"""
