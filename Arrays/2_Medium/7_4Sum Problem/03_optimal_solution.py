class Solution:
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        result = []
        # Step 1: Sort the array
        nums.sort()

        # Step 2: Fix the first element
        for i in range(n):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Step 3: Fix the second element
            for j in range(i + 1, n):
                # Skip duplicate values for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Step 4: Initialize two pointers
                k = j + 1  # left pointer
                l = n - 1  # right pointer

                # Step 5: Two-pointer traversal
                while k < l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    # Need a bigger sum → move left pointer
                    if total_sum < target:
                        k += 1
                    # Need a smaller sum → move right pointer
                    elif total_sum > target:
                        l -= 1
                    # Found a valid quadruplet
                    else:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        result.append(temp)

                        # Move both pointers
                        k += 1
                        l -= 1

                        # Skip duplicates for k
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        # Skip duplicates for l
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        return result


nums = [1, 0, -1, 0, -2, 2]
obj = Solution()
print(obj.four_sum(nums, 0))  # output : [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

"""
Logic:
1. Sort the input array to enable the two-pointer technique and handle duplicates easily.

2. Use two nested loops:
   - The first loop fixes the first number (i).
   - The second loop fixes the second number (j).

3. For each fixed pair (i, j), use two pointers:
   - `k` starts from j + 1
   - `l` starts from the end of the array

4. Compute the sum of the four selected numbers:
   - If the sum is less than the target, move `k` forward.
   - If the sum is greater than the target, move `l` backward.
   - If the sum equals the target, store the quadruplet.

5. After finding a valid quadruplet:
   - Move both pointers (`k++`, `l--`)
   - Skip duplicate values to ensure only unique quadruplets are added.

6. Continue this process until all possible unique quadruplets that sum to the target are found.

Result:
The algorithm returns a list of all unique quadruplets whose sum is equal to the given target.
"""
