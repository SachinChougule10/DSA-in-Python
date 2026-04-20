# LeetCode : 268. Missing Number : Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array (Optimal Solution)

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation:
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


class Solution:
    def missing_number(self, nums: list[int]) -> int:
        n = len(nums)

        # XOR of all numbers from 0 to n
        xor_all = 0

        # XOR of all elements in array
        xor_arr = 0

        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor_all ^= i

        # XOR all elements in the given array
        for num in nums:
            xor_arr ^= num

        # Missing number = XOR of both results
        return xor_all ^ xor_arr


obj = Solution()

nums1 = [0, 1]
print(obj.missing_number(nums1))  # Output : 2

nums2 = [3, 0, 1]
print(obj.missing_number(nums2))  # Output : 2

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(obj.missing_number(nums3))  # Output : 8

"""
Optimal XOR Approach to Find Missing Number:

1. We are given an array of size 'n' containing distinct numbers 
   from the range 0 to n. One number is missing.

2. Key XOR Properties used:
   - a ^ a = 0        (same numbers cancel out)
   - a ^ 0 = a        (identity property)
   - XOR is commutative and associative

3. Strategy:
   - XOR all numbers from 0 to n → xor_all
   - XOR all elements of the array → xor_arr

4. Since the array contains all numbers except one:
   - Every number that appears in both groups cancels out
   - Only the missing number remains

5. Final result:
   missing_number = xor_all ^ xor_arr

6. Example intuition:
   (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1)
   → (0^0) ^ (1^1) ^ (3^3) ^ 2
   → 2

Time Complexity:
- O(n) → single pass computations

Space Complexity:
- O(1) → no extra space used
"""
