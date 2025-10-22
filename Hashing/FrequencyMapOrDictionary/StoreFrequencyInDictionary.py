nums = [5, 6, 7, 7, 1, 9, 111, 1, 5, 1, 1]

frequency_map = {}

for i in range(0, len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]] += 1
    else:
        frequency_map[nums[i]] = 1

print(frequency_map)
