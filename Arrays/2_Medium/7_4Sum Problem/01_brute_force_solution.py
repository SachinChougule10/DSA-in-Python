# Leetcode 18. 4Sum : Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
# such that: 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


class Solution:
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)  # Length of the array
        result = set()  # Set to store unique quadruplets
        # First loop: pick the first element
        for i in range(n):
            # Second loop: pick the second element
            for j in range(i + 1, n):
                # Third loop: pick the third element
                for k in range(j + 1, n):
                    # Fourth loop: pick the fourth element
                    for l in range(k + 1, n):
                        # Check if the sum of the selected four elements equals target
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            # Create a quadruplet
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()  # Sort to ensure same quadruplets are in same order
                            # Convert to tuple and add to set to avoid duplicates
                            result.add(tuple(temp))

        # Convert each tuple back to list before returning
        return [list(i) for i in result]


nums = [1, 0, -1, 0, -2, 2]
obj = Solution()
print(obj.four_sum(nums, 0))


"""
LOGIC:
1. We use four nested loops to generate all possible combinations of
   four distinct indices i, j, k, and l such that i < j < k < l.
2. For each combination, we check whether the sum of the four elements
   equals the given target.
3. If a valid quadruplet is found:
   - We sort it to maintain a consistent order.
   - We store it as a tuple in a set to eliminate duplicate quadruplets.
4. Finally, we convert the set of tuples into a list of lists and return it.

TIME COMPLEXITY:
- O(n⁴), since we are using four nested loops.

SPACE COMPLEXITY:
- O(m), where m is the number of unique quadruplets stored in the set.
"""
