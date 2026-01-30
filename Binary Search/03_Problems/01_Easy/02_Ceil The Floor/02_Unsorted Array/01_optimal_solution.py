# Ceil The Floor
# Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

# Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
# Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

# Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.


class Solution:
    def ceil_the_floor(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Initialize floor and ceil as -1
        floor = -1  # largest value <= target found so far
        ceil = -1  # smallest value >= target found so far

        # Traverse each element in the array
        for num in nums:
            # Check for floor condition
            if num <= target:
                # Update floor if: 1) floor is not set yet, 2)current number is greater than previous floor
                if floor == -1 or num > floor:
                    floor = num

            # Check for ceil condition
            if num >= target:
                # Update ceil if: 1) ceil is not set yet, 2) current number is smaller than previous ceil
                if ceil == -1 or num < ceil:
                    ceil = num

        # Return floor and ceil as a list
        return [floor, ceil]


nums = a = [3, 4, 7, 8, 8, 10]
obj = Solution()
print(obj.ceil_the_floor(nums, 6))  # Output: [4, 7]
print(obj.ceil_the_floor(nums, 7))  # Output: [7, 7]

"""
Logic:

We are given an unsorted array and a target value.
The goal is to find:
1. Floor → the largest element in the array that is less than or equal to the target.
2. Ceil  → the smallest element in the array that is greater than or equal to the target.

Approach:
- Since the array is unsorted, we cannot use binary search.
- We traverse the array once and track:
  - `floor`: maximum value <= target
  - `ceil`: minimum value >= target
- While iterating:
  - Update floor when a better (larger) valid candidate is found.
  - Update ceil when a better (smaller) valid candidate is found.
- If no valid floor or ceil exists, the value remains -1.

Complexity:
Time Complexity  : O(n)
Space Complexity : O(1)
"""
