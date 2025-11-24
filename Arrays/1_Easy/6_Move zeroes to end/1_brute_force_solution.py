def move_zeros_to_end(nums):

    n = len(nums)
    temp = []

    for i in range(0, n):
        if nums[i] != 0:
            temp.append(nums[i])

    m = len(temp)

    for i in range(0, m):
        nums[i] = temp[i]

    for i in range(m, n):
        nums[i] = 0

    return nums


nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
print(move_zeros_to_end(nums))


# Logic:
# The goal is to move all zeros in the list to the end while keeping the order of non-zero elements unchanged.

# Step 1: Traverse the array and collect all non-zero elements in a temp list.
# Step 2: Copy the elements from temp back into the original list from index 0.
# Step 3: Fill the remaining positions with zeros.

# This approach maintains stability (relative order of non-zero elements)
# but uses extra space for the temp list.

# Time Complexity: O(n) — each element is processed a constant number of times.
# Space Complexity: O(n) — due to the temporary list storing non-zero elements.
