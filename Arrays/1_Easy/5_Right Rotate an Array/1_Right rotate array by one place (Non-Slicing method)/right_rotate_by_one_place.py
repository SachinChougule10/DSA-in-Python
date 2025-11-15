def rotate_array_by_one_place(nums):

    n = len(nums)
    temp = nums[n - 1]  # store last element of the array in a variable

    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]

    nums[0] = temp
    # replace the first element of the current array with temp i.e. last element of the previous array

    return nums


nums = [5, -2, 3, 9, 0, 6, 10, 7]
print(rotate_array_by_one_place(nums))


# Logic:

# The goal is to rotate the array to the right by one position.
# We first store the last element of the array in a temporary variable.

# Then we shift every element one step to the right:
#  - Starting from the second-last element and moving backward, each element is moved to the position i+1.

# After completing the shift, the last element (stored in temp)
# is placed at index 0, achieving the right rotation by one place.

# Time Complexity: O(n)   → We traverse the array once in reverse.
# Space Complexity: O(1)  → No extra space except one temporary variable.
