# Leetcode : 930. Binary Subarrays With Sum (Brute Force Solution)
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
    def num_subarrays_with_sum(self, nums: list[int], goal: int):
        n = len(nums)
        # Stores number of valid subarrays
        count = 0

        # Running sum of current subarray
        total = 0

        # Outer loop: starting index of subarray
        for i in range(n):
            # Reset sum for new starting index
            total = 0

            # Inner loop: ending index of subarray
            for j in range(i, n):
                # Add current element to sum
                total += nums[j]

                # If sum exceeds goal, no need to continue further
                if total > goal:
                    break

                # If sum equals goal, increment count
                if total == goal:
                    count += 1

        return count


obj = Solution()

nums1 = [1, 0, 1, 0, 1]
goal1 = 2

print(obj.num_subarrays_with_sum(nums1, goal1))  # Output: 4

nums2 = [0, 0, 0, 0, 0]
goal2 = 0

print(obj.num_subarrays_with_sum(nums2, goal2))  # Output: 15


"""
Logic (Brute Force Approach):

1. Goal:
   Count number of subarrays whose sum is exactly equal to goal.

2. Approach:
   - Generate all possible subarrays using two loops.
   - Outer loop (i): starting index
   - Inner loop (j): ending index

3. Key Idea:
   - Maintain a running sum (total) for each subarray.
   - Add elements one by one as we expand the subarray.

4. Optimization:
   - If total > goal, break early (since array has only 0s and 1s,
     sum will only increase further).

5. Condition:
   - If total == goal → increment count

6. Example:
   nums = [1,0,1,0,1], goal = 2
   Valid subarrays:
   [1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1] → count = 4

7. Time Complexity:
   - O(n^2)

8. Space Complexity:
   - O(1)

Note:
   This works because elements are only 0 and 1 (monotonic sum).
"""
