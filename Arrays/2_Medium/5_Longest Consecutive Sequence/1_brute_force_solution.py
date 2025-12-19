# 128. Longest Consecutive Sequence:- Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        max_count = 0

        for i in range(0, n):
            num = nums[i]  # store current number variable - num
            count = 1

            while num + 1 in nums:  # check whether the next number is available in nums
                count += 1  # if next number is avialable, increase the count by one
                num += 1  # update num's value to it's next num
            max_count = max(max_count, count)
            # check whether, the current count of consecutive numbers is more or the previous count

        return max_count


# nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
obj = Solution()
print(obj.longestConsecutive(nums))


# Time complexity = O(n²)
# Space complexity = O(1)

"""
Logic:
- For each element in the array, treat it as the start of a possible sequence.
- Store the current number in a variable `num` and initialize count = 1.
- Keep checking if the next consecutive number (num + 1) exists in the array.
- If it exists, increment the count and move to the next number.
- Track the maximum length of consecutive numbers found so far.

Note:
- The check `num + 1 in nums` scans the array each time,
  which makes this a brute-force approach.

Time Complexity: O(n²)
- Outer loop runs n times.
- `num + 1 in nums` takes O(n) time.

Space Complexity: O(1)
- No extra data structures are used.
"""
