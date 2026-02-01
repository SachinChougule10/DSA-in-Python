# GFG : Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. Return 0 if the target is not present (Brute Force Approach)


class Solution:
    def no_of_occurence(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # To store the first and last occurrence index of target
        first = -1
        last = -1

        # Traverse the array linearly (brute force)
        for i in range(n):
            # Check if current element matches the target
            if nums[i] == target:
                # If first occurrence is not set, set it
                if first == -1:
                    first = i
                # Update last occurrence every time target is found
                last = i

        # If target is never found in the array
        if first == -1:
            return 0

        # Number of occurrences = last index - first index + 1
        return (last - first) + 1


nums = [1, 1, 2, 2, 2, 2, 3]
obj = Solution()
print(obj.no_of_occurence(nums, 2))  # output : 4
print(obj.no_of_occurence(nums, 50))  # output : 0

"""
Logic (Brute Force Approach):

1. Initialize two variables:
   - first → to store the index of the first occurrence of target
   - last  → to store the index of the last occurrence of target

2. Traverse the array from left to right:
   - When target is found:
     - If first is not set, assign current index to first
     - Always update last to the current index

3. After traversal:
   - If first is still -1, the target does not exist → return 0
   - Otherwise, number of occurrences = (last - first) + 1

Time Complexity:
- O(n), where n is the size of the array (linear traversal)

Space Complexity:
- O(1), no extra space used
"""
