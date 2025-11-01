def largest_number(nums):
    n = len(nums)
    largest_number = nums[0]

    for i in range(0, n):
        largest_number = max(largest_number, nums[i])
    return largest_number


nums = [55, 32, -97, 99, 3, 67]
print(largest_number(nums))

# the problem with this method (assigning largest_number = 0), is that, if all the numbers in the array are negative,
# then the largest number will always be zero as we assigned largest_number = 0 and if all numbers are neagtive,
# even if we iterate through all the numbers in the array none of them will be greater than largest_number = 0
