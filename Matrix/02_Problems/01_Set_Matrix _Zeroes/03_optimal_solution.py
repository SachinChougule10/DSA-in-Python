class Solution:
    def set_matrix_zeroes(self, matrix: list[list[int]]) -> list:
        rows = len(matrix)
        cols = len(matrix[0])

        # These flags are used to handle the EDGE CASE where the first row or first column contains a zero.
        first_row = False
        first_column = False

        # STEP 1: MARK ROWS AND COLUMNS
        # We use:
        # - matrix[i][0] as a marker for row i
        # - matrix[0][j] as a marker for column j

        # If matrix[i][j] == 0:
        #   - Mark row i by setting matrix[i][0] = 0
        #   - Mark column j by setting matrix[0][j] = 0

        # If the zero is in the first row or first column, we store that information in first_row / first_column
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:  # If zero is found in first row
                        first_row = True
                    if j == 0:  # If zero is found in first column
                        first_column = True
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # STEP 2: ZERO OUT INNER MATRIX (EXCLUDING MARKERS)
        # We start from index 1 to avoid modifying the marker row (row 0) and marker column (column 0)
        for i in range(1, rows):
            for j in range(1, cols):
                # If either the row marker or column marker is zero, then this cell should be set to zero
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # STEP 3: HANDLE FIRST ROW
        # If the first row originally contained a zero, set the entire first row to zero
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0

        # STEP 4: HANDLE FIRST COLUMN
        # If the first column originally contained a zero, set the entire first column to zero
        if first_column:
            for i in range(rows):
                matrix[i][0] = 0

        return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

obj = Solution()
print(obj.set_matrix_zeroes(matrix))


"""
LOGIC:
    
1. The first row and first column are reused as MARKERS.
   - matrix[i][0] indicates whether row i should be zeroed.
   - matrix[0][j] indicates whether column j should be zeroed.

2. The cell matrix[0][0] cannot store two pieces of information (for both first row and first column).
   Therefore, two boolean variables are used:
   - first_row
   - first_column

3. Algorithm Steps:
   - First pass: detect zeros and place markers.
   - Second pass: update inner matrix using markers.
   - Third pass: zero the first row if needed.
   - Fourth pass: zero the first column if needed.

4. This approach avoids using extra arrays and works in O(1) space.

Time Complexity:  O(m x n)
The first nested loop that scans all elements takes O(mn), and the second nested loop that updates the inner matrix also takes O(mn). 
The final single loops for the first row and first column take O(n) and O(m), which are smaller compared to the dominant O(mn) terms, so they are ignored. 
Combining the main costs gives O(mn) + O(mn) = O(2mn), and we ignore the constant factor 2, resulting in overall O(mn) time complexity.

Space Complexity: O(1)
"""
