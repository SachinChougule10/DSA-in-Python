# This program prints only the diagonal elements of a 2D matrix. All other elements are replaced with '*'.

matrix = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):  # Iterate over rows
    for j in range(cols):  # Iterate over columns
        if i == j:  # Check for main diagonal position
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()  # Move to the next row

"""
Logic:
- i represents the row index.
- j represents the column index.

- When i == j:
  The element lies on the main diagonal, so the matrix element is printed.

- When i != j:
  The element is not on the diagonal, so it is replaced with '*'.

This logic prints only the diagonal elements of the matrix.
"""
