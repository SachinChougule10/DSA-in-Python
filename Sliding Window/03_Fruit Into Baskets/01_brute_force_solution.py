# Leetcode : 904. Fruit Into Baskets : You are visiting a farm that has a single row of fruit trees arranged from left to right (Brute Force Solution)
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].

# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].


# Constraints:
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length


class Solution:
    def total_fruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        curr_length = 0  # stores current valid subarray length
        max_length = 0  # stores maximum length found

        # iterate over each possible starting index
        for i in range(n):
            # to store distinct fruit types
            fruits_set = set()

            # expand subarray from i to right
            for j in range(i, n):
                # add current fruit type
                fruits_set.add(fruits[j])

                # valid condition (at most 2 types)
                if len(fruits_set) <= 2:
                    # calculate length of subarray
                    curr_length = j - i + 1
                    # update max
                    max_length = max(max_length, curr_length)
                else:
                    # more than 2 types → stop expanding
                    break

        return max_length


obj = Solution()

fruits1 = [1, 2, 3, 2, 2]
print(obj.total_fruit(fruits1))  # Output : 4

fruits2 = [1, 2, 1]
print(obj.total_fruit(fruits2))  # Output : 3

# this question is equivalent to :- Longest subarray with Atmost two distinct integers

"""
LOGIC (Brute Force Approach):

- Problem reduces to:
  Finding the longest subarray with at most 2 distinct integers.

- Steps:
  1. Start from every index 'i' (outer loop).
  2. From each 'i', expand the subarray using 'j' (inner loop).
  3. Maintain a set to track distinct fruit types.
  4. If number of distinct fruits ≤ 2:
       → valid subarray
       → update max_length
  5. If number of distinct fruits > 2:
       → invalid
       → break and move to next 'i'

- Key Insight:
  We check all subarrays and keep only those that satisfy
  the constraint of having at most 2 unique fruit types.

--------------------------------------------------

DRY RUN (fruits = [1,2,3,2,2]):

i = 0 → [1], [1,2], [1,2,3] ❌ → stop → max = 2  
i = 1 → [2], [2,3], [2,3,2], [2,3,2,2] → max = 4  
i = 2 → [3], [3,2], [3,2,2] → max = 4  
i = 3 → [2], [2,2] → max = 4  
i = 4 → [2] → max = 4  

Final Answer = 4

--------------------------------------------------

TIME COMPLEXITY:
O(n^2) → nested loops

SPACE COMPLEXITY:
O(1) → set holds at most 3 elements

--------------------------------------------------

NOTE:
This is a brute force solution.
Optimal solution uses Sliding Window (Two Pointers) → O(n)
"""
