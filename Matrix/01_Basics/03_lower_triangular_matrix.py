# This program prints the lower triangular part of a 2D matrix. Elements above the diagonal are replaced with '*'.

matrix = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):  # Iterate over rows
    for j in range(cols):  # Iterate over columns
        if j <= i:  # Lower triangular condition
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()

"""
Logic:
- i represents the row index.
- j represents the column index.

- When j <= i:
  The element lies on or below the main diagonal, so the matrix element is printed.

- When j > i:
  The element lies above the main diagonal, so it is replaced with '*'.

This logic prints the lower triangular part of the matrix.
"""
