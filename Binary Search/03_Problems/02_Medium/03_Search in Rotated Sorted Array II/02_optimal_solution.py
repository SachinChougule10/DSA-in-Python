# 81. Search in Rotated Sorted Array II (Optimal Solution)
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.


class Solution:
    def search_in_rotated_array(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2

            # If target is found, return True
            if nums[mid] == target:
                return True

            # If nums[low], nums[mid], and nums[high] are equal, we cannot determine which half is sorted due to duplicates.
            # So, shrink the search space from both ends to avoid missing the target.
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # If right half is sorted
            if nums[mid] <= nums[high]:
                # Check if target lies in the sorted right half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            # Else, left half is sorted
            else:
                # Check if target lies in the sorted left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        # Target not found, return False
        return False


nums = [7, 7, 7, 7, 7, 7, 7, 1, 2, 3, 4, 5, 7, 7]
obj = Solution()
print(obj.search_in_rotated_array(nums, 1))  # output: True
print(obj.search_in_rotated_array(nums, 10))  # output: False

"""
Logic (Optimal Solution):

1. The array is sorted but rotated and may contain duplicate elements.
2. We apply binary search to reduce the number of operations.
3. At each step:
   - Compute the mid index.
   - If nums[mid] equals the target, return True.
4. If nums[low], nums[mid], and nums[high] are equal:
   - We cannot determine which half is sorted.
   - Shrink the search space by incrementing low and decrementing high.
5. Otherwise:
   - If the right half is sorted (nums[mid] <= nums[high]):
       - Check if the target lies within this range.
       - Narrow the search accordingly.
   - Else, the left half is sorted:
       - Check if the target lies within this range.
       - Narrow the search accordingly.
6. If the search space is exhausted, return False.

Time Complexity:
- Average Case: O(log n)
- Worst Case (all duplicates): O(n)

Space Complexity:
- O(1), as no extra space is used.

Note:
- Handling duplicates is essential, otherwise binary search fails.
- This approach minimizes operations while maintaining correctness.
"""
