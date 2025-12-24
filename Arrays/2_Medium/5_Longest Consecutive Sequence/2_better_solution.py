class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()  # sort the list
        n = len(nums)
        last_smallest = float("-inf")  # previous number
        count = 0  # current streak length
        longest = 0  # longest streak found

        for i in range(n):
            if nums[i] - 1 == last_smallest:  # check for consecutive number
                count += 1
                last_smallest = nums[i]
            elif nums[i] != last_smallest:  # not consecutive and not duplicate
                count = 1
                last_smallest = nums[i]
            longest = max(longest, count)  # update longest streak
        return longest


# If current number is duplicate (nums[i] == last_smallest)both conditions above fail, so nothing happens.Duplicates are ignored automatically.

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
obj = Solution()
print(obj.longestConsecutive(nums))


# Time complexity = O(nlogn + n) = O(nlogn)
# Space complexity = O(1)

"""
Logic:
- Sort the array to bring consecutive numbers next to each other.
- Traverse the sorted array while tracking the current consecutive streak.
- If the current number is exactly 1 greater than the previous, extend the streak.
- If it is a duplicate, ignore it.
- Otherwise, reset the streak count.
- Keep updating the maximum streak length found.

Time Complexity:
- Sorting takes O(n log n)
- Single traversal takes O(n)
- Overall: O(n log n)

Space Complexity:
- O(1) (sorting is done in-place)
"""
