# Leetcode : 992. Subarrays with K Different Integers (Optimal Solution)
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

# Example 2:
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length


class Solution:
    def subarray_with_k_distinct(self, nums: list[int], k: int) -> int:
        # Exactly k distinct = atMost(k) - atMost(k-1)
        return self.at_most(nums, k) - self.at_most(nums, k - 1)

    def at_most(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0  # Left pointer of sliding window
        hash_map = {}  # Stores frequency of elements in current window
        count = 0  # Counts subarrays with at most k distinct elements

        for right in range(n):
            # Add current element to hashmap
            hash_map[nums[right]] = hash_map.get(nums[right], 0) + 1

            # If distinct elements exceed k, shrink window
            while len(hash_map) > k:
                hash_map[nums[left]] -= 1

                # Remove element if its frequency becomes 0
                if hash_map[nums[left]] == 0:
                    del hash_map[nums[left]]

                left += 1  # Move left pointer

            # Count subarrays ending at 'right'
            # All subarrays from left → right are valid
            count += right - left + 1

        return count


obj = Solution()

nums1 = [1, 2, 1, 2, 3]
k1 = 2
print(obj.subarray_with_k_distinct(nums1, k1))  # Output: 7

nums2 = [1, 2, 1, 3, 4]
k2 = 3
print(obj.subarray_with_k_distinct(nums2, k2))  # Output: 3


"""
Logic (Optimal Sliding Window + At Most Trick):

1. Goal:
   Count subarrays with exactly k distinct integers.

2. Key Trick:
   exact(k) = atMost(k) - atMost(k - 1)

3. Why this works:
   - atMost(k) → subarrays with ≤ k distinct elements
   - atMost(k-1) → subarrays with ≤ k-1 distinct elements
   - Subtract → gives exactly k distinct elements

4. Sliding Window (at_most):
   - Use two pointers (left, right)
   - Expand window with 'right'
   - Maintain frequency map
   - If distinct elements > k → shrink window

5. Counting:
   - For each 'right', number of valid subarrays =
     (right - left + 1)

6. Why (right - left + 1)?
   - All subarrays ending at 'right' and starting from any
     index between left → right are valid

7. Complexity:
   - Time: O(n)
   - Space: O(k)

8. Example:
   nums = [1,2,1,2,3], k = 2 → Output = 7

Important Pattern:
   EXACT K = atMost(K) - atMost(K-1) # pattern
"""
