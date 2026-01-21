# Leetcode : 704. Binary Search : Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def binary_search(self, nums: list[int], target) -> int:
        n = len(nums)  # Total number of elements in the array
        low = 0  # Starting index of the search space
        high = n - 1  # Ending index of the search space
        # result = -1

        # Continue searching while the search space is valid
        while low <= high:
            # Find the middle index of the current search space
            mid = (low + high) // 2

            # If the middle element is the target, return its index
            if nums[mid] == target:
                # Target found — for Leetcode 704, returning any valid index is sufficient, so we return immediately without checking for earlier occurrences.
                return mid

                # to check FIRST occurrence of the target in case of duplicates.(GFG version)
                # result = mid            # Store current index as a potential answer
                # high = mid - 1          # Continue searching in the left half

            # If target is greater than middle element, discard the left half and search in the right half
            elif nums[mid] < target:
                low = mid + 1
            # If target is smaller than middle element, discard the right half and search in the left half
            else:
                high = mid - 1

        # If the loop ends, the target does not exist in the array
        return -1


# true
nums = [-1, 0, 3, 5, 9, 12]
obj = Solution()
print(obj.binary_search(nums, 9))

"""
LOGIC EXPLANATION:

Binary Search works on the principle of divide and conquer.
Since the array is already sorted, we can repeatedly eliminate half of the search space.

1. Initialize two pointers:
   - low at the beginning of the array
   - high at the end of the array

2. Find the middle index using:
      mid = (low + high) // 2

3. Compare nums[mid] with the target:
   - If equal, we have found the target → return mid
   - If target is greater, ignore the left half (low = mid + 1)
   - If target is smaller, ignore the right half (high = mid - 1)

4. Repeat the process until:
   - The target is found, or
   - low becomes greater than high (target not present)


TIME COMPLEXITY:
- O(log n) → Search space is halved in every iteration

SPACE COMPLEXITY:
- O(1) → No extra space is used (iterative approach)

ADDITIONAL NOTE (First Occurrence Variant):

    In problems where the array may contain duplicate elements and the first occurrence of the target is required, we should NOT return
    immediately when nums[mid] == target.

    Instead:
    - Store the current index in a variable (e.g., result)
    - Move the search to the left half using: high = mid - 1
    - Continue the search to find the leftmost occurrence

    This modification is commonly used in:
    - First occurrence / last occurrence problems
    - Counting frequency of an element
    - Lower bound / upper bound type problems

    For Leetcode 704, this modification is unnecessary because returning any valid index of the target is acceptable.
"""
