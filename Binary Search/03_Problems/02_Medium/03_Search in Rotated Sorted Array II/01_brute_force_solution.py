# 81. Search in Rotated Sorted Array II (Brute Force Approach)
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.


class Solution:
    def search_sorted_array(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        # Traverse each element in the array
        for i in range(n):
            # Check if current element matches the target
            if nums[i] == target:
                return True  # Target found
        # If loop finishes and target is not found, return False
        return False


nums = [2, 5, 6, 0, 0, 1, 2]
obj = Solution()
print(obj.search_sorted_array(nums, 0))  # output: True
print(obj.search_sorted_array(nums, 10))  # output: False

"""
Logic (Brute Force Approach):

1. The given array is rotated and may contain duplicate elements.
2. Since this is a brute force solution, we do not rely on the sorted or rotated nature of the array.
3. We simply iterate through each element of the array one by one.
4. If any element matches the target value, we immediately return True.
5. If the entire array is traversed and the target is not found, we return False.

Time Complexity:
- O(n), where n is the number of elements in the array.

Space Complexity:
- O(1), as no extra space is used.
"""
