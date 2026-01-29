# 35. Search Insert Position : Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
class Solution:
    def search_insert_position(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Traverse the array from left to right
        for i in range(n):
            # If the current element is equal to target, return its index
            if nums[i] == target:
                return i
            # If the current element is greater than target, this is the correct position to insert the target
            elif nums[i] > target:
                return i
        # If target is greater than all elements in the array, it should be inserted at the end
        return n


nums = [1, 3, 5, 6]
obj = Solution()
print(obj.search_insert_position(nums, 5))  # Output: 2
print(obj.search_insert_position(nums, 2))  # Output: 1
print(obj.search_insert_position(nums, 10))  # Output: 4

"""
Logic Explanation:

1. The array is sorted in strictly increasing order and contains distinct elements.

2. We iterate through the array from left to right.

3. For each element:
   - If nums[i] == target, the target is already present, so we return its index.
   - If nums[i] > target, the target cannot appear laterbecause the array is sorted.
     Therefore, the current index is the correct insert position.

4. If the loop finishes without returning:
   - It means the target is greater than all elements in the array.
   - In this case, the target should be inserted at the end, so we return n.

5. Time Complexity:
   - O(n) in the worst case.

6. Space Complexity:
   - O(1), as no extra space is used.
"""
