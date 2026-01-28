# Problem: Find ceil in a Sorted Array (Brute Force Approach)
# Definition: The ceil of a given target value is the smallest element in the array that is greater than or equal to the target.
# ceil = smallest number in array >= target


class Solution:
    def ceil(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # Traverse each element in the sorted array
        for i in range(n):
            # First element >= target is the ceil
            if nums[i] >= target:
                return nums[i]
        return -1  # If no ceil exists


nums = [10, 20, 30, 40, 50]
obj = Solution()
print(obj.ceil(nums, 25))  # output : 30

"""
Logic Summary:

1. The array is sorted in ascending order.
2. Traverse the array from the beginning.
3. The first element that is greater than or equal to the target is the ceil.
4. Return that element immediately.
5. If traversal finishes without finding such an element, return -1 to indicate that no ceil exists.

Time Complexity: O(n)
Space Complexity: O(1)
"""
