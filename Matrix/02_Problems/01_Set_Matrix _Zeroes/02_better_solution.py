class Solution:
    def set_matrix_zeroes(self, matrix: list[list[int]]) -> list:
        rows = len(matrix)  # Total number of rows in the matrix
        cols = len(matrix[0])  # Total number of columns in the matrix

        # Marker array to track which rows should be set to zero
        # If row_matrix[i] == -1, then row i contains at least one zero
        row_matrix = [0 for _ in range(rows)]

        # Marker array to track which columns should be set to zero
        # If col_matrix[j] == -1, then column j contains at least one zero
        col_matrix = [0 for _ in range(cols)]

        # Identify all rows and columns that contain a zero
        for i in range(rows):  # Iterate through each row
            for j in range(cols):  # Iterate through each column
                if matrix[i][j] == 0:  # Check for zero
                    row_matrix[i] = -1  # Mark row i for zeroing
                    col_matrix[j] = -1  # Mark column j for zeroing

        # Update the matrix based on the marked rows and columns
        for i in range(rows):
            for j in range(cols):
                # If the current row or column was marked, set the element to zero
                if row_matrix[i] == -1 or col_matrix[j] == -1:
                    matrix[i][j] = 0

        return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
obj = Solution()
print(obj.set_matrix_zeroes(matrix))

"""
LOGIC EXPLANATION:

1. Two separate marker arrays are used:
   - row_matrix to track rows that contain at least one zero.
   - col_matrix to track columns that contain at least one zero.

2. In the first traversal of the matrix:
   - If a zero is found at position (i, j), row_matrix[i] and col_matrix[j] are marked.
   - This indicates that all elements in that row and column must be set to zero later.

3. In the second traversal:
   - Each element is checked against the marker arrays.
   - If its row or column is marked, the element is set to zero.

4. This two-pass approach prevents overwriting values while scanning the matrix.

TIME COMPLEXITY:
- O(m x n)
The algorithm performs a first nested loop that traverses all cells of the matrix to fill row_matrix and col_matrix, which takes O(m x n) time.
It then runs a second nested loop over all rows and columns to update elements based on those markers, also taking O(m x n). 
The additional operations use only linear scans of size O(m) and O(n), which are smaller compared to the dominant O(mn) terms. Hence the total cost becomes O(mn) + O(mn) = O(2mn), 
and ignoring the constant factor 2 gives overall O(mn) time complexity.

SPACE COMPLEXITY:
- O(m + n) due to the marker arrays
Let the matrix have m rows and n columns. Two extra marker arrays are used: row_matrix of size m and col_matrix of size n, which together require O(m + n) additional space. 
Apart from these arrays, no extra space is used that depends on the input size. Hence, the overall space complexity of the algorithm is O(m + n).
"""
