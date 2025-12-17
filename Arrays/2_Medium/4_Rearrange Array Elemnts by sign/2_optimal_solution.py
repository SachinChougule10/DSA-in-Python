class Solution:
    def rearrange_by_sign(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n  # Result array of same size as of given array

        pos_index = 0  # Even indices for positive numbers
        negative_index = 1  # Odd indices for negative numbers

        # Traverse the input array
        for i in range(0, n):
            if nums[i] >= 0:
                result[pos_index] = nums[i]  # Place positive number
                pos_index += 2  # Move to next even index
            else:
                result[negative_index] = nums[i]  # Place negative number
                negative_index += 2  # Move to next odd index
        return result


nums = [3, 1, -2, -5, 2, -4]
obj = Solution()
print(obj.rearrange_by_sign(nums))


"""
Logic:
- Create a result array of the same size.
- Maintain two pointers:
  - pos_index for even indices (positive numbers)
  - negative_index for odd indices (negative numbers)
- Traverse the input array and place positives and negatives
  at their respective indices while preserving order.

Time Complexity: O(n)
Space Complexity: O(n)
"""
