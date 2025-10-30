def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_part = merge_sort(left_arr)
    right_part = merge_sort(right_arr)

    return merge_array(left_part, right_part)


def merge_array(left_part, right_part):
    result = []
    i, j = 0, 0
    n, m = len(left_part), len(right_part)

    while i < n and j < m:
        if left_part[i] <= right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left_part[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right_part[j])
            j += 1

    return result


arr = [3, 1, 6, 2, 4, 8, 7]
print(merge_sort(arr))
