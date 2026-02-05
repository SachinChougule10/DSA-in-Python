# Leetcode : 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.


class Solution:
    def minimum_in_rotated_sorted_array(self, nums: list[int]) -> int:
        n = len(nums)
        # Initialize binary search boundaries
        low = 0
        high = n - 1
        # Store the minimum element found
        min_element = float("inf")

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2

            # At least one half of the array is always sorted. The minimum element lies at the rotation point,
            # and the rotation point is part of the UNSORTED half.So we always move toward the unsorted half.

            # If the right half is sorted
            if nums[mid] <= nums[high]:
                # nums[mid] could be the minimum, but the actual minimum (rotation point) lies to the left
                min_element = min(min_element, nums[mid])
                # move to unsorted left half
                high = mid - 1
            else:
                # Left half is sorted, so nums[low] is the minimum of this half, but the overall minimum (rotation point) lies in the unsorted right half
                min_element = min(min_element, nums[low])
                # move to unsorted right half
                low = mid + 1
        return min_element


nums = [3, 4, 5, 1, 2]
obj = Solution()
print(obj.minimum_in_rotated_sorted_array(nums))  # output : 1

"""
Logic:
1. The array is a rotated version of a sorted array with unique elements.
2. In such an array, at least one half (left or right) is always sorted.
3. The minimum element appears exactly at the rotation point.
4. A sorted half cannot contain the rotation point, because rotation breaks the sorted order.
5. Therefore, the minimum element must always lie in the UNSORTED half.

Binary Search Decisions:

6. If nums[mid] <= nums[high]:
   - The right half [mid ... high] is sorted.
   - The rotation point (minimum) cannot lie inside this sorted half,
     though nums[mid] itself could be the minimum.
   - Record nums[mid] as a candidate and search the left (unsorted) half.

7. Else (nums[mid] > nums[high]):
   - The left half [low ... mid] is sorted.
   - Since no rotation occurred here, nums[low] is only the minimum of the left half, not the entire array.
   - Hence, the rotation point (minimum element) must lie in the unsorted right half [mid + 1 ... high].
   - Continue the search in the right half.

8. Repeat until the search space is exhausted.
9. Return the minimum element found.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""
