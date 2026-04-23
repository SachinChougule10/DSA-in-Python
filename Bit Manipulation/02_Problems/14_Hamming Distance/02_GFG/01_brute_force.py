# GFG : Total Hamming Distance (Brute Force Solution)
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
        total = 0  # stores final answer

        # iterate over all pairs
        for i in range(n):
            for j in range(i + 1, n):

                # XOR gives bits where numbers differ
                xor = arr[i] ^ arr[j]

                # count set bits (number of 1s in xor)
                count = 0
                while xor:
                    xor = xor & (xor - 1)  # removes rightmost set bit
                    count += 1

                total += count  # add distance for this pair

        return total


obj = Solution()

arr1 = [4, 14, 4, 14]
print(obj.total_hamming_distance(arr1))  # Output : 8

arr2 = [1, 14]
print(obj.total_hamming_distance(arr2))  # Output : 4

"""
Logic:
- Iterate over all possible pairs (i, j) where i < j
- For each pair, compute XOR of the two numbers
- XOR gives 1 at positions where bits differ
- Count the number of set bits in the XOR result
- Add this count to the total answer

Steps:
1. Use two nested loops to generate all pairs
2. For each pair:
   - Compute xor = arr[i] ^ arr[j]
   - Count set bits in xor (using Brian Kernighan’s algorithm)
3. Add the count to the result
4. Return the final sum

Time Complexity: O(n^2 * log(max_element))
Space Complexity: O(1)
"""
