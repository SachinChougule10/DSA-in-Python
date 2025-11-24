def move_zeros_to_end(nums):

    n = len(nums)  # Get the total number of elements in the list
    temp = []  # Temporary list to store all non-zero elements

    for i in range(0, n):
        if nums[i] != 0:  # Check if current element is not zero
            temp.append(nums[i])  # Add non-zero element to temp list

    m = len(temp)  # Number of non-zero elements collected

    for i in range(0, m):  # Copy non-zero elements back into original list
        nums[i] = temp[i]

    for i in range(m, n):  # Fill the rest of the list with zeros
        nums[i] = 0

    return nums  # Return the updated list


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
