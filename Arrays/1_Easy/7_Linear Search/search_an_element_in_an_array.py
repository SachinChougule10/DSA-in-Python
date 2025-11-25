# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array.
# Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.


def linear_search(arr, x):

    n = len(arr)  # length of the array

    for i in range(0, n):  # iterate through each index of the array
        if arr[i] == x:  # check if current element matches the target
            return i  # return the index if target is found
    return -1  # if loop finishes without finding x, return -1


nums = [10, 8, 6, 7, 9, 6, 1, 2, 5]
print(linear_search(nums, 9))
print(linear_search(nums, 3))


# Logic:

# This function performs a simple linear search on the array.
# It scans each element from left to right and compares it with the target value x.
# If arr[i] == x, we immediately return the index i.
# If we finish scanning the entire array without finding x, we return -1.

# Time Complexity: O(n) — we may need to check each element once.
# Space Complexity: O(1) — no extra space is used apart from variables.
