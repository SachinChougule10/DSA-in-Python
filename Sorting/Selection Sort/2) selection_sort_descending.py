class Solution:
    def selection_sort(self, arr):
        for i in range(0, len(arr)):
            max_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[max_index]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]

        return arr


arr = [4, 2, 5, 6, 1, 8, 9, 10, 7, 2, 3]
print(Solution().selection_sort(arr))
