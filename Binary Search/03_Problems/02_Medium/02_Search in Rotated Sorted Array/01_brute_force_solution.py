# Leetcode : 33. Search in Rotated Sorted Array (Brute Force Solution)
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.


class Solution:
    def search_in_rotated_array(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # Traverse the array element by element
        for i in range(n):
            # If current element matches the target
            if nums[i] == target:
                return i  # return its index
        # If target is not found in the array return -1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
obj = Solution()
print(obj.search_in_rotated_array(nums, 0))  # output : 4

"""
LOGIC (Brute Force):

This solution searches for a target element in a rotated sorted array by scanning each element one by one.

Steps:
1. Iterate through the array from index 0 to n-1.
2. Compare each element with the target.
3. If a match is found, return the index.
4. If the loop finishes without finding the target, return -1.

Why this works:
- Rotation does not affect correctness because every element is still checked exactly once.

TIME COMPLEXITY:
- O(n), where n is the length of the array.

SPACE COMPLEXITY:
- O(1), no extra space used.
"""
