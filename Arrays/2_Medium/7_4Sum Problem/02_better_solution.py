class Solution:
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)  # Length of the array
        result = set()  # Set to store unique quadruplets

        # First loop: pick the first element
        for i in range(n):
            # Second loop: pick the second element
            for j in range(i + 1, n):
                # HashSet used to solve the remaining part as a 2-sum problem. It stores numbers we have already seen while iterating k
                my_set = set()
                # Third loop: pick the third element
                for k in range(j + 1, n):
                    # Calculate the required fourth element
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    # If the fourth element is already seen, we found a valid quadruplet
                    if fourth in my_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        # Sort to keep a consistent order
                        temp.sort()
                        # Store as tuple in the set to avoid duplicates
                        result.add(tuple(temp))
                    # Add current element to the set for future checks
                    my_set.add(nums[k])
        # Convert result back to list of lists
        return [list(i) for i in result]


nums = [1, 0, -1, 0, -2, 2]
obj = Solution()
print(obj.four_sum(nums, 0))

"""
LOGIC:
1. The problem requires finding four distinct numbers whose sum equals the target.
2. We fix the first two numbers using two nested loops (indices i and j).
3. After fixing nums[i] and nums[j], the problem reduces to a 2-sum problem:
      nums[k] + nums[l] = target - (nums[i] + nums[j])
4. We solve this 2-sum efficiently using a hash set:
   - While iterating index k, we calculate the required fourth value.
   - If the required value already exists in the set, a valid quadruplet is found.
5. Each valid quadruplet is sorted and stored as a tuple inside a set
   to eliminate duplicate results.
6. Finally, the set of unique quadruplets is converted into a list of lists.

TIME COMPLEXITY:
- O(n³)
  - Two loops for fixing i and j
  - One loop for k with O(1) hash lookups

SPACE COMPLEXITY:
- O(n) for the hash set used in the inner loop (2-sum storage)
- O(m) for storing unique quadruplets, where m is the number of valid results
- Overall space complexity: O(n + m)
"""
