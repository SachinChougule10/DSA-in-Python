def find_missing_number(nums):
    n = len(nums)

    return n * (n + 1) // 2 - sum(nums)
    # Using formula: sum of 0..n minus sum of nums gives the missing number


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(find_missing_number(nums))


# Logic:

# - The numbers should be from 0 to n with one missing.
# - Formula for sum of first n natural numbers (0..n) is: n*(n+1)//2.
# - Subtracting the sum of the array from the expected sum gives the missing number.

# Example:
#   expected_sum = 9*10/2 = 45
#   actual_sum = sum(nums) = 36
#   missing = 45 - 36 = 9

# Time Complexity: O(n) due to sum(nums)
# Space Complexity: O(1) since no extra data structures are used.
