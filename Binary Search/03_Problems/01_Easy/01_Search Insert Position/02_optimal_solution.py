# 35. Search Insert Position : Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search_insert_position(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0  # left boundary of binary search
        high = n - 1  # right boundary of binary search
        ans = n  # default insert position (end of array)

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2  # middle index

            # If nums[mid] is greater than or equal to target, target can be inserted at mid or before
            if nums[mid] >= target:
                ans = mid  # update possible insert position
                high = mid - 1  # move left to find earlier position
            # If nums[mid] is less than target, target must be inserted to the right
            else:
                low = mid + 1
        return ans


nums = [1, 3, 5, 6]
obj = Solution()
print(obj.search_insert_position(nums, 2))  # Output: 1
print(obj.search_insert_position(nums, 5))  # Output: 2
print(obj.search_insert_position(nums, 7))  # Output: 4

"""
Logic Explanation:

1. The array is sorted and contains distinct elements, which allows the use of binary search.

2. We maintain two pointers:
   - low: starting index of the search space
   - high: ending index of the search space

3. The variable ans is initialized to n:
   - This represents the case where the target is greater than all elements in the array and should be inserted at the end.

4. During each iteration:
   - mid is calculated as the middle index.
   - If nums[mid] >= target:
     • mid is a valid insert position.
     • Update ans with mid.
     • Move left (high = mid - 1) to find a smaller valid index.
   - If nums[mid] < target:
     • Target must be on the right side.
     • Move right (low = mid + 1).

5. When the loop ends:
   - ans holds the smallest index where target can be inserted while maintaining sorted order.

6. Time Complexity:
   - O(log n), because binary search is used.

7. Space Complexity:
   - O(1), as no extra space is required.
"""
