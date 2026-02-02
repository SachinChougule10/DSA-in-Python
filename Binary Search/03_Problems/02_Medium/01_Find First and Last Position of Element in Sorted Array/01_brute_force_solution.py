# Leetcode : 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].


class Solution:
    def first_and_last_position(self, nums: list[int], target: int):
        n = len(nums)

        first_position = -1  # stores index of first occurrence of target
        last_position = -1  # stores index of last occurrence of target

        # Traverse the array once
        for i in range(n):
            # If current element matches the target
            if nums[i] == target:
                # If this is the first time target is found
                if first_position == -1:
                    first_position = i
                # Update last_position every time target is found
                last_position = i

            # Since the array is sorted: nums[i] > target means we have crossed all possible target values.
            # We break ONLY if the target was already found and we move past it, otherwise breaking early may skip the target completely.
            elif nums[i] > target and last_position != -1:
                break
        return [first_position, last_position]


nums = [5, 7, 7, 8, 8, 10]
nums1 = [1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9]
obj = Solution()
print(obj.first_and_last_position(nums, 8))  # output : [3, 4]
print(obj.first_and_last_position(nums1, 3))  # output : [2, 6]

"""
Logic Explanation:

1. The array is sorted in non-decreasing order, which allows us to scan it from left to right and stop early when appropriate.

2. We maintain two variables:
   - first_position: stores the index of the first occurrence of the target.
   - last_position: stores the index of the last occurrence of the target.

3. While iterating through the array:
   - When nums[i] == target, we record the index.
     • first_position is set only once (first occurrence).
     • last_position is updated every time the target is found.

4. Since the array is sorted:
   - When nums[i] becomes greater than target, no further target values can appear after this index.

5. However, we break the loop only if the target has already been found
   (last_position != -1).
   - This condition ensures we do not stop searching before finding the target.
   - If we break as soon as nums[i] > target without finding the target, we may exit the loop too early and miss the correct result.

6. If the target is never found:
   - first_position and last_position remain -1.

7. Time Complexity:
   - O(n) in the worst case.

8. Space Complexity:
   - O(1), as no extra space is used.
"""
