# Problem: This program finds the FLOOR of a given target value in a sorted array using binary search
# Definition:The floor of a given target value is the largest element in the array that is less than or equal to the target.
# floor = largest number in an array <= target


class Solution:
    def floor(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Initialize binary search boundaries
        low = 0
        high = n - 1
        # Stores the floor value (largest element <= target)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            # If mid element is <= target, it can be a floor candidate
            if nums[mid] <= target:
                ans = nums[mid]  # Update floor
                low = mid + 1  # Try to find a larger valid floor on the right
            else:
                high = mid - 1  # Move left if mid element is greater than target

        return ans


nums = [10, 20, 30, 40, 50]
obj = Solution()
print(obj.floor(nums, 25))  # output : 20

"""
Logic Summary:

1. Binary search is used because the array is sorted.
2. `ans` keeps track of the best floor value found so far.
3. Whenever nums[mid] <= target:
   - Update ans with nums[mid]
   - Move right to search for a larger valid floor.
4. If nums[mid] > target:
   - Move left to find smaller elements.
5. After the loop, ans contains the floor value.
6. If no floor exists, ans remains -1.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
