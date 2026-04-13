# Leetcode : 260. Single Number III : Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice (Optimal Solution)
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
        n = len(nums)
        XOR = 0  # Will store XOR of all elements

        for i in range(n):
            # All pairs cancel out → we get XOR of the two unique numbers
            # Since there are two unique numbers, they must differ in at least one bit
            XOR = XOR ^ nums[i]

        # This isolates the rightmost set bit (the bit where the two unique numbers differ)
        right_most = (XOR & (XOR - 1)) ^ XOR  # OR right_most = XOR & (-XOR)

        # We will use this bit to divide numbers into two groups (b1 and b2)
        b1, b2 = 0, 0

        for i in range(n):
            # If the rightmost bit is set → result is non-zero → add to b1
            # If not set → result is zero → add to b2
            if nums[i] & right_most:
                b1 = b1 ^ nums[i]
            else:
                b2 = b2 ^ nums[i]

        # The two unique elements will fall into different buckets
        # Duplicate elements go into the same bucket and cancel out using XOR
        # Finally, b1 and b2 each contain one unique element
        return [b1, b2]


obj = Solution()

nums = [1, 2, 1, 3, 2, 5]
print(obj.single_number(nums))  # Output : [3, 5]

"""
Logic: Optimal XOR + Bit Manipulation (Very Detailed Explanation)

Problem:
- Every element appears twice except TWO elements
- Find those two unique elements
--------------------------------------------------------------------

Step 1: XOR all elements

XOR = 0
for num in nums:
    XOR ^= num

What happens here?

- Duplicate numbers cancel out:
    a ^ a = 0

Example:
nums = [1, 2, 1, 3, 2, 5]

XOR = 1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5
    = (1 ^ 1) ^ (2 ^ 2) ^ (3 ^ 5)
    = 0 ^ 0 ^ (3 ^ 5)
    = 6

So:
XOR = 3 ^ 5

Now XOR contains the XOR of the two unique numbers

--------------------------------------------------------------------

Step 2: Find a differentiating bit

right_most = XOR & -XOR

Example:
XOR = 6 → binary: 110

-XOR (2's complement):
6  = 00000110
-6 = 11111010

Now:
6 & -6 = 00000010 = 2

This keeps ONLY the rightmost set bit

Meaning:
- This bit is different between the two unique numbers
- One number has this bit = 1
- Other has this bit = 0

--------------------------------------------------------------------

Step 3: Divide numbers into two groups

We use:
if num & right_most

What does this mean?

It checks whether the current number has that specific bit

Case 1:
num & right_most != 0
→ bit is present → goes to bucket b1

Case 2:
num & right_most == 0
→ bit not present → goes to bucket b2

--------------------------------------------------------------------

Step 4: Apply grouping on example

nums = [1, 2, 1, 3, 2, 5]
right_most = 2 (binary: 010)

Check each number:

1 → 001 & 010 = 0 → goes to b2
2 → 010 & 010 = 2 → goes to b1
1 → 001 & 010 = 0 → goes to b2
3 → 011 & 010 = 2 → goes to b1
2 → 010 & 010 = 2 → goes to b1
5 → 101 & 010 = 0 → goes to b2

Buckets:

b1 = [2, 3, 2]
b2 = [1, 1, 5]

--------------------------------------------------------------------

Step 5: XOR inside each bucket

Bucket b1:
2 ^ 2 ^ 3 = 3

Bucket b2:
1 ^ 1 ^ 5 = 5

Duplicates cancel out inside each bucket

--------------------------------------------------------------------

Final Answer:
[3, 5]

--------------------------------------------------------------------

Why this works:

- The two unique numbers differ in at least one bit
- That bit is used to separate them into different buckets
- Duplicate numbers always go into the SAME bucket
- So they cancel out using XOR
- Each bucket is left with exactly one unique number

--------------------------------------------------------------------

Key Intuition:

1. XOR everything → get XOR of two unique numbers
2. Find a bit where they differ
3. Split numbers using that bit
4. XOR each group separately

--------------------------------------------------------------------

One-line intuition:

Use XOR to cancel duplicates → use a differing bit to split → XOR again to get both unique numbers

--------------------------------------------------------------------

Time Complexity: O(n)
Space Complexity: O(1)
"""
