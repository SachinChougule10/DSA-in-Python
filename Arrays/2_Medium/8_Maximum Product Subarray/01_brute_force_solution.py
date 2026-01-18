# Leetcode : 152. Maximum Product Subarray. Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Note that the product of an array with a single element is the value of that element.


class Solution:
    def maximum_product_subarray(self, nums: list[int]) -> int:
        n = len(nums)
        # Stores the maximum product found so far
        max_product = float("-inf")
        # Loop to choose the starting index of the subarray
        for i in range(n):
            # Loop to choose the ending index of the subarray
            for j in range(i, n):
                # Product of the current subarray nums[i..j]
                product = 1
                # Loop to calculate product of elements from i to j
                for k in range(i, j + 1):
                    product = nums[k] * product
                # Update maximum product if current subarray product is larger
                max_product = max(max_product, product)

        return max_product


nums = [2, 3, -2, 4]
obj = Solution()
print(obj.maximum_product_subarray(nums))

"""
Logic:
- The goal is to find the maximum product of any possible contiguous subarray.
- To guarantee correctness, this approach checks every possible subarray.

Steps:
1. Use the first loop to fix the starting index `i` of the subarray.
2. Use the second loop to fix the ending index `j` of the subarray.
3. For each pair (i, j), compute the product of elements from index i to j using a third loop.
4. Track the maximum product encountered across all subarrays.
5. Return the maximum product after all combinations are evaluated.

Why it works:
- Every contiguous subarray is examined exactly once.
- The product of each subarray is computed independently, ensuring accuracy.

Complexity:
- Time Complexity: O(n³) due to three nested loops.
- Space Complexity: O(1) since only constant extra space is used.
"""
