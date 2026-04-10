# Leetcode : 137. Single Number II : Given an integer array nums where every element appears three times except for one, which appears exactly once (Brute Force Solution)
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
        # Dictionary to store frequency of each element
        hash_map = {}

        for num in nums:
            # Count frequency of each number
            hash_map[num] = hash_map.get(num, 0) + 1

        for num, value in hash_map.items():
            # The element appearing exactly once is our answer
            if value == 1:
                return num


obj = Solution()

nums = [0, 1, 0, 1, 0, 1, 99]
print(obj.single_number(nums))  # Output : 99

"""
Logic: Brute Force using HashMap (Frequency Count)

Approach:
- Use a dictionary (hash_map) to count occurrences of each element
- Traverse the array and store frequency of each number
- Traverse the dictionary to find the element with frequency = 1

Key Observation:
- Every element appears exactly 3 times except one
- The required element appears only once → frequency == 1

Example:
nums = [0, 1, 0, 1, 0, 1, 99]

Step 1: Build frequency map
{
    0: 3,
    1: 3,
    99: 1
}

Step 2: Find element with frequency 1
- 0 → 3 (ignore)
- 1 → 3 (ignore)
- 99 → 1 (answer)

Final Answer = 99

Why this works:
- We explicitly count occurrences
- The unique element is the one with frequency exactly 1

Time Complexity:
- O(n) for building hashmap
- O(n) for checking → Overall O(n)

Space Complexity:
- O(n) → for storing hashmap

Note:
- This is NOT optimal as it uses extra space
- Optimal solution uses bit manipulation (bitwise counting)
"""
