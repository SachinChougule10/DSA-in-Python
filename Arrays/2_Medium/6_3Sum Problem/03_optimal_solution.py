class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)  # total number of elements
        result = []  # stores final triplets
        # Sort the array to: 1) Apply the two-pointer technique, 2) Easily skip duplicate values
        nums.sort()

        # Fix the first element of the triplet
        for i in range(n):
            # Skip duplicate values for the first element. This prevents repeating the same triplet
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers:
            j = i + 1  # left pointer
            k = n - 1  # right pointer

            # Move pointers until they cross
            while j < k:
                # Calculate the sum of current triplet
                total_sum = nums[i] + nums[j] + nums[k]
                # If sum is smaller than 0, move left pointer right to increase sum
                if total_sum < 0:
                    j += 1
                # If sum is greater than 0, move right pointer left to decrease sum
                elif total_sum > 0:
                    k -= 1
                # If sum is exactly 0, we found a valid triplet
                else:
                    temp = [nums[i], nums[j], nums[k]]  # valid triplet found
                    result.append(temp)

                    # Move both pointers inward
                    j += 1
                    k -= 1
                    # skip duplicate second element, ensures unique triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # skip duplicate third element, ensures unique triplets
                    while j < k and nums[k] == nums[k + 1]:
                        k += 1
        return result


nums = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.three_sum(nums))


"""
1. The array is first sorted so that:
   - Two-pointer technique can be applied
   - Duplicate triplets can be skipped easily

2. We fix one element nums[i] using a loop.

3. For each fixed nums[i], we use two pointers:
   - j starts just after i (left pointer)
   - k starts at the end of the array (right pointer)

4. We calculate:
      total_sum = nums[i] + nums[j] + nums[k]

5. If total_sum < 0:
   - Move j to the right to increase the sum

6. If total_sum > 0:
   - Move k to the left to decrease the sum

7. If total_sum == 0:
   - A valid triplet is found and added to the result
   - Move both pointers inward

8. Duplicate values are skipped:
   - For i to avoid repeated first elements
   - For j and k to avoid repeated triplets

9. The process continues until all unique triplets are found.

10. Time Complexity:
        O(n²)
        - Sorting the array takes O(n log n) time.
        - The outer loop runs O(n) times to fix the first element.
        - For each fixed element, the two-pointer scan runs in O(n) time.
        - Since O(n²) dominates O(n log n), the overall time complexity is O(n²).

11. Space Complexity:
        O(1)
        - Only a constant amount of extra space is used for pointers and variables.
        - The array is sorted in place.
        - No additional data structures are used.
        - Space used to store the output triplets is excluded from auxiliary space.
"""
