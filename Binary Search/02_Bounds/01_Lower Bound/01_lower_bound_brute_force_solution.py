# Program: Brute Force Lower Bound in a Sorted Array
# This program finds the Lower Bound of a target value using a linear scan.
# Lower Bound is defined as the smallest index i such that nums[i] >= target.
# If no such index exists, the program returns n (length of the array).


class Solution:
    def lower_bound(self, nums: list[int], target: int) -> int:
        n = len(nums)  # Length of the array

        # Traverse the array from left to right
        for i in range(n):
            # If current element is equal to or greater than target, this index is the lower bound
            if nums[i] >= target:
                return i
        # If all elements are smaller than target, lower bound does not exist, return n
        return n


nums = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
obj = Solution()
print(obj.lower_bound(nums, 3))  # output : 2
print(obj.lower_bound(nums, 6))  # output : 4
print(obj.lower_bound(nums, 12))  # output : 10

"""
Logic Explanation:

The Lower Bound is the smallest index i such that nums[i] >= target.

Since the array is sorted, we can simply scan the array from left to right
and return the first index where the element is greater than or equal to the target.

Steps:
1. Traverse the array from index 0 to n - 1.
2. At each index, check if nums[i] >= target.
3. If the condition is satisfied, return the current index.
4. If the loop completes without finding such an index, it means all elements are smaller than the target.
5. In that case, return n.

Time Complexity:
- O(n) → Linear traversal of the array

Space Complexity:
- O(1) → No extra space used
"""
