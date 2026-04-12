# Leetcode : 260. Single Number III : Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice (Brute Force Solution)
# Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

# Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]

# Example 3:
# Input: nums = [0,1]
# Output: [1,0]

# Constraints:
# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.


class Solution:
    def single_number(self, nums: list[int]) -> list[int]:
        # Dictionary to store frequency of each element
        hash_map = {}
        # List to store elements appearing once
        result = []

        for num in nums:
            # Count frequency of each number
            hash_map[num] = hash_map.get(num, 0) + 1

        for num, value in hash_map.items():
            # Collect elements that appear exactly once
            if value == 1:
                result.append(num)

        # Return the two unique elements
        return result


obj = Solution()

nums = [1, 2, 1, 3, 2, 5]
print(obj.single_number(nums))  # Output : [3, 5]

"""
Logic: Brute Force using HashMap (Frequency Count)

Approach:
- Use a dictionary (hash_map) to count occurrences of each element
- Traverse the array and store frequency of each number
- Traverse the dictionary and collect elements with frequency = 1

Key Observation:
- Every element appears exactly twice except TWO elements
- Those two elements will have frequency == 1

Example:
nums = [1, 2, 1, 3, 2, 5]

Step 1: Build frequency map
{
    1: 2,
    2: 2,
    3: 1,
    5: 1
}

Step 2: Collect elements with frequency 1
- 1 → 2 (ignore)
- 2 → 2 (ignore)
- 3 → 1 (add)
- 5 → 1 (add)

Final Answer = [3, 5]  (order can vary)


Why this works:
- We explicitly count occurrences
- Elements appearing once are directly identified

Time Complexity:
- O(n) for building hashmap
- O(n) for traversal → Overall O(n)

Space Complexity:
- O(n) → for storing hashmap

Note:
- This is NOT optimal as it uses extra space
- Optimal solution uses XOR + bit manipulation

One-line intuition:
Count frequencies → pick elements with frequency 1
"""
