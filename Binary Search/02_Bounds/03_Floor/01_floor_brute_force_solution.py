# Problem: This program finds the FLOOR of a given target value in a sorted array using brute force
# Definition:The floor of a given target value is the largest element in the array that is less than or equal to the target.
# floor = largest number in an array <= target


class Solution:
    def floor(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # ans is used to store the floor value. If no element <= target exists, ans will remain -1.
        ans = -1

        # Traverse each element in the array
        for i in range(n):
            # Check if current element is <= target
            if nums[i] <= target:
                # Update ans with the maximum valid value so far
                ans = max(ans, nums[i])
        return ans


nums = [10, 20, 30, 40, 50]
obj = Solution()
print(obj.floor(nums, 25))  # output : 20

"""
Logic Summary:

1. Initialize ans as -1 to handle cases where no floor exists.
2. Traverse the array element by element.
3. If an element is less than or equal to the target:
   - Compare it with the current ans.
   - Store the larger value.
4. After the loop, ans contains the largest element <= target.
5. If no such element exists, ans remains -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""
