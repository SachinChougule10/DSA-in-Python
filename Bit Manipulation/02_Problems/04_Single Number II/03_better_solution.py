# Leetcode : 137. Single Number II : Given an integer array nums where every element appears three times except for one, which appears exactly once (Better Solution)
# Find the single element and return it. You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3

# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

# Constraints:
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1


class Solution:
    def single_number(self, nums: list[int]) -> int:
        # Sort the array so duplicates are grouped together
        nums.sort()
        n = len(nums)

        # Traverse in steps of 3 (since elements appear 3 times)
        for i in range(1, n, 3):
            # Compare current element with previous
            # If they are not equal → previous element is the unique one
            if nums[i] != nums[i - 1]:
                return nums[i - 1]

        # If all triplets are valid, last element is the unique one
        return nums[n - 1]


obj = Solution()

nums = [0, 1, 0, 1, 0, 1, 99]
print(obj.single_number(nums))  # Output : 99

"""
Logic: Sorting + Group Checking Approach

Idea:
- Since every element appears 3 times except one,
  sorting will group identical elements together

Approach:
1. Sort the array
2. Traverse the array in steps of 3
3. For each group:
   - Check if nums[i] == nums[i - 1]
   - If not → nums[i - 1] is the unique element
4. If all groups are valid, last element is the answer

Key Observation:
- Triplets will always look like: [x, x, x]
- Unique element will break this pattern

Example:
nums = [0, 1, 0, 1, 0, 1, 99]

After sorting:
[0, 0, 0, 1, 1, 1, 99]

Check groups:
- (0, 0, 0) → valid
- (1, 1, 1) → valid
- 99 → single → answer

Why this works:
- Sorting clusters duplicates
- We only need to detect where the triplet pattern breaks

Time Complexity:
- O(n log n) → due to sorting

Space Complexity:
- O(1) (if in-place sort is considered)

One-line intuition:
Sort → check groups of 3 → find where pattern breaks
"""
