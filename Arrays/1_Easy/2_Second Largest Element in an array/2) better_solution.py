def second_largest(nums):
    n = len(nums)
    largest_number = float("-inf")
    second_largest_number = float("-inf")

    for i in range(0, n):
        largest_number = max(largest_number, nums[i])

    for i in range(0, n):
        if nums[i] > second_largest_number and nums[i] != largest_number:
            second_largest_number = nums[i]

    return -1 if second_largest_number == float("-inf") else second_largest_number


nums = [55, 32, 97, -55, 45, 32, 88, 21]
nums1 = [10]

print(second_largest(nums))
print(second_largest(nums1))
