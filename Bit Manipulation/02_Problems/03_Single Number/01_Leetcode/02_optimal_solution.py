# Leetcode : 136. Single Number : Given a non-empty array of integers nums, every element appears twice except for one (Optimal Solution)
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
        # Initialize result to 0 (identity element for XOR)
        result = 0

        for num in nums:
            # XOR current number with result
            # duplicates cancel out because a ^ a = 0
            result = result ^ num  # eg :- ((((4 ^ 1) ^ 2) ^ 1) ^ 2)

        # The remaining value is the single number
        return result


nums = [4, 1, 2, 1, 2]

obj = Solution()
print(obj.single_number(nums))  # Output : 4

"""
Logic: XOR Approach for "Single Number"

Basic XOR Rules:
- a ^ a = 0
- a ^ 0 = a

XOR Properties:
1. Commutative:
   a ^ b = b ^ a

2. Associative:
   (a ^ b) ^ c = a ^ (b ^ c)

Because of this:
- Order of XOR does NOT matter
- Grouping of elements does NOT matter

Key Observations:
- Duplicate elements cancel out → a ^ a = 0
- Zero does not affect result → a ^ 0 = a

Conclusion:
When we XOR all elements in the array:
- All duplicate numbers cancel each other
- Only the unique number remains

One-line intuition:
XOR removes pairs → only the non-repeating element is left


--------------------------------------------------------------------

Example:
nums = [4, 1, 2, 1, 2]

We prove that ANY order or grouping gives same result

------------------------------------
Method 1 (left to right):
------------------------------------
res = 0
res = res ^ 4 = 4
res = res ^ 1 = 5
res = res ^ 2 = 7
res = res ^ 1 = 6
res = res ^ 2 = 4

Final Answer = 4


------------------------------------
Method 2 (pair duplicates first):
------------------------------------
(1 ^ 1) = 0
(2 ^ 2) = 0

Now:
4 ^ 0 ^ 0 = 4

Final Answer = 4


------------------------------------
Method 3 (random grouping):
------------------------------------
(4 ^ 1) ^ (2 ^ 1) ^ 2

Step-by-step:
4 ^ 1 = 5
2 ^ 1 = 3

Now:
5 ^ 3 ^ 2

5 ^ 3 = 6
6 ^ 2 = 4

Final Answer = 4


------------------------------------
Method 4 (completely shuffled):
------------------------------------
2 ^ 4 ^ 1 ^ 2 ^ 1

Group:
(2 ^ 2) ^ (1 ^ 1) ^ 4
= 0 ^ 0 ^ 4
= 4


------------------------------------
Why this ALWAYS works:
------------------------------------
- a ^ a = 0   → duplicates cancel
- XOR is commutative → order doesn't matter
- XOR is associative → grouping doesn't matter

So no matter how you reorder or group:
→ duplicates cancel
→ only the single number remains


Time Complexity: O(n)
Space Complexity: O(1)
"""
