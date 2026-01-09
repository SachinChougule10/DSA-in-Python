# Leetcode 48. Rotate Image : You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).


class Solution:
    def rotate_image(self, matrix: list[list[int]]) -> list:
        rows = len(matrix)  # Number of rows in the original matrix
        cols = len(matrix[0])  # Number of columns in the original matrix

        # Create an empty result matrix with same dimensions. This will hold the rotated image
        # result = [[0] * rows for _ in range(rows)]
        result = [[0 for _ in range(rows)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # Rotation formula for BRUTE FORCE: Element at position matrix[i][j] moves to result[j][(rows - 1) - i]
                result[j][(rows - 1) - i] = matrix[i][j]

        return result


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
obj = Solution()
print(obj.rotate_image(matrix))


"""
LOGIC EXPLANATION (Brute Force):

1. A new matrix 'result' of size n x n is created.
   The original matrix is not modified during traversal.

2. Every element of the original matrix is visited using nested loops with indices (i, j).

3. For a 90 degree clockwise rotation:
      original (i, j)  --->  rotated (j, n - 1 - i)

4. The formula keeps:
   - column index of result fixed to new position
   - row index derived from original column

5. This mapping shifts:
   - first row → last column
   - last row → first column
   achieving clockwise image rotation.

TIME COMPLEXITY:
- O(n x n) = O(n²)

SPACE COMPLEXITY:
- O(n x n) extra space for new matrix = O(n²)

where,
n = number of rows = number of columns because rotation problem uses a square matrix (rows == cols).

"""
