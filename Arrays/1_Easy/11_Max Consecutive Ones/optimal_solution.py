# Leetcode 485 : Max Consecutive Ones
# Qusetion :- Given a binary array nums, return the maximum number of consecutive 1's in the array.


def max_consecutive_ones(nums):
    n = len(nums)

    count = 0  # current streak of 1s
    max_count = 0  # longest streak found

    for i in range(0, n):
        if nums[i] == 1:
            count += 1  # extend streak
        else:
            max_count = max(max_count, count)  # update max streak
            count = 0  # reset streak

    return max(max_count, count)  # final check in case array ends with 1s


nums = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(nums))

# Logic:
# We maintain a counter for consecutive 1s.
# Each time we encounter a 1 → increase count.
# When we encounter a 0 → update max_count and reset count.
# After the loop, we return the maximum of max_count and count (handles ending with 1s).

# Time Complexity: O(n) — one pass through the array.
# Space Complexity: O(1) — only constant extra variables used.
