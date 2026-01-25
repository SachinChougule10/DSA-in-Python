# Program: Upper Bound in a Sorted Array
# Description: This program implements the Upper Bound operation using Binary Search.
# Upper Bound = smallest index such that arr[index] > target
# If no such index exists, return -1


class Solution:
    def upper_bound(self, nums: list[int], target: int) -> int:
        n = len(nums)  # Length of the array
        low = 0  # Left boundary of binary search
        high = n - 1  # Right boundary of binary search
        ans = -1  # Stores the upper bound index (if found)

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2  # Calculate middle index

            # If current element is strictly greater than target, it is a potential upper bound
            if nums[mid] > target:
                # Store possible answer
                ans = mid
                # Move left to check if there exists a smaller index that also satisfies the condition
                high = mid - 1
            else:
                # Current element is less than or equal to target, discard left half
                low = mid + 1
        # ans will hold the smallest index where nums[index] > target. If no such index exists, ans remains -1
        return ans


nums = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]
obj = Solution()
print(obj.upper_bound(nums, 8))  # output : 6

"""
LOGIC EXPLANATION:

Upper Bound finds the smallest index i such that nums[i] > target.

Since the array is sorted, Binary Search is used to efficiently locate the boundary where elements change from <= target to > target.

Steps:
1. Initialize two pointers:
   - low at the start of the array
   - high at the end of the array

2. Find the middle index:
      mid = (low + high) // 2

3. Compare nums[mid] with target:
   - If nums[mid] > target:
        • This index is a valid upper bound candidate
        • Store mid in ans
        • Move left (high = mid - 1) to find the FIRST such index
   - If nums[mid] <= target:
        • Discard the left half
        • Move right (low = mid + 1)

4. Continue until low > high.

5. Return ans:
   - ans contains the smallest index where nums[index] > target
   - If such an index does not exist, ans remains -1

TIME COMPLEXITY:
- O(log n)

SPACE COMPLEXITY:
- O(1)
"""
