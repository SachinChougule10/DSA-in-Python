def is_sorted(nums):
    n = len(nums)

    for i in range(0, n - 1):
        if nums[i + 1] < nums[i]:
            return False
    return True


nums = [3, 5, 6, 8, 9, 10, 20]
nums1 = [5, 1, 2, 3, 6, 9, 10]

print(is_sorted(nums))
print(is_sorted(nums1))

# Logic: The function checks if each next element is smaller than the previous one.
# If found, it returns False; otherwise, True — confirming ascending order.
