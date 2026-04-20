# LeetCode : 268. Missing Number : Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array (Brute Force Solution)

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
        # Total numbers present (one number is missing from 0 to n)
        n = len(nums)

        # Loop through all possible numbers from 0 to n
        for i in range(n + 1):

            #  Assume current number 'i' is not present
            found = False

            # Check if 'i' exists in the array
            for num in nums:
                if num == i:
                    found = True  # Number found
                    break  # Stop checking further

            # If 'i' was not found in the array, it is the missing number
            if not found:
                return i


obj = Solution()

nums1 = [0, 1]
print(obj.missing_number(nums1))  # Output : 2

nums2 = [3, 0, 1]
print(obj.missing_number(nums2))  # Output : 2

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(obj.missing_number(nums3))  # Output : 8


"""
Brute Force Approach to Find Missing Number:

1. The array contains 'n' distinct numbers from the range 0 to n.
   So exactly one number is missing.

2. Iterate through all numbers from 0 to n (inclusive).

3. For each number 'i':
   - Assume it is not present (found = False)
   - Traverse the entire array:
       → If 'i' is found, mark found = True and break

4. After checking the array:
   - If found is still False → 'i' is missing

5. Return the missing number immediately.

Time Complexity:
- Outer loop runs (n + 1) times
- Inner loop runs up to n times
→ O(n²)

Space Complexity:
- O(1) (no extra space used)
"""
