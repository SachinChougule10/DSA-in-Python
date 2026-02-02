# Leetcode : 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def lower_bound(self, nums: list[int], target: int):
        n = len(nums)
        low = 0
        high = n - 1
        first_position = -1  # stores first index where nums[mid] >= target

        # Binary search to find first index >= target
        while low <= high:
            mid = (low + high) // 2

            # If mid value is greater than or equal to target, it can be a possible first position
            if nums[mid] >= target:
                first_position = mid
                high = mid - 1  # move left to find earlier occurrence
            else:
                low = mid + 1  # move right
        return first_position

    def upper_bound(self, nums: list[int], target: int):
        n = len(nums)
        low = 0
        high = n - 1
        last_position = -1  # stores first index where nums[mid] > target

        # Binary search to find first index > target
        while low <= high:
            mid = (low + high) // 2

            # If mid value is greater than target, it can be a possible upper bound
            if nums[mid] > target:
                last_position = mid
                high = mid - 1  # move left to find earlier greater element
            else:
                low = mid + 1  # move right
        return last_position

    def search_range(self, nums: list[int], target: int) -> list[int]:

        # Find first occurrence (lower bound)
        lb = self.lower_bound(nums, target)

        # If target is not present in the array
        # lb == -1 → no element >= target
        # nums[lb] != target → element >= target exists but target itself doesn't
        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        # Find first element greater than target (upper bound)
        ub = self.upper_bound(nums, target)
        # If no element greater than target exists, then target occurs till the end of the array
        if ub == -1:
            return [lb, len(nums) - 1]

        # Last occurrence is just before upper bound
        return [lb, ub - 1]


nums = [5, 7, 7, 8, 8, 10]
obj = Solution()
print(obj.search_range(nums, 8))  # output : [3, 4]


"""
Logic Explanation:

1. The array is sorted, so binary search can be applied.

2. lower_bound():
   - Finds the first index where nums[index] >= target.
   - This gives the potential starting position of the target.
   - If nums[lb] != target, then the target does not exist in the array.

3. upper_bound():
   - Finds the first index where nums[index] > target.
   - This helps identify where the target elements end.

4. search_range():
   - First checks whether the target exists using lower_bound.
   - If not found, returns [-1, -1].
   - If upper_bound exists, the last position is ub - 1.
   - If upper_bound does not exist, the target extends till the end of the array.

5. Time Complexity:
   - lower_bound → O(log n)
   - upper_bound → O(log n)
   - Overall → O(log n)

6. Space Complexity:
   - O(1) (no extra space used)
"""
