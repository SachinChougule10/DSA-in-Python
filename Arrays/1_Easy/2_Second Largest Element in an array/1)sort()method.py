def second_largest(nums):
    nums.sort()  # Sort the list in ascending order
    return nums[-2]  # Return second last element directly


nums = [55, 32, 97, -55, 45, 32, 88, 21]
print(second_largest(nums))
