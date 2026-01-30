# This program finds the floor and ceil of a target value in a sorted array (Optimal Solution)

# You're given a sorted array 'a' of 'n' integers and an integer 'x'.
# Find the floor and ceiling of 'x' in 'a[0..n-1]'.

# Example:
# Input: n=6, x=5, a=[3, 4, 7, 8, 8, 10]
# Output: 4 7
# Explanation: The floor and ceiling of 'x' = 5 are 4 and 7, respectively.


class Solution:
    def ceil_the_floor(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0  # left boundary of binary search
        high = n - 1  # right boundary of binary search
        floor = -1  # largest value <= target found so far
        ceil = -1  # smallest value >= target found so far

        # Binary search to find floor and ceil
        while low <= high:
            mid = (low + high) // 2  # middle index

            # If exact target is found, both floor and ceil are equal to target
            if nums[mid] == target:
                floor = nums[mid]
                ceil = nums[mid]
                break
            # If mid value is smaller than target, it is a valid candidate for floor
            elif nums[mid] < target:
                floor = nums[mid]
                low = mid + 1  # move right to find closer floor
            # If mid value is greater than target, it is a valid candidate for ceil
            else:
                ceil = nums[mid]
                high = mid - 1  # move left to find closer ceil

        return [floor, ceil]


nums = a = [3, 4, 7, 8, 8, 10]
obj = Solution()
print(obj.ceil_the_floor(nums, 6))  # Output: [4, 7]
print(obj.ceil_the_floor(nums, 7))  # Output: [7, 7]

"""
Logic Explanation:

1. The array is sorted in non-decreasing order, which allows the use of binary search.

2. We maintain two pointers:
   - low: starting index of the search space
   - high: ending index of the search space

3. We also maintain two variables:
   - floor: stores the largest element less than or equal to the target
   - ceil: stores the smallest element greater than or equal to the target

4. During each iteration of binary search:
   - If nums[mid] == target:
     • The target exists in the array.
     • Both floor and ceil are equal to the target.
     • We can stop searching.

   - If nums[mid] < target:
     • nums[mid] is a possible floor value.
     • We update floor and move right to find a closer value.

   - If nums[mid] > target:
     • nums[mid] is a possible ceil value.
     • We update ceil and move left to find a closer value.

5. When the loop ends:
   - floor contains the closest smaller or equal value (or -1 if none exists).
   - ceil contains the closest greater or equal value (or -1 if none exists).

6. Time Complexity:
   - O(log n), due to binary search.

7. Space Complexity:
   - O(1), as no extra space is used.
"""
