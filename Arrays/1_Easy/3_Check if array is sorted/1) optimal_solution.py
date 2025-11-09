def is_sorted(nums):
    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


nums = [3, 5, 6, 8, 9, 10, 20]
nums1 = [5, 1, 2, 3, 6, 9, 10]

print(is_sorted(nums))
print(is_sorted(nums1))

# Logic: Iterates through the list and compares each element with the next.
# Returns False if any element is greater than the next; otherwise, True.
