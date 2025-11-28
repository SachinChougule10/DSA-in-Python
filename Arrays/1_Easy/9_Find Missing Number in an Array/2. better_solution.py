def find_missing_number(nums):
    n = len(nums)

    freq_map = {}

    # Step 1: initialize frequency map for all numbers 0 to n

    # alternate way to nitialize frequency map for all numbers 0 to n :-
    # for i in range(0, n + 1):
    #     freq_map[i] = 0

    freq_map = {i: 0 for i in range(0, n + 1)}

    # Step 2: mark each number present in the list

    # alternate way to mark each number present in the freq map
    # for i in range(0, n):
    #     if nums[i] in freq_map:
    #         freq_map[nums[i]] += 1

    for i in nums:
        freq_map[i] = 1

    # Step 3: find which number wasn't marked (value = 0)
    for k, v in freq_map.items():
        if v == 0:
            return k


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(find_missing_number(nums))

# Logic:

# We know the array contains numbers from 0 to n with one missing.
# Step 1: Create a frequency map for all numbers from 0 to n and set each value to 0.
# Step 2: For every number in nums, mark it as present by setting freq_map[num] = 1.
# Step 3: The number that remains 0 in freq_map is the missing number.

# Time Complexity: O(n) because we iterate through nums and freq_map once.
# Space Complexity: O(n) due to the frequency map storing n+1 keys.
