# This program prints the secondary diagonal of a 2D matrix. All other elements are replaced with '*'.

matrix = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]

rows = len(matrix)  # Total number of rows
cols = len(matrix[0])  # Total number of columns

for i in range(rows):  # Iterate over rows
    for j in range(cols):  # Iterate over columns
        if i + j == rows - 1:  # Check for secondary diagonal position
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()  # Move to the next row

"""
Logic:
- i represents the row index.
- j represents the column index.

- For the secondary diagonal, the sum of indices i + j equals (number of rows - 1).

- When this condition is true, the matrix element is printed.
- Otherwise, the element is replaced with '*'.

This logic prints the secondary diagonal of the matrix.
"""
