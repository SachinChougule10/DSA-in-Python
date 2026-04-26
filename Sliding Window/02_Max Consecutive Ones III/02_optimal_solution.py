# Leetcode : 1004. Max Consecutive Ones III : Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's (Optimal  Solution)

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

        # Left pointer of sliding window
        left = 0

        # Count of zeroes in current window
        zeroes = 0

        # Expand window using right pointer
        for right in range(n):
            # If current element is 0, increment zero count
            if nums[right] == 0:
                zeroes += 1

            # If zeroes exceed k, shrink window from left
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1  # Reduce zero count when removing a 0
                left += 1  # Move left pointer forward

            # Window is valid here (zeroes <= k)
            currLength = right - left + 1
            maxLength = max(maxLength, currLength)

        return maxLength


obj = Solution()

nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
print(obj.longestOnes(nums1, 2))  # Output : 6

nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
print(obj.longestOnes(nums2, 3))  # Output : 10

nums3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(obj.longestOnes(nums3, 2))  # Output : 11

# For Max Consecutive Ones III, we are actually solving: Find the longest subarray that contains at most k zeros.

"""
LOGIC (Optimal - Sliding Window):

We need to find the longest subarray that contains at most k zeroes.
This is a classic "variable size sliding window" problem.

--------------------------------------------------

Key Idea:
Maintain a window [left, right] such that:
→ Number of zeroes in the window <= k

Expand the window using right pointer.
If condition breaks (zeroes > k), shrink window using left pointer.

--------------------------------------------------

Steps:

1. Initialize:
   left = 0
   zeroes = 0
   maxLength = 0

2. Traverse array with right pointer:

   - If nums[right] == 0:
       → Increment zero count

3. If zeroes > k:
   - Shrink window from left:
       → If nums[left] == 0 → decrement zero count
       → Move left forward

   - Repeat until zeroes <= k

4. Now window is valid:
   - Calculate length = right - left + 1
   - Update maxLength

--------------------------------------------------

Why this works:
- We always maintain a VALID window (at most k zeroes)
- We expand greedily and shrink only when needed
- This ensures we check all valid subarrays efficiently

--------------------------------------------------

Example:
nums = [1,1,1,0,0,0,1], k = 2

Window expands → zeroes increase
When zeroes > k → shrink from left
Always maintain valid window

--------------------------------------------------

Time Complexity:
O(n)
- Each element is visited at most twice (once by right, once by left)

--------------------------------------------------

Space Complexity:
O(1)
- No extra space used

--------------------------------------------------

Important Insight:
This is a standard pattern:
→ "Longest subarray with at most K constraint"

Same pattern used in:
- Longest substring with k distinct chars
- Max consecutive ones II
- Fruit into baskets

--------------------------------------------------
"""
