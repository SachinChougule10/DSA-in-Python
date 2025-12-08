class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maximum = float("-inf")  # Stores the maximum subarray sum found so far
        currSum = 0  # Current running sum

        for i in range(0, n):
            currSum = currSum + nums[i]  # Add current element to running sum
            maximum = max(maximum, currSum)  # Update maximum if current sum is larger

            if currSum < 0:  # If running sum becomes negative, reset it to 0
                currSum = 0

        return maximum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Solution()
print(obj.maxSubArray(nums))


"""Approach: Kadane's Algorithm

We iterate through the array and maintain a running sum (currSum).

If currSum becomes negative, we reset it to 0 because a negative running sum will only reduce the sum of future subarrays.

We track the maximum sum encountered so far in maximum.

This gives the maximum subarray sum in O(n) time and O(1) space."""
