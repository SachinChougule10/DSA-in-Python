# Leetcode : 73. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.


class Solution:
    def set_matrix_zeroes(self, matrix: list[list[int]]) -> list:
        rows = len(matrix)  # Total number of rows
        cols = len(matrix[0])  # Total number of columns

        # First traversal: Whenever a 0 is found, mark its entire row and column
        for i in range(rows):  # Iterate through rows
            for j in range(cols):  # Iterate through columns
                if matrix[i][j] == 0:  # Check for zero
                    self.mark_infinity(matrix, i, j)  # Mark row and column

        # Second traversal: Replace all temporary markers (infinity) with 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float("inf"):  # Convert temp markers (infinity) to 0
                    matrix[i][j] = 0

        return matrix

    def mark_infinity(self, matrix, row, column):
        rows = len(matrix)
        cols = len(matrix[0])

        # Mark all non-zero elements in the given column (keep column index fixed)
        for i in range(rows):
            if matrix[i][column] != 0:
                matrix[i][column] = float("inf")

        # Mark all non-zero elements in the given row (keep row index fixed)
        for j in range(cols):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
obj = Solution()
print(obj.set_matrix_zeroes(matrix))


"""
LOGIC EXPLANATION (Brute Force):

1. Traverse the matrix to find elements with value 0.

2. When a 0 is found at position (i, j):
   - Mark all non-zero elements in row i as infinity.
   - Mark all non-zero elements in column j as infinity.
   - Infinity is used as a temporary marker to avoid immediate overwriting.

3. After marking all affected rows and columns, traverse the matrix again and convert all infinity values to 0.

4. This ensures:
   - Original zeros remain unchanged.
   - Only required rows and columns are set to zero.

TIME COMPLEXITY:
- O((m x n) x (m + n)) → Brute force

SPACE COMPLEXITY:
- O(1) extra space (modifies matrix in-place)

"""
