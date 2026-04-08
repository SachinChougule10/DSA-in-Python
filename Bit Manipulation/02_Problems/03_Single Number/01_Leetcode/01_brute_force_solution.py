# Leetcode : 136. Single Number : Given a non-empty array of integers nums, every element appears twice except for one (Brute Force Solution)
# Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


class Solution:
    def single_number(self, nums: list[int]) -> int:
        # Dictionary to store frequency of each number
        hash_map = {}

        # Count frequency of each element
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        # Find the element with frequency = 1
        for key, value in hash_map.items():
            if value == 1:
                return key
        # Alternative way (commented)
        # Iterate original array and check frequency

        # for i in nums:
        #     if hash_map[i] == 1:
        #         return i


nums = [4, 1, 2, 1, 2]

obj = Solution()
print(obj.single_number(nums))  # Output : 4

"""
Logic Explanation:

1. Problem Understanding:
   - Every element appears twice except one.
   - We need to find that single occurring element.

2. Approach (Brute Force using Hash Map):
   - Use a dictionary (hash_map) to store frequency of each number.
   - Traverse the array and count occurrences.

3. Steps:
   - First loop:
        Build frequency map
        Example:
            nums = [4,1,2,1,2]
            hash_map = {4:1, 1:2, 2:2}

   - Second loop:
        Find the key whose value is 1
        → That is the single number

4. Why it works:
   - Since all numbers appear twice except one,
     only one element will have frequency = 1.

5. Complexity:
   - Time Complexity: O(n)
   - Space Complexity: O(n)

6. Note:
   - This is NOT optimal as it uses extra space.
   - Optimal solution uses XOR (O(1) space).
"""
