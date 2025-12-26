class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        my_set = set()  # store unique elements
        n = len(nums)
        longest = 0  # longest consecutive sequence length
        count = 0
        for i in range(0, n):
            my_set.add(nums[i])

        # Check sequences starting points
        for num in my_set:
            if num - 1 not in my_set:  # check if it's the start of a sequence
                x = num
                count = 1  # current sequence length

                # Count consecutive numbers
                while x + 1 in my_set:  # count consecutive numbers
                    count += 1
                    x += 1
                longest = max(longest, count)  # update longest sequence length
        return longest


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
obj = Solution()
print(obj.longestConsecutive(nums))


"""
Logic:
- Store all elements in a set to allow O(1) lookups.
- Iterate through the set and consider a number only if it is the
  start of a sequence (i.e., num - 1 is not present).
- From that starting number, keep checking num + 1, num + 2, ...
  to count the length of the consecutive sequence.
- Update the longest sequence length found.

Time Complexity:
- O(n): Each number is processed at most once.
- Set lookups are O(1) on average.

Space Complexity:
- O(n): Extra space used to store elements in the set.
"""
