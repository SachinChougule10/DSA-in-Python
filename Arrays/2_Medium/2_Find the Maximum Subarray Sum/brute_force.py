# Leetcode 53: Given an integer array nums, find the subarray with the largest sum, and return its sum.


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        n = len(nums)

        maximum = float("-inf")  # initialize maximum sum to the lowest possible value

        for i in range(0, n):  # Outer loop picks starting point of subarray
            total = 0  # reset sum for each new subarray start

            for j in range(i, n):  # Inner loop extends subarray from index i to j
                total = total + nums[j]
                maximum = max(maximum, total)  # update max sum if a higher sum is found

        return maximum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Solution()
print(obj.maxSubArray(nums))


"""Approach:-

Brute Force — Check All Subarrays
Use two loops to try every possible subarray.
Compute the sum for each subarray starting at i and ending at j.
Keep track of the maximum sum found.

Time Complexity: O(n²)
 → For every i, we scan j...n (all subarrays are checked)
Space Complexity: O(1)
 → No extra data structures used.
"""
