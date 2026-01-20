class Solution:
    def maximum_product_subarray(self, nums: list[int]) -> int:
        n = len(nums)  # Length of the input array
        # left_product stores the product of elements when traversing from left to right
        left_product = 1
        # right_product stores the product of elements when traversing from right to left
        right_product = 1
        # max_product keeps track of the maximum product subarray found so far. Initialized with the first element to handle all-negative arrays
        max_product = nums[0]

        # Single loop to calculate both prefix and suffix products
        for i in range(n):
            # If left_product becomes 0, reset it to 1. This is because a subarray cannot benefit from multiplying further after 0
            left_product = 1 if left_product == 0 else left_product

            # If right_product becomes 0, reset it to 1. This allows starting a fresh subarray from the right side
            right_product = 1 if right_product == 0 else right_product

            # Calculate prefix product (subarray starting from the left)
            left_product = left_product * nums[i]

            # Calculate suffix product (subarray starting from the right)
            right_product = right_product * nums[n - 1 - i]

            # Update the maximum product by comparing:
            # 1. Previously found maximum product
            # 2. Current prefix product
            # 3. Current suffix product
            max_product = max(max_product, left_product, right_product)

        return max_product


nums = [2, 3, -2, 4]
obj = Solution()
print(obj.maximum_product_subarray(nums))  # output : 6


"""
Logic Explanation:
- The maximum product subarray problem is tricky due to the presence of negative numbers and zeros.
- A negative number can flip the sign of the product, and a zero breaks any ongoing subarray.

Approach:
- Traverse the array from left to right to compute prefix products.
- Simultaneously traverse from right to left to compute suffix products.
- If a product becomes zero, reset it to 1 to start a new subarray.
- At every index, compare the prefix product, suffix product, and the current maximum to find the best result.

Why this works:
- For an odd number of negative values, the maximum product subarray must exclude either the first or the last negative number.
- Prefix products effectively exclude the last negative.
- Suffix products effectively exclude the first negative.
- Taking the maximum at each step ensures the best valid subarray is chosen.

Prefix scan (left → right)
    Effectively tries removing the last negative because it considers subarrays that end before that negative.

Suffix scan (right → left)
    Effectively tries removing the first negative because it considers subarrays that start after that negative.

You don't explicitly remove anything — the direction of multiplication naturally skips it.

Edge Cases Handled:
- Arrays containing zeros
- Arrays containing all negative numbers
- Single-element arrays

Complexity:
- Time Complexity: O(n)
- Space Complexity: O(1)
"""
