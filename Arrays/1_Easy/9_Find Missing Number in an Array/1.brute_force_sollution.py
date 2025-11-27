# Question :- Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


def find_missing_number(nums):
    n = len(nums)

    for i in range(0, n + 1):  # Check each number from 0 to n
        if i not in nums:  # if number not present in the list
            return i  # return missing number


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(find_missing_number(nums))  # output :- 8

# Logic:

# The array contains numbers from 0 to n with exactly one missing.
# We loop from 0 to n and check which number is not present in the array.
# The first number that is not found in nums is the missing number.
# Time Complexity: O(n²) because the for-loop runs n+1 times, and each "i not in nums" check is O(n).
# Space Complexity: O(1) since no extra data structures are used.
