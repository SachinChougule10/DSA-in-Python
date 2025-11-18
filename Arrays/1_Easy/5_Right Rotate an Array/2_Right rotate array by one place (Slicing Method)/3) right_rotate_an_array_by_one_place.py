def right_rotate_by_one_place(nums):

    n = len(nums)

    nums[:] = nums[-1:-2:-1] + nums[0 : n - 1]
    # using list slicing and concatenate both, one in reverse way and one in normal way

    return nums


nums = [5, -2, 3, 9, 0, 6, 10, 7]
print(right_rotate_by_one_place(nums))


# Logic:

# To rotate the array to the right by one place, we take the last element of the
# list and place it at the front. This is achieved using list slicing:

# nums[-1:-2:-1] → returns the last element as a list (e.g., [7])
# nums[0:n-1]    → gives the sublist containing all elements except the last one

# Concatenating these two parts forms the rotated list:
#     [last_element] + [remaining_elements]

# The assignment nums[:] = ... ensures that the rotation happens in-place,
# meaning the same list object is updated instead of creating a new one. This is
# useful when multiple variables reference the same list.

# Time Complexity: O(n)  → slicing traverses the list once.
# Space Complexity: O(n) → a new temporary list is created during concatenation.
