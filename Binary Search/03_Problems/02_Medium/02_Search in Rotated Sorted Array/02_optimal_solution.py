# Leetcode : 33. Search in Rotated Sorted Array (Optimal Approach)
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search_in_rotated_array(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2

            # If target is found at mid
            if nums[mid] == target:
                return mid

            # Check if the right half is sorted
            if nums[mid] <= nums[high]:
                # If target lies within the sorted right half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1  # move right
                else:
                    high = mid - 1  # move left

            # Otherwise, the left half must be sorted
            else:
                # If target lies within the sorted left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1  # move left
                else:
                    low = mid + 1  # move right
        # if target not found, return -1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
obj = Solution()
print(obj.search_in_rotated_array(nums, 0))  # output : 4

"""
LOGIC (Optimal Binary Search):

This solution searches for a target element in a rotated sorted array with distinct values using binary search.

Key Observations:
- At any given time, one half of the array is always sorted.
- By checking which half is sorted, we can decide where the target may lie and discard the other half.

Steps:
1. Initialize two pointers: low and high.
2. Find the middle index.
3. If nums[mid] equals target, return mid.
4. Check if the right half is sorted:
   - If target lies in that range, search right.
   - Otherwise, search left.
5. Else, the left half is sorted:
   - If target lies in that range, search left.
   - Otherwise, search right.
6. Repeat until low > high.
7. If target is not found, return -1.

TIME COMPLEXITY:
- O(log n)

SPACE COMPLEXITY:
- O(1)

"""
