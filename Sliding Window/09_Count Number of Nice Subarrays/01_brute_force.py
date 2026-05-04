# 1248. Count Number of Nice Subarrays (Brute Force Solution)
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.

# Example 3:
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

# Constraints:
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length


class Solution:
    def number_of_subarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Stores number of valid subarrays
        odd_count = 0

        # Counts number of odd elements in current subarray
        total = 0

        # Outer loop: starting index of subarray
        for i in range(n):
            # Reset odd count for new starting index
            total = 0

            # Inner loop: ending index of subarray
            for j in range(i, n):

                # nums[j] % 2 gives 1 if odd, 0 if even
                total += nums[j] % 2

                # If odd count exceeds k, stop expanding
                if total > k:
                    break

                # If exactly k odd numbers, it's a valid subarray
                if total == k:
                    odd_count += 1

        return odd_count


obj = Solution()

nums1 = [1, 1, 2, 1, 1]
k1 = 3
print(obj.number_of_subarrays(nums1, k1))  # Output: 2

nums2 = [2, 4, 6]
k2 = 1
print(obj.number_of_subarrays(nums2, k2))  # Output: 0

nums3 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k3 = 2
print(obj.number_of_subarrays(nums3, k3))  # Output: 16

"""
Logic (Brute Force Approach):

1. Goal:
   Count number of subarrays containing exactly k odd numbers.

2. Approach:
   - Generate all subarrays using two loops.
   - Outer loop (i): start index
   - Inner loop (j): end index

3. Key Idea:
   - Instead of checking odd manually, use:
        nums[j] % 2
     → 1 if odd, 0 if even

4. Maintain:
   - 'total' → number of odd elements in current subarray

5. Condition:
   - If total == k → valid subarray → increment count
   - If total > k → break (adding more elements will only increase odd count)

6. Optimization:
   - Early break works because odd count only increases

7. Example:
   nums = [1,1,2,1,1], k = 3
   Valid subarrays:
   [1,1,2,1], [1,2,1,1] → count = 2

8. Time Complexity:
   - O(n^2)

9. Space Complexity:
   - O(1)

Note:
   This is brute force. Optimal uses sliding window + atMost trick.
"""
