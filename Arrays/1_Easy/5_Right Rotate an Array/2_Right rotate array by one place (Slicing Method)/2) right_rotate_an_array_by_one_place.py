def right_rotate_by_one_place(nums):

    n = len(nums)
    nums[:] = [nums[n - 1]] + nums[0 : n - 1]

    return nums


nums = [5, -2, 3, 9, 0, 6, 10, 7]
print(right_rotate_by_one_place(nums))


# Logic:

# To rotate the array to the right by one place, we take the last element of the
# array (nums[-1]) and place it at the beginning. The remaining part of the list
# (nums[0 : n-1]) is appended after it.

# nums[:] = ... ensures that the rotation happens in-place, meaning the same list
# object is modified rather than creating a new one. This is useful when other
# variables reference the same list.

# Example:
# Input:  [5, -2, 3, 9, 0, 6, 10, 7]
# Output: [7, 5, -2, 3, 9, 0, 6, 10]

# Time Complexity: O(n)  → slicing operations traverse the list once.
# Space Complexity: O(n) → a new temporary list is created while concatenating.
