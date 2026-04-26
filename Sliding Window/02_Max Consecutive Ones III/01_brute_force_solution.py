# Leetcode : 1004. Max Consecutive Ones III : Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's (Brute Force Solution)

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Length of array
        n = len(nums)

        # Stores maximum valid subarray length
        maxLength = 0

        # Outer loop → fix starting index of subarray
        for i in range(n):
            # Count of 0s in current subarray
            zeroes = 0

            # Inner loop → extend subarray from i to j
            for j in range(i, n):
                # If current element is 0, increment zero count
                if nums[j] == 0:
                    zeroes += 1

                # Check if we can still flip at most k zeroes
                if zeroes <= k:
                    # Current subarray length
                    currLength = j - i + 1
                    maxLength = max(maxLength, currLength)
                else:
                    # If zeroes exceed k → no need to extend further
                    break

        return maxLength


obj = Solution()

nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
print(obj.longestOnes(nums1, 2))  # Output : 6

nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
print(obj.longestOnes(nums2, 3))  # Output : 10

# For Max Consecutive Ones III, we are actually solving: Find the longest subarray that contains at most k zeros.

"""
LOGIC (Brute Force Approach):

We need to find the longest subarray that contains at most k zeroes.
Why? Because we can flip at most k zeroes to 1s.

--------------------------------------------------

Key Idea:
Try all possible subarrays and check:
→ If number of zeroes <= k → valid subarray
→ Track maximum length among valid ones

--------------------------------------------------

Steps:

1. Fix starting index i (outer loop)

2. For each i, expand subarray using j (inner loop):
   - Keep track of number of zeroes in current window

3. For every element nums[j]:
   - If nums[j] == 0 → increment zero count

4. If zeroes <= k:
   - Calculate length = j - i + 1
   - Update maxLength

5. If zeroes > k:
   - Break the loop (no need to check further j)
   - Because adding more elements will only increase length but still invalid

--------------------------------------------------

Example:
nums = [1,1,1,0,0,0,1], k = 2

For i = 0:
→ Expand j until zeroes > k
→ Valid subarrays:
   [1], [1,1], [1,1,1], [1,1,1,0], [1,1,1,0,0]
→ Stop when zeroes = 3

--------------------------------------------------

Time Complexity:
O(n^2)
- Outer loop runs n times
- Inner loop runs up to n times

--------------------------------------------------

Space Complexity:
O(1)
- No extra space used

--------------------------------------------------

Important Insight:
This brute force works but is not optimal.
Better approach = Sliding Window (O(n))

--------------------------------------------------
"""
