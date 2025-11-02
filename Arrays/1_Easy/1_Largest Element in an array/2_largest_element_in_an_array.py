def largest_element(nums):
    n = len(nums)
    largest_number = float("-inf")

    for i in range(0, n):
        largest_number = max(largest_number, nums[i])
    return largest_number


# nums = [55, 32, -97, 99, 3, 67]

nums = [-55, -32, -97, -99, -3, -67]
print(largest_element(nums))


# in this method by assigning largest_number = float("-inf"), even if all the numbers are negative in the array,
# we will get the correct largest number among all the negative numbers


# NOTE :- What happens when max () has same elements to be compared?

# The max(a, b) function:

# Returns the greater of the two values.

# If both are equal, it just returns that value (doesn’t matter which one).
# max (7,7) = 7

# So when all elements are the same, every comparison just returns that same value, and the largest number ends up being that value.
