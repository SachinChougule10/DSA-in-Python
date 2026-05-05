# Leetcode : 992. Subarrays with K Different Integers (Brute Force Solution)
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
        n = len(nums)
        hash_set = set()  # Stores distinct elements in current subarray
        count = 0  # Counts number of valid subarrays

        # Outer loop: starting index of subarray
        for i in range(n):
            hash_set = set()  # Reset set for new starting index

            # Inner loop: ending index of subarray
            for j in range(i, n):
                hash_set.add(nums[j])  # Add current element

                # If distinct elements exceed k, stop expanding
                if len(hash_set) > k:
                    break

                # If exactly k distinct elements → valid subarray
                elif len(hash_set) == k:
                    count += 1

        return count


obj = Solution()

nums1 = [1, 2, 1, 2, 3]
k1 = 2
print(obj.subarray_with_k_distinct(nums1, k1))  # Output: 7

nums2 = [1, 2, 1, 3, 4]
k2 = 3
print(obj.subarray_with_k_distinct(nums2, k2))  # Output: 3


"""
Logic (Brute Force Approach):

1. Goal:
   Count subarrays with exactly k distinct integers.

2. Approach:
   - Generate all subarrays using two loops.
   - Outer loop (i): start index
   - Inner loop (j): end index

3. Data Structure:
   - Use a set to store distinct elements in current subarray

4. Steps:
   - Add elements one by one to the set
   - If size of set > k → break (invalid)
   - If size of set == k → valid subarray → increment count

5. Optimization:
   - Early break works because adding more elements
     will only increase distinct count

6. Example:
   nums = [1,2,1,2,3], k = 2
   Valid subarrays:
   [1,2], [2,1], [1,2], [2,3],
   [1,2,1], [2,1,2], [1,2,1,2]

7. Time Complexity:
   - O(n^2)

8. Space Complexity:
   - O(k)

Note:
   Optimal solution uses sliding window + atMost trick.
"""
