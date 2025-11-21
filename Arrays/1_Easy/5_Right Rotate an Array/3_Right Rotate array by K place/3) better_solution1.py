def right_rotate_array_by_k_place(nums, k):

    n = len(nums)

    nums[:] = nums[n - k :] + nums[: n - k]
    print(nums)


nums = [3, 9, 5, 6, 7, 2, 10, 9]
right_rotate_array_by_k_place(nums, 5)


# If k > n, this code will break


# Logic:
# This function rotates the array to the right by k places using list slicing.
# First, nums[n - k :] extracts the last k elements of the list.
# Next, nums[: n - k] extracts the remaining first part of the list.
# Concatenating these two slices gives the right-rotated array.

# nums[:] = ... is used so the same list object is updated in-place instead of creating a new list reference.

# Important Note:
# This code assumes that k <= n. If k is greater than n, then the expression nums[n - k :] will not work as intended, causing incorrect slicing behavior.

# Time Complexity: O(n)  → slicing and concatenation each traverse the list.
# Space Complexity: O(n) → a new list is created during concatenation.
