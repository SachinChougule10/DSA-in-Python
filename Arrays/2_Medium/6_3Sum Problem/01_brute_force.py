# Leetcode : 15. 3Sum : Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)  # Length of the array
        my_set = set()  # Set to store unique triplets
        temp = []  # Temporary list to store a triplet

        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the sum of the triplet is zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        # Sort the triplet to handle duplicates
                        temp.sort()
                        # Convert list to tuple (hashable) and add to set
                        my_set.add(tuple(temp))

        # Convert set of tuples back to list of lists
        return [list(i) for i in my_set]


nums = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.three_sum(nums))

"""
# 1. We use three nested loops to generate all possible triplets (i, j, k) such that i < j < k. This ensures all indices are different.

# 2. For every triplet, we check whether : nums[i] + nums[j] + nums[k] == 0

# 3. If the sum is zero:
#    - We store the triplet in a temporary list
#    - Sort the triplet so that duplicates like [-1, 0, 1] and [1, -1, 0] become identical after sorting

# 4. We store the sorted triplet as a tuple in a set.
#    - Set automatically removes duplicate triplets
#    - Tuples are used because lists are not hashable

# 5. Finally, we convert the set of tuples back into a list of lists and return the result.

# Time Complexity:
# - O(n³) due to three nested loops

# Space Complexity:
# - O(k), where k is the number of unique triplets stored in the set

# This brute-force approach is easy to understand but inefficient for large inputs.
# Optimized solutions use sorting + two pointers to achieve O(n²) time complexity.

"""
