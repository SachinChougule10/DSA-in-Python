# This program prints the upper triangular part of a matrix. Elements below the main diagonal are replaced with '*'.

matrix = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]

rows = len(matrix)  # Number of rows (each inner list represents one row)
cols = len(matrix[0])  # Number of columns (length of any row; same for all rows)

for i in range(rows):  # Iterate over rows
    for j in range(cols):  # Iterate over columns
        if j >= i:  # Upper triangular condition
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()  # Move to next row


""" 
 i represents the row index
 j represents the column index

 When j >= i:
   - The element lies on or above the main diagonal
   - So we print the actual matrix element

 When j < i:
   - The element lies below the main diagonal
   - So we replace it with '*'

 This condition helps in printing the upper triangular matrix.
 """
