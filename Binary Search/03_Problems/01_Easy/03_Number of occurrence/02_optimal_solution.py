# Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. Return 0 if the target is not present (optimal solution)


class Solution:

    # Finds the lower bound (first index where nums[index] >= target)
    def lower_bound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        first = -1  # stores the possible index of lower bound

        while low <= high:
            mid = (low + high) // 2

            # If mid element is >= target, it can be a lower bound
            if nums[mid] >= target:
                first = mid
                high = mid - 1  # move left to find earlier occurrence
            else:
                low = mid + 1  # move right

        return first

    # Finds the upper bound (first index where nums[index] > target)
    def upper_bound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        last = -1  # stores the possible index of upper bound

        while low <= high:
            mid = (low + high) // 2

            # If mid element is greater than target, it can be an upper bound
            if nums[mid] > target:
                last = mid
                high = mid - 1  # move left to find earlier index
            else:
                low = mid + 1  # move right

        return last

    # Returns the number of occurrences of target in nums
    def no_of_occurence(self, nums: list[int], target: int) -> int:

        # Find first occurrence (lower bound)
        lb = self.lower_bound(nums, target)
        # If target is not present
        if lb == -1 or nums[lb] != target:
            return 0

        # Find first index greater than target (upper bound)
        ub = self.upper_bound(nums, target)
        # If upper bound does not exist, target appears till end
        if ub == -1:
            return len(nums) - lb

        # Number of occurrences
        return ub - lb


nums = [1, 1, 2, 2, 2, 2, 3]
obj = Solution()
print(obj.no_of_occurence(nums, 2))  # output : 4
print(obj.no_of_occurence(nums, 10))  # output : 0
print(obj.no_of_occurence(nums, 3))  # output : 1
print(obj.no_of_occurence(nums, 1))  # output : 2

"""
LOGIC:

This solution finds the number of occurrences of a target element in a sorted array using binary search.

1. lower_bound():
   - Finds the first index where the element is greater than or equal to target.
   - If target exists, this index points to its first occurrence.

2. upper_bound():
   - Finds the first index where the element is strictly greater than target.
   - This helps identify the position just after the last occurrence of target.

3. Counting occurrences:
   - If lower_bound is invalid or does not point to target, return 0.
   - If upper_bound exists:
         occurrences = upper_bound - lower_bound
   - If upper_bound does not exist:
         occurrences = len(array) - lower_bound

TIME COMPLEXITY:
- lower_bound: O(log n)
- upper_bound: O(log n)
- Total: O(log n)

SPACE COMPLEXITY:
- O(1) (no extra space used)

This approach is optimal and efficient for sorted arrays.
"""
