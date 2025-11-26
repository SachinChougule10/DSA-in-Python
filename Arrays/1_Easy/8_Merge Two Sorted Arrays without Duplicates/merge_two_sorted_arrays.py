# Question :- Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
# Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.


def merge_two_sorted_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    i = 0  # pointer for arr1
    j = 0  # pointer for arr2
    result = []  # stores the union elements

    # Merge both arrays like merge sort while avoiding duplicates
    while i < n and j < m:
        if arr1[i] <= arr2[j]:  # If arr1 element is smaller or equal
            if len(result) == 0 or result[-1] != arr1[i]:  # avoid duplicates
                result.append(arr1[i])
            i += 1  # move pointer in arr1
        else:
            if len(result) == 0 or result[-1] != arr2[j]:  # avoid duplicates
                result.append(arr2[j])
            j += 1  # move pointer in arr2

    # Add remaining elements of arr1 (after one array is exhausted)
    while i < n:
        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    # Add remaining elements of arr2
    while j < m:
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

print(merge_two_sorted_arrays(a, b))


# Logic:

# Since both arrays are already sorted, we use two pointers (i for arr1 and j for arr2)
# and compare elements just like in merge step of merge sort.

# At each step:
#   - If arr1[i] <= arr2[j], we consider arr1[i] for the result and move pointer i.
#   - Otherwise, we consider arr2[j] and move pointer j.

# To avoid duplicates, we only append an element if the result list is empty
# or the last inserted element is different from the current element.

# After one array is fully traversed, we append the remaining elements
# from the other array (again checking for duplicates).

# Time Complexity:  O(n + m)     → Each list is scanned once.
# Space Complexity: O(n + m)     → The result list stores the union elements.
