def bubble_sort(nums):

    n = len(nums)
    for i in range(n - 2, -1, -1):
        is_swapped = False

        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True

        if is_swapped == False:
            return nums
    return nums


nums = [1, 2, 4, 5, 9, 10, 12, 3, 14]
print(bubble_sort(nums))
