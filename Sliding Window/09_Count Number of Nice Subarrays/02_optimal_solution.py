# 1248. Count Number of Nice Subarrays (Optimal Solution)
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
    def at_most(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0  # Left pointer of sliding window
        odd_count = 0  # Stores number of valid subarrays (result)
        total = 0  # Counts number of odd elements in current window

        for right in range(n):
            # Add current element (1 if odd, 0 if even)
            total += nums[right] % 2

            # Shrink window if odd count exceeds k
            while total > k:
                total -= nums[left] % 2
                left += 1

            # Count subarrays ending at 'right'
            # All subarrays starting from left → right are valid
            odd_count += right - left + 1

        return odd_count

    def number_of_subarrays(self, nums: list[int], k: int) -> int:
        # Exact k = atMost(k) - atMost(k-1)
        return self.at_most(nums, k) - self.at_most(nums, k - 1)


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
Logic (Optimal Sliding Window + At Most Trick):

1. Goal:
   Count subarrays with exactly k odd numbers.

2. Key Transformation:
   Convert array into:
   - 1 → odd number
   - 0 → even number

   So problem becomes similar to:
   "Binary Subarrays With Sum = k"

3. Key Trick:
   exact(k) = atMost(k) - atMost(k - 1)

4. Sliding Window (at_most function):
   - Use two pointers (left, right)
   - Expand window with 'right'
   - Add nums[right] % 2 to count odd numbers
   - If odd count > k → shrink window from left

5. Counting:
   - For each 'right', number of valid subarrays =
     (right - left + 1)

6. Why this works:
   - All subarrays ending at 'right' and starting between
     left → right satisfy atMost(k)

7. Final Answer:
   - Subtract atMost(k-1) from atMost(k)
   → gives exactly k odd numbers

8. Complexity:
   - Time: O(n)
   - Space: O(1)

Important Pattern:
   EXACT K = atMost(K) - atMost(K-1)

Same pattern as:
   - Binary Subarrays With Sum
"""
