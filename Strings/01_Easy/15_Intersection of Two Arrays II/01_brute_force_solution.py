# 350. Intersection of Two Arrays II. Given two integer arrays nums1 and nums2, return an array of their intersection (Brute Force Solution)
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


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # store final intersection elements
        result = []

        # visited array to avoid using same element again
        visited = [False] * len(nums2)

        # traverse nums1
        for i in range(len(nums1)):

            # check every element in nums2
            for j in range(len(nums2)):

                # if elements match and not already used
                if nums1[i] == nums2[j] and not visited[j]:

                    # add common element
                    result.append(nums1[i])

                    # mark element as used
                    visited[j] = True

                    # stop searching further for current element
                    break

        # return intersection array
        return result


# Example Usage
obj = Solution()

print(obj.intersect([1, 2, 2, 1], [2, 2]))  # Output : [2, 2]
print(obj.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output : [4, 9]


"""
Logic (Brute Force Approach):
1. Traverse every element of nums1.
2. For each element, search through nums2.
3. If a matching unused element is found:
   - add it to result
   - mark it as visited
4. Break after first match to maintain correct frequency count.

Why It Is Brute Force:
- Every element in nums1 checks almost every element in nums2.
- Uses nested loops for searching matches.

Time Complexity:
O(n * m)

Space Complexity:
O(m)
for visited array.
"""
