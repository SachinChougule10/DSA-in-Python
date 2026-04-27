# Leetcode : 904. Fruit Into Baskets : You are visiting a farm that has a single row of fruit trees arranged from left to right (Optimal Solution)
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
        # left pointer of sliding window
        left = 0

        #  stores frequency of fruits in current window
        hash_map = {}

        # current window size
        curr_length = 0

        # maximum valid window size
        max_length = 0

        # expand window using right pointer
        for right in range(n):
            # add current fruit to hashmap (increase frequency)
            hash_map[fruits[right]] = hash_map.get(fruits[right], 0) + 1

            # if more than 2 distinct fruits, shrink window
            while len(hash_map) > 2:
                # reduce frequency
                hash_map[fruits[left]] -= 1

                # remove fruit if its count becomes 0
                if hash_map[fruits[left]] == 0:
                    del hash_map[fruits[left]]

                # move left pointer
                left += 1

            # valid window → update lengths
            curr_length = right - left + 1
            max_length = max(max_length, curr_length)

        return max_length


obj = Solution()

fruits1 = [1, 2, 3, 2, 2]
print(obj.total_fruit(fruits1))  # Output : 4

fruits2 = [1, 2, 1]
print(obj.total_fruit(fruits2))  # Output : 3


"""
LOGIC (Optimal - Sliding Window + HashMap):

- Problem reduces to:
  "Find the longest subarray with at most 2 distinct integers"

- Approach:
  1. Use two pointers (left, right) to maintain a sliding window
  2. Expand window using 'right'
  3. Store fruit frequencies in a hashmap
  4. If distinct fruits > 2:
       → shrink window from left
       → decrease frequency
       → remove fruit if frequency becomes 0
  5. At every valid window (≤ 2 types):
       → calculate length
       → update max_length

--------------------------------------------------

DRY RUN (fruits = [1,2,3,2,2]):

right = 0 → {1} → len=1 → max=1  
right = 1 → {1,2} → len=2 → max=2  
right = 2 → {1,2,3} ❌ → shrink  
           → remove 1 → {2,3} → len=2  
right = 3 → {2,3} → len=3 → max=3  
right = 4 → {2,3} → len=4 → max=4  

Final Answer = 4

--------------------------------------------------

TIME COMPLEXITY:
O(n) → each element visited at most twice

SPACE COMPLEXITY:
O(1) → hashmap stores at most 3 keys

--------------------------------------------------

PATTERN RECOGNITION:

Whenever you see:
- "at most 2 types"
- "at most K distinct"
- "two baskets"
- "two characters allowed"

Think: Sliding Window + HashMap
"""
