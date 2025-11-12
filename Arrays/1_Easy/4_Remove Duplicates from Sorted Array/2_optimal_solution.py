def remove_duplicates(nums):

    n = len(nums)
    i = 0
    j = i + 1

    if n == 1:
        return 1

    while j < n:
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1  # we need to move forward 'j' no matter if elements are same or not

    return i + 1


nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
nums1 = [10]
print(remove_duplicates(nums))
print(remove_duplicates(nums1))

# Logic:
# This solution uses a two-pointer approach.
# 'i' tracks the position of the last unique element,
# while 'j' scans through the array to find the next unique element.
# When a new unique value is found, it is swapped to the next position of 'i'.
# The function finally returns i + 1, representing the count of unique elements in-place.
