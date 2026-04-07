# Leetcode : 78. Subsets : Given an integer array nums of unique elements, return all possible subsets (the power set) (Optimal Solution)
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


class Solution:
    def subsets(self, nums: list[int]):
        # Get the length of input array
        n = len(nums)

        # Total number of subsets = 2^n
        no_of_subsets = 1 << n  # equivalent to 2^n

        result = []

        # Iterate through all numbers from 0 to (2^n - 1)
        for num in range(no_of_subsets):
            subset = []

            # Check each bit position
            for i in range(n):
                # If i-th bit is set, include nums[i] in subset
                if num & (1 << i):
                    subset.append(nums[i])

            # Add the generated subset to result
            result.append(subset)

        return result


obj = Solution()
num1 = [1, 2, 3]
print(obj.subsets(num1))
# Output : [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

"""
LOGIC EXPLANATION:

This solution uses the concept of BIT MANIPULATION to generate all subsets.

1. Total Subsets:
   For an array of size n, total subsets = 2^n.
   Example: nums = [1,2,3] → 2^3 = 8 subsets

2. Binary Representation:
   Each number from 0 to (2^n - 1) represents a subset.
   
   Example for n = 3:
   0 → 000 → []
   1 → 001 → [1]
   2 → 010 → [2]
   3 → 011 → [1,2]
   4 → 100 → [3]
   5 → 101 → [1,3]
   6 → 110 → [2,3]
   7 → 111 → [1,2,3]

3. Idea:
   - Treat each number as a bitmask.
   - If i-th bit is set → include nums[i] in subset.

4. Bit Check:
   num & (1 << i)
   - Checks whether the i-th bit is ON (1).

5. Time Complexity:
   O(n * 2^n)
   - We generate 2^n subsets
   - For each subset, we check n bits

6. Space Complexity:
   O(n * 2^n)
   - To store all subsets

This is one of the most optimal and clean approaches for generating subsets.
"""
