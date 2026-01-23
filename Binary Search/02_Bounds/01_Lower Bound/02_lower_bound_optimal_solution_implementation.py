# Program: Lower Bound in a Sorted Array
# Description: This program implements the Lower Bound operation using Binary Search.
# Lower Bound = smallest index such that arr[index] >= target
# If no such index exists, return -1


class Solution:
    def lower_bound(self, nums: list[int], target: int) -> int:
        n = len(nums)  # Length of the array
        low = 0  # Left boundary of binary search
        high = n - 1  # Right boundary of binary search
        ans = -1  # Stores the lower bound index (if found)

        while low <= high:
            mid = (low + high) // 2  # Calculate middle index

            # If current element is >= target, it is a potential lower bound
            if nums[mid] >= target:
                # Store the index as a possible answer
                ans = mid
                # Move left to check if there exists a smaller index that also satisfies the condition
                high = mid - 1
            else:
                # Current element is smaller than target, discard left half
                low = mid + 1

        # ans will hold the smallest index where nums[index] >= target. If no such index exists, ans remains -1
        return ans


nums = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
obj = Solution()
print(obj.lower_bound(nums, 1))  # output : 0
print(obj.lower_bound(nums, 9))  # output : 6


"""
LOGIC EXPLANATION:

Lower Bound finds the smallest index i such that nums[i] >= target.

Since the array is sorted, we use Binary Search to efficiently locate the boundary where elements change from < target to >= target.

Steps:
1. Initialize two pointers:
   - low at the start of the array
   - high at the end of the array

2. Find the middle index:
      mid = (low + high) // 2

3. Compare nums[mid] with target:
   - If nums[mid] >= target:
        • This index is a valid lower bound candidate
        • Store mid in ans
        • Move left (high = mid - 1) to find the FIRST occurrence
   - If nums[mid] < target:
        • Discard the left half
        • Move right (low = mid + 1)

4. Continue until low > high.

5. Return ans:
   - ans contains the smallest index where nums[index] >= target
   - If such an index does not exist, ans remains -1

TIME COMPLEXITY:
- O(log n) → Binary search halves the search space each iteration

SPACE COMPLEXITY:
- O(1) → No extra space used
"""
