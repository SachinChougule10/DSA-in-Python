nums = [5, 8, 1, 6, 9, 2, 4]

size = len(nums)

for i in range(size - 2, -1, -1):
    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
