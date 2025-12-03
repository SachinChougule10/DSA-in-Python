# This program performs a left rotation of the given array by one position.
# Left rotation by one place means each element shifts one step to the left, and the first element moves to the end of the array.


def left_rotate_by_one_place(nums):
    n = len(nums)
    temp = nums[0]  # store first element

    for i in range(1, n):
        nums[i - 1] = nums[i]  # shift elements left

    nums[n - 1] = temp  # place stored element at end

    print(nums)


nums = [3, 9, 5, 6, 7, 2, 10, 9]
left_rotate_by_one_place(nums)


# Logic:

# A left rotation by one place means shifting each element to the left,
# and moving the first element to the end.
# Step 1: Store the first element in temp.
# Step 2: Shift each element one position left.
# Step 3: Place temp at the end of the list.
# Time Complexity: O(n) since each element is shifted once.
# Space Complexity: O(1) because no extra array is used.
