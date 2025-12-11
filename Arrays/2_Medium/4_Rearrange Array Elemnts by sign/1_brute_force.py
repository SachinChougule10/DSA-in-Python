# Leetcode 2149 :- Rearrange Array Elements by Sign

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should return the array of nums such that the array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


class Solution:
    def rearrange_by_sign(self, nums: list[int]) -> list[int]:

        n = len(nums)
        positive_numbers = []  # stores all positive numbers in order
        negative_numbers = []  # stores all negative numbers in order

        # Separate positive and negative numbers
        for i in range(0, n):
            if nums[i] > 0:
                positive_numbers.append(nums[i])
            else:
                negative_numbers.append(nums[i])

        m = len(positive_numbers)  # count of positive numbers
        final = []

        # Build the final array by alternating positive and negative
        for j in range(0, m):
            final.append(positive_numbers[j])  # add positive
            final.append(negative_numbers[j])  # add negative

        return final


nums = [3, 1, -2, -5, 2, -4]
obj = Solution()
print(obj.rearrange_by_sign(nums))

# Logic:

# - First, split the array into two lists: one for positive numbers, one for negative numbers.
# - Because the input guarantees equal count, we can alternate them easily.
# - We then build the result by taking one positive and then one negative (preserving their order).
# - Since each number is processed once, this approach works efficiently.

# Time Complexity: O(n)   → One pass to split + one pass to merge.
# Space Complexity: O(n)  → Extra space for two temporary lists and the final result.
