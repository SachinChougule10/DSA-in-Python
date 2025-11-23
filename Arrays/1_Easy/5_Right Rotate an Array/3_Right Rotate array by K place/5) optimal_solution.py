def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def right_rotate(nums, k):

    n = len(nums)
    k = k % n
    reverse(nums, n - k, n - 1)  # Step 1: reverse last k elements
    reverse(nums, 0, n - k - 1)  # Step 2: reverse first n-k elements
    reverse(nums, 0, n - 1)  # Step 3: reverse whole array

    print(nums)


nums = [3, 9, 5, 6, 7, 2, 10, 9]
right_rotate(nums, 5)


# LOGIC SUMMARY:

# This program rotates an array to the right by k positions
# using the Reversal Algorithm.

# Steps:
# 1. Reverse the last k elements.
# 2. Reverse the first n - k elements.
# 3. Reverse the entire array.

# Why this works:
# - Reversing parts and then the whole list rearranges elements exactly as a right rotation requires.
# - Works even when k > n because we use: k = k % n

# Time Complexity:  O(n)
# Space Complexity: O(1)   (no extra list created)

# Example:
# nums = [3, 9, 5, 6, 7, 2, 10, 9], k = 5
# After rotation → [7, 2, 10, 9, 3, 9, 5, 6]
