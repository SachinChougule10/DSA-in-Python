def right_rotate_by_k_place(nums, k):

    n = len(nums)
    rotations = k % n  # handle cases where k > n

    for _ in range(0, rotations):
        e = nums.pop()  # remove last element
        nums.insert(0, e)  # insert it at the beginning
    print(nums)


nums = [3, 9, 5, 6, 7, 2]
right_rotate_by_k_place(nums, 10)

# Logic:

# To rotate an array to the right by k positions, we first reduce unnecessary
# rotations using k % n because rotating n times results in the original array.

# For each rotation:
#   1. nums.pop() removes the last element.
#   2. nums.insert(0, e) inserts that element at the beginning.

# Repeating this process 'rotations' times rotates the list to the right by k steps.

# Time Complexity: O(k * n) → inserting at index 0 shifts all elements each time.
# Space Complexity: O(1)    → rotation happens in-place.
