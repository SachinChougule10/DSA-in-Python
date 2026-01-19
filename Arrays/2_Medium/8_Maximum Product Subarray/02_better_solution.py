class Solution:
    def maximum_product_subarray(self, nums: list[int]) -> int:
        n = len(nums)
        # Stores the maximum product found so far
        max_product = float("-inf")
        # Loop to choose the starting index of the subarray
        for i in range(n):
            # Product of the current subarray beginning at index i
            product = 1
            # Loop to extend the subarray from index i to j
            for j in range(i, n):
                # Multiply current element to the running product
                product = product * nums[j]
                # Update maximum product if needed
                max_product = max(max_product, product)
        return max_product


nums = [2, 3, -2, 4]
obj = Solution()
print(obj.maximum_product_subarray(nums))

"""
Logic:
- This approach improves upon the brute force solution by reducing redundant product calculations.
- Instead of recalculating the product for every subarray, it reuses previously computed results.

Steps:
1. Use the outer loop to fix the starting index `i` of the subarray.
2. Initialize a variable `product` to 1 for each new starting index.
3. Use the inner loop to extend the subarray from index `i` to `j`.
4. Multiply the current element `nums[j]` with the running product.
5. After each multiplication, update the maximum product if the current subarray product is larger.
6. Continue expanding until the end of the array, then move to the next starting index.

Why it works:
- All contiguous subarrays are still evaluated.
- The running product avoids recomputing values, improving efficiency.

Complexity:
- Time Complexity: O(n²) due to two nested loops.
- Space Complexity: O(1) since only constant extra space is used.
"""
