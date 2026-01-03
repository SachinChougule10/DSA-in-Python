# This program prints a 2D matrix in proper format by iterating through each row and using the unpacking operator (*).

matrix = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]

# Iterate through each row and print it using unpacking
for row in matrix:
    print(*row)

"""
 'row' represents one row of the matrix (a list).
  The '*' operator unpacks the elements of the row list.

 Example:
   row = [5, 10, 8]
   print(*row)  --> print(5, 10, 8)

 This prints all elements of the row separated by spaces, without using explicit column indexing.
 """
