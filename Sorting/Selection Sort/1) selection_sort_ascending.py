class Solution:
    def selection_sort(self, arr):
        for i in range(0, len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


arr = [4, 2, 5, 6, 1, 8, 9, 10, 7, 2, 3]
print(Solution().selection_sort(arr))
