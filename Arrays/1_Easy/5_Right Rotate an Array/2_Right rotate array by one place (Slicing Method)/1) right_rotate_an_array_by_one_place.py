def rotate_array_by_one_place(nums):
    n = len(nums)
    # nums[:] = nums[-1] + nums[0 : n - 1]         # This will give an error "unsupported operand types" as we are trying to concatenate 'int' and 'list'

    print(id(nums))

    nums[:] = [nums[-1]] + nums[0 : n - 1]
    # converting 'int' into 'list' and then concatenating them

    print(id(nums))

    return nums


nums = [5, -2, 3, 9, 0, 6, 10, 7]
print(rotate_array_by_one_place(nums))


"""🔹 Case 1: nums = [nums[-1]] + nums[0:n-1]

This creates a new list object and then reassigns the variable nums to point to it.

The old list is no longer referenced by nums.

If other variables were pointing to the original list, they won’t see this change.

Example:

nums = [1, 2, 3]
alias = nums        # alias points to the same list
nums = [0] + nums   # reassigns nums to a NEW list
print(nums)   # [0, 1, 2, 3]
print(alias)  # [1, 2, 3]  -> unaffected




🔹 Case 2: nums[:] = [nums[-1]] + nums[0:n-1]

nums[:] means "replace all elements of the existing list."

No new list object is created for nums; instead, the same list in memory is updated.

Other variables pointing to the same list will also see the update.

Example:

nums = [1, 2, 3]
alias = nums        # alias points to the same list
nums[:] = [0] + nums
print(nums)   # [0, 1, 2, 3]
print(alias)  # [0, 1, 2, 3]  -> alias is also updated!
"""


"""
Short Explanation :- 

nums = [...] → creates a new list object and reassigns nums to it (different memory address).

nums[:] = [...] → modifies the same list in place (same memory address), so all references to that list see the change.

"""


# Logic:
# To rotate the array by one place to the right, we create a new list using slicing.
# The last element nums[-1] becomes the first element, and the rest of the array
# (nums[0 : n-1]) is appended after it.
#
# nums[:] is used instead of nums = ... to ensure in-place modification:
#   - nums = [...] creates a NEW list object and reassigns the variable nums,
#     which does NOT update other references to the original list.
#   - nums[:] = [...] updates the contents of the SAME list object,
#     so all variables referencing that list will see the changes.
#
# Time Complexity: O(n)   → slicing and concatenation traverse the list once.
# Space Complexity: O(n)  → a new list is created for the rotated version.
