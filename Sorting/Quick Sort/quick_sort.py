def partition(arr, low, high):
    pivot = arr[low]  # chose pivot
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


arr = [4, 9, 7, 8, 2, 3, 1, 5, 6]
n = len(arr)
# print(quick_sort(arr, 0, n - 1))

quick_sort(arr, 0, n - 1)
print(arr)


"""
Logic:
- Pivot chosen as first element
- i scans left → right for element > pivot
- j scans right → left for element ≤ pivot
- Swap until i & j cross
- Place pivot in correct position
- Recursively sort left & right parts
"""
