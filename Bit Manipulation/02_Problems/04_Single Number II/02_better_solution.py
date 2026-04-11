# Leetcode : 137. Single Number II : Given an integer array nums where every element appears three times except for one, which appears exactly once (Better Solution)
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
        # Final result
        ans = 0

        # Iterate through all 32 bits (for integer representation)
        for bit_index in range(0, 32):
            # Count of set bits at current position
            count = 0

            for num in nums:
                # Check if current bit is set in num
                if num & (1 << bit_index):
                    count += 1

            # If count % 3 == 1 → this bit belongs to the unique number
            if count % 3 == 1:
                # Set that bit in answer
                ans = ans | (1 << bit_index)

        return ans


obj = Solution()

nums = [0, 1, 0, 1, 0, 1, 99]
print(obj.single_number(nums))  # Output : 99

"""
Logic: Bit Manipulation (Bit Counting Approach)

Idea:
- Instead of counting numbers, count bits at each position (0 to 31)
- Every number appears 3 times except one
- So, bits contributed by repeating numbers will be multiples of 3

Approach:
1. For each bit position (0 to 31):
   - Count how many numbers have that bit set
2. If count % 3 == 1:
   - That bit belongs to the unique number
3. Construct the result using those bits

Key Observation:
- Bits of numbers appearing 3 times → contribute in multiples of 3
- Unique number contributes extra bits → count % 3 = 1

Example:
nums = [0, 1, 0, 1, 0, 1, 99]

Binary:
0  → 00000000
1  → 00000001
99 → 01100011

Bit counting:
- For each bit position, sum all bits
- Bits from 0 and 1 repeat 3 times → multiples of 3
- Bits from 99 remain → count % 3 = 1

Final Answer = 99


Why this works:
- We isolate each bit independently
- Remove contribution of numbers appearing 3 times using modulo
- Rebuild the unique number from remaining bits

Time Complexity:
- O(32 * n) ≈ O(n)

Space Complexity:
- O(1)

Important Note:
- Works for negative numbers as well (with proper 32-bit handling if needed)

One-line intuition:
Count bits → remove multiples of 3 → rebuild the unique number
"""
