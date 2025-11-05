def second_largest(nums):
    n = len(nums)  # Get length of the list
    nums.sort()  # Sort the list in ascending order

    return nums[n - 2]  # Return second last element (second largest)


nums = [55, 32, 97, -55, 45, 32, 88, 21]
print(second_largest(nums))
