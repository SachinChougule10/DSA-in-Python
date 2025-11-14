def twoSum(nums, target):

    hash_map = {}

    for i, num in enumerate(nums):
        remaining = target - num

        if remaining in hash_map:
            return [hash_map[remaining], i]
        else:
            hash_map[num] = i


nums = [5, 9, 1, 2, 4, 15, 6, 3]
print(twoSum(nums, 13))

# Logic:

# Instead of checking all pairs using nested loops, we use a hash map (dictionary)
# to store each number and its index as we iterate through the list.

# For each number 'num':
#   - We compute the 'remaining' value needed to reach the target.
#   - If the remaining value already exists in the hash_map, it means we have
#     found two numbers whose sum equals the target, so we return their indices.
#   - Otherwise, we store the current number and its index in the hash_map.

# This approach ensures we scan the list only once.

# Time Complexity: O(n)   → Each element is processed once.
# Space Complexity: O(n)  → Hash map stores at most n elements.
