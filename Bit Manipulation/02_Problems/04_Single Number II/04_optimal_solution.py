# Leetcode : 137. Single Number II : Given an integer array nums where every element appears three times except for one, which appears exactly once (Optimal Solution)
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
        # Will store bits appearing once
        ones = 0

        # Will store bits appearing twice
        twos = 0

        for num in nums:
            # Step 1: Add current number to 'ones' if not present in 'twos'
            ones = (ones ^ num) & ~twos

            # Step 2: Add current number to 'twos' if not present in updated 'ones'
            twos = (twos ^ num) & ~ones

        # After 3 occurrences:
        # number goes → ones → twos → removed (both become 0)

        # Only the element appearing once remains
        return ones


obj = Solution()

nums = [0, 1, 0, 1, 0, 1, 99]
print(obj.single_number(nums))  # Output : 99

# 0 → ones → twos → removed → ones → ...

"""
Logic: Optimal Bit Manipulation using Ones & Twos

Core Idea:
- Track occurrences modulo 3 using two variables:
  - ones → bits seen once
  - twos → bits seen twice
- When a number appears 3 times → it gets removed

Formulas:
ones = (ones ^ num) & ~twos
twos = (twos ^ num) & ~ones

--------------------------------------------------------------------

Detailed Dry Run:
nums = [0, 1, 0, 1, 0, 1, 99]

Initial:
ones = 0, twos = 0

Step 1: num = 0
ones = (0 ^ 0) & ~0 = 0
twos = (0 ^ 0) & ~0 = 0
→ ones = 0, twos = 0

Step 2: num = 1
ones = (0 ^ 1) & ~0 = 1
twos = (0 ^ 1) & ~1 = 0
→ ones = 1, twos = 0   (1st occurrence)

Step 3: num = 0
ones = (1 ^ 0) & ~0 = 1
twos = (0 ^ 0) & ~1 = 0
→ ones = 1, twos = 0

Step 4: num = 1 (2nd time)
ones = (1 ^ 1) & ~0 = 0
twos = (0 ^ 1) & ~0 = 1
→ ones = 0, twos = 1   (2nd occurrence)

Step 5: num = 0
ones = (0 ^ 0) & ~1 = 0
twos = (1 ^ 0) & ~0 = 1
→ ones = 0, twos = 1

Step 6: num = 1 (3rd time)
ones = (0 ^ 1) & ~1 = 0
twos = (1 ^ 1) & ~0 = 0
→ ones = 0, twos = 0   (removed after 3rd occurrence)

Step 7: num = 99
ones = (0 ^ 99) & ~0 = 99
twos = (0 ^ 99) & ~99 = 0
→ ones = 99, twos = 0

Final Answer:
ones = 99
--------------------------------------------------------------------

Pattern to Remember:
1st occurrence → ones
2nd occurrence → twos
3rd occurrence → removed (both reset to 0)
--------------------------------------------------------------------

Why this works:
- Each bit cycles through:
  ones → twos → removed (mod 3 behavior)
- Effectively simulates count % 3 without extra space
- Only the unique element (appearing once) remains in 'ones'

Time Complexity: O(n)
Space Complexity: O(1)

One-line intuition:
Simulate count % 3 using two bitmasks (ones & twos)
"""
