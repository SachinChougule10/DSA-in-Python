# Problem: Find ceil in a Sorted Array (Binary Search – Optimal Approach)
# Definition: The ceil of a given target value is the smallest element in the array that is greater than or equal to the target.
# ceil = smallest number in array >= target


class Solution:
    def ceil(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Initialize binary search boundaries
        low = 0
        high = n - 1
        # Stores the ceil value (smallest element >= target). If no ceil exists, it will remain -1
        ans = -1

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2

            # If mid element can be a ceil candidate
            if nums[mid] >= target:
                ans = nums[mid]  # Update ceil
                high = mid - 1  # Search left for a smaller valid ceil
            else:
                low = mid + 1  # Search right for larger elements
        return ans


nums = [10, 20, 30, 40, 50]
obj = Solution()
print(obj.ceil(nums, 25))  # output : 30

"""
Logic Summary:

1. Binary search is used because the array is sorted.
2. `ans` keeps track of the best ceil value found so far.
3. Whenever nums[mid] >= target:
   - Update ans with nums[mid]
   - Move left to check if a smaller valid ceil exists.
4. If nums[mid] < target:
   - Move right to find larger elements.
5. After the loop, ans contains the smallest element >= target.
6. If no such element exists, ans remains -1.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
