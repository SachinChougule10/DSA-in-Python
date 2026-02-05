# Leetcode : 153. Find Minimum in Rotated Sorted Array (Brute Force Approach)
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.


class Solution:
    def minimum_in_rotated_array(self, nums: list[int]) -> int:
        n = len(nums)
        # Initialize minimum element with infinity
        min_element = float("inf")

        # Traverse through the array
        for i in range(n):
            # Update minimum if current element is smaller
            if nums[i] < min_element:
                min_element = nums[i]
        # Return the minimum element found
        return min_element


nums = [3, 4, 5, 1, 2]
obj = Solution()
print(obj.minimum_in_rotated_array(nums))  # output : 1

"""
Logic:
1. The array is a rotated version of a sorted array containing unique elements.
2. In a brute force approach, we do not use the sorted or rotated property.
3. We initialize a variable `min_element` with positive infinity.
4. Traverse each element of the array one by one.
5. Compare the current element with `min_element`.
6. If the current element is smaller, update `min_element`.
7. After traversing the entire array, `min_element` will store the smallest value.
8. Return the minimum element.

Time Complexity:
O(n), where n is the number of elements in the array.

Space Complexity:
O(1), as no extra space is used apart from variables.
"""
