# This program iterates through a 2D matrix and prints it in proper matrix format using nested loops.

matrix = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]

rows = len(matrix)  # Number of rows (each inner list represents one row)
cols = len(matrix[0])  # Number of columns (length of any row; same for all rows)


# Iterate through the matrix and print it in matrix format
for i in range(rows):  # Iterate over rows (keeps the row constant)
    for j in range(cols):  # Iterate over columns
        print(matrix[i][j], end=" ")
    print()  # Move to next row


"""
This program prints a 2D list (matrix) in proper matrix format.
Rows are calculated using len(matrix) because each inner list represents one row.
Columns are calculated using len(matrix[0]) because all rows in a matrix have the same number of columns.
"""
