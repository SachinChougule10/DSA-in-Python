# Question :- Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


def remove_duplicates(nums):
    n = len(nums)

    freq_map = {}  # To store unique elements

    for i in range(0, n):
        freq_map[nums[i]] = 0  # Insert element as key (removes duplicates)

    j = 0

    for k in freq_map:  # Copy unique keys back to list
        nums[j] = k
        j += 1

    return j  # Return count of unique elements


nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]

print(remove_duplicates(nums))

# Logic: Using a dictionary to keep only unique elements, then rewriting them into the list.
