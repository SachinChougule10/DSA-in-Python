def right_rotate_by_k_place(nums):

    k = 3  # we have to rotate the array 3 times

    for _ in range(0, k):
        e = nums.pop()  # remove last element
        nums.insert(0, e)  # place it at the begining
    print(nums)


nums = [3, 9, 5, 6, 7, 2]
right_rotate_by_k_place(nums)


# Logic:

# To rotate the array to the right by k positions, we repeatedly move the last
# element to the front.

# For each rotation:
#   1. nums.pop() removes and returns the last element.
#   2. nums.insert(0, e) places that element at the beginning.

# Repeating this process k times results in a right rotation by k steps.

# Note:
# - This method is simple but not the most optimal for large lists, as insert(0, ...) has O(n) complexity.

# Time Complexity: O(k * n)  → each insertion at index 0 shifts elements.
# Space Complexity: O(1)      → operations are done in-place.
