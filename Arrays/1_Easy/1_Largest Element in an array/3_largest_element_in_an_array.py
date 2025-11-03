def largest_element(nums):

    n = len(nums)
    largest_number = float("-inf")

    for i in range(0, n):
        if nums[i] > largest_number:
            largest_number = nums[i]

    return largest_number


nums = [55, 32, -97, 99, 3, 67]
print(largest_element(nums))


# use this method (using 'if statement') if interviewer ask you not to use inbuilt 'max()' function
