def merge_sort(arr, low, high):
    if low >= high:
        return arr
    mid = (low + high) // 2

    merge_sort(arr, low, mid)  # sort the left half
    merge_sort(arr, mid + 1, high)  # sort the right half

    merge_arrays(arr, low, mid, high)  # merge both halves
    return arr


def merge_arrays(arr, low, mid, high):
    temp = []  # empty data structure to add elements temperoraily
    left = low  # pointer of left half (starting from low)
    right = mid + 1  # pointer of right half (starting from mid+1)

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


arr = [3, 1, 6, 2, 4, 8, 7]
print(merge_sort(arr, 0, len(arr) - 1))
