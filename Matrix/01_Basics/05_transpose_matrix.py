# This program transposes a 2D matrix. Rows become columns and columns become rows.

matrix = [[5, 9, 1], [2, 3, 7]]  # Original matrix (2 rows × 3 columns)

rows = len(matrix)  # Number of rows in the original matrix
cols = len(matrix[0])  # Number of columns in the original matrix

# Create an empty result matrix with swapped dimensions (3 rows × 2 columns)
result = [[0] * rows for _ in range(cols)]

# Iterate through each element of the original matrix
for i in range(rows):  # Loop over rows
    for j in range(cols):  # Loop over columns
        result[j][i] = matrix[i][j]  # Assign transposed value

print(result)  # Print the transposed matrix


"""
1. rows = len(matrix)
   - Counts how many rows are present in the original matrix.

2. cols = len(matrix[0])
   - Counts how many columns are present.
   - We use the first row because all rows have the same number of columns.

3. result = [[0] * rows for _ in range(cols)]
   - Creates an empty matrix with transposed dimensions.
   - If original is (rows x cols), result becomes (cols x rows).

4. Nested loops:
   - Outer loop (i) iterates through rows.
   - Inner loop (j) iterates through columns.

5. result[j][i] = matrix[i][j]
   - Swaps row and column indices.
   - This converts rows into columns (transpose operation).
"""
