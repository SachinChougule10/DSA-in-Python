# 350. Intersection of Two Arrays II. Given two integer arrays nums1 and nums2, return an array of their intersection (Optimal Solution)
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # store frequency of elements from nums1
        freq = Counter(nums1)

        # final intersection array
        result = []

        # traverse nums2
        for num in nums2:

            # if element exists in freq map
            # and frequency is greater than 0
            if freq[num] > 0:

                # add common element
                result.append(num)

                # decrease frequency
                freq[num] -= 1

        # return final result
        return result


# Example Usage
obj = Solution()

print(obj.intersect([1, 2, 2, 1], [2, 2]))  # Output : [2, 2]
print(obj.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output : [9, 4]

"""
Logic (Optimal HashMap Approach):
1. Store frequency of all elements from nums1 using Counter.
2. Traverse nums2:
   - if element frequency is greater than 0,
     it means common element exists.
3. Add element to result and decrease frequency.
4. Frequency decrement ensures duplicates are handled correctly.

Why This Is Optimal:
- HashMap provides O(1) average lookup time.
- Avoids nested loop searching.

Time Complexity:
O(n + m)

Space Complexity:
O(n)
for frequency hashmap.
"""
