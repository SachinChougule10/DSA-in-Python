# Leetcode : 1) Two Sum :- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(nums, target):
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [5, 9, 1, 2, 4, 15, 6, 3]
print(twoSum(nums, 13))


# Logic:
# The function checks every possible pair of numbers in the list.
# It uses two nested loops — the outer loop picks one number (nums[i]),
# and the inner loop checks all numbers after it (nums[j]).
# If their sum equals the target, their indices [i, j] are returned.
# This is a brute-force approach with Time Complexity =  O(n²)
