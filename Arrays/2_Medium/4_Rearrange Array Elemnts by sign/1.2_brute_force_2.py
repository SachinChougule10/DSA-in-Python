class Solution:
    def rearrange_by_signs(self, nums: list[int]) -> list[int]:

        n = len(nums)
        positive_numbers = []  # store all positive numbers
        negative_numbers = []  # store all negative numbers

        # Separate positives and negatives while maintaining order
        for i in range(0, n):
            if nums[i] > 0:
                positive_numbers.append(nums[i])
            else:
                negative_numbers.append(nums[i])

        m = len(positive_numbers)

        # Place positives at even indices and negatives at odd indices
        for j in range(0, m):
            nums[j * 2] = positive_numbers[j]
            nums[(j * 2) + 1] = negative_numbers[j]

        return nums


nums = [3, 1, -2, -5, 2, -4]
obj = Solution()
print(obj.rearrange_by_signs(nums))

# Logic:

# 1. Traverse the array and store positive and negative numbers separately
#    while preserving their original order.
# 2. Iterate over the positives list and place:
#    - positive numbers at even indices (0, 2, 4, ...)
#    - negative numbers at odd indices (1, 3, 5, ...)
# 3. Return the modified array.

# Time Complexity:
# O(n) — one pass to separate elements and one pass to rearrange.

# Space Complexity:
# O(n) — extra space used to store positive and negative numbers.
