# This program finds the floor and ceil of a target value in a sorted array (Brute Force Approach)
# Floor: largest element less than or equal to the target
# Ceil : smallest element greater than or equal to the target


class Solution:
    def ceil_the_floor(self, nums: list[int], target: int) -> int:
        n = len(nums)
        floor = -1  # largest value smaller than or equal to target
        ceil = -1  # smallest value greater than or equal to target

        # Traverse the sorted array
        for i in range(n):
            # If exact target is found, both floor and ceil are the target itself
            if nums[i] == target:
                return [nums[i], nums[i]]
            # If current element is smaller than target, update floor (possible candidate)
            elif nums[i] < target:
                floor = nums[i]
            # If current element is greater than target, this is the first possible ceil since the array is sorted
            else:
                ceil = nums[i]
                break  # no need to check further elements, as we have to find - smallest index of element >= target
        return [floor, ceil]


nums = a = [3, 4, 7, 8, 8, 10]
obj = Solution()
print(obj.ceil_the_floor(nums, 6))  # Output: [4, 7]
print(obj.ceil_the_floor(nums, 7))  # Output: [7, 7]

"""
Logic Explanation:

1. The array is sorted in non-decreasing order.

2. We want to find:
   - Floor: the largest element that is less than or equal to the target.
   - Ceil: the smallest element that is greater than or equal to the target.

3. We iterate through the array from left to right:
   - If nums[i] == target:
     • The target exists in the array.
     • Both floor and ceil are equal to the target.
     • We return immediately.

   - If nums[i] < target:
     • nums[i] is a valid candidate for floor.
     • We keep updating floor until we cross the target.

   - If nums[i] > target:
     • Since the array is sorted, this is the first valid ceil.
     • We store it and break the loop.

4. If the loop finishes without finding an exact match:
   - floor will store the closest smaller value (or -1 if none exists).
   - ceil will store the closest greater value (or -1 if none exists).

5. Time Complexity:
   - O(n) in the worst case.

6. Space Complexity:
   - O(1), as no extra space is used.
"""
