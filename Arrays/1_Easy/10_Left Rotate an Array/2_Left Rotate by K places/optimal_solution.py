def reverse_array(nums, left, right):
    # Helper function to reverse elements in-place between two indices
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def left_rotate_by_k_place(nums, k):
    # Left rotate the array by k positions using the reversal algorithm
    n = len(nums)

    k = k % n  # Handle cases where k > n

    reverse_array(nums, 0, k - 1)  # Step 1: Reverse first k elements
    reverse_array(nums, k, n - 1)  # Step 2: Reverse the remaining elements
    reverse_array(nums, 0, n - 1)  # Step 3: Reverse the whole array

    print(nums)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
left_rotate_by_k_place(nums, 3)


# Logic:

# Use the reversal algorithm:
# 1. Reverse first k elements
# 2. Reverse remaining elements
# 3. Reverse the entire array

# Time Complexity: O(n) — each element is swapped a constant number of times.
# Space Complexity: O(1) — rotation done in-place without extra space.
