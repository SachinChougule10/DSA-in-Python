# This file contains a function to left-rotate a list by 'k' positions.

# Left rotation means shifting each element to the left, and moving the
# first 'k' elements to the end of the list.

# Example:
# Input : [1,2,3,4,5,6,7,8,9], k = 3
# Output: [4,5,6,7,8,9,1,2,3]

# The implementation manually performs rotation without using Python slicing.


def left_rotate_by_k_places(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is larger than the list size

    temp = nums[0:k]  # Store the first k elements (these will move to the end)

    for i in range(k, n):  # Shift the remaining elements left by k positions
        nums[i - k] = nums[i]

    for j in range(n - k, n):  # Place stored elements at the end
        nums[j] = temp[j - (n - k)]

    print(nums)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
left_rotate_by_k_places(nums, 3)

# Logic:
# We store the first 'k' elements, shift the rest of the array left by 'k'
# positions, and place the stored elements at the end.

# Time Complexity: O(n) — every element is visited once.
# Space Complexity: O(k) — we store only the first 'k' elements.
