# Leetcode : 930. Binary Subarrays With Sum (Optimal Solution)
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

# Constraints:
# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length


class Solution:
    def at_most(self, nums: list[int], goal: int) -> int:

        # If goal is negative, no valid subarray exists
        if goal < 0:
            return 0

        n = len(nums)
        # Left pointer of sliding window
        left = 0

        # Current window sum
        total = 0

        # Count of subarrays with sum <= goal
        count = 0

        for right in range(n):
            # Expand window by adding current element
            total += nums[right]

            # Shrink window until sum becomes <= goal
            while total > goal:
                total -= nums[left]
                left += 1

            # Number of valid subarrays ending at 'right'
            # = size of current window
            count += right - left + 1

        return count

    def num_subarrays_with_sum(self, nums: list[int], goal: int):
        # Exact sum = atMost(goal) - atMost(goal - 1)
        return self.at_most(nums, goal) - self.at_most(nums, goal - 1)


obj = Solution()

nums1 = [1, 0, 1, 0, 1]
goal1 = 2

print(obj.num_subarrays_with_sum(nums1, goal1))  # Output: 4

nums2 = [0, 0, 0, 0, 0]
goal2 = 0

print(obj.num_subarrays_with_sum(nums2, goal2))  # Output: 15


# Why subtraction works

# Look carefully.

# atMost(2) contains:
# sum 0
# sum 1
# sum 2

# atMost(1) contains:
# sum 0
# sum 1

# If we remove the second from the first:

# (sum0 + sum1 + sum2)
# -
# (sum0 + sum1)

# Remaining:

# sum2

# Which is exactly what we want.

"""
Logic (Optimal Sliding Window + At Most Trick):

1. Goal:
   Count subarrays with sum exactly equal to goal.

2. Key Trick:
   exact(goal) = atMost(goal) - atMost(goal - 1)

3. Why this works:
   - atMost(goal) → counts subarrays with sum ≤ goal
   - atMost(goal - 1) → counts subarrays with sum ≤ goal - 1
   - Subtracting removes all smaller sums, leaving only exact = goal

4. Sliding Window (at_most function):
   - Use two pointers (left, right)
   - Expand window with 'right'
   - If sum exceeds goal, shrink using 'left'
   - At each step, count subarrays ending at right:
        count += (window size)

5. Why (right - left + 1)?
   - All subarrays ending at 'right' and starting from any index
     between left → right are valid

6. Edge Case:
   - If goal < 0 → return 0 (no valid subarrays)

7. Complexity:
   - Time: O(n)
   - Space: O(1)

8. Example:
   nums = [1,0,1,0,1], goal = 2
   Result = 4

Important Pattern:
   EXACT K = atMost(K) - atMost(K-1)
"""
