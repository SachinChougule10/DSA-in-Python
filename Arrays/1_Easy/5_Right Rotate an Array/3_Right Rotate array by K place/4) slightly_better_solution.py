def right_rotate_by_k_place(nums):

    k = 10
    n = len(nums)

    k = k % n  # reduce extra full rotations

    nums[:] = nums[n - k :] + nums[: n - k]
    print(nums)


nums = [3, 9, 5, 6, 7, 2, 10, 9]
right_rotate_by_k_place(nums)


# version with k % n works for both:

# 1) when k < n
# 2) when k > n

# because modulo automatically reduces unnecessary full rotations


# Logic:

# This function rotates the array to the right by k positions using list slicing.
# First, k is reduced using k % n so that unnecessary full rotations are removed.
# Example: rotating an array of length 8 by k = 10 is the same as rotating it by 2.

# After reducing k, nums[n - k :] extracts the last k elements, and nums[: n - k]
# gives the remaining first part of the list. Concatenating these two slices forms
# the right-rotated result.

# nums[:] = ... ensures that the rotation happens in-place, meaning the same list
# object is updated instead of creating a new one.

# This approach works correctly for both:
#   - k < n
#   - k > n (handled automatically using modulo)

# Time Complexity: O(n)  → slicing and concatenation traverse the list.
# Space Complexity: O(n) → a new temporary list is created during concatenation.
