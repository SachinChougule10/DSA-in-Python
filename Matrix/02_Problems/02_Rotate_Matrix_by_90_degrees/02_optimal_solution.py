# Leetcode : 48. Rotate Image : You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


class Solution:
    def rotate_image(self, matrix: list[list[int]]) -> list:
        rows = len(matrix)
        cols = len(matrix[0])

        # STEP 1: Transpose the matrix in-place
        # Swap elements only above the primary diagonal to avoid double swapping
        for i in range(0, rows - 1):
            for j in range(i + 1, cols):
                # Exchange row and column indices
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # STEP 2: Reverse each row in-place
        # After transpose, reversing each row gives clockwise 90 degree rotation of the original square matrix
        for i in range(rows):
            matrix[i].reverse()

        return matrix


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
obj = Solution()
print(obj.rotate_image(matrix))


"""
LOGIC EXPLANATION (Optimal Brute Force In-Place):

1. Matrix rotation clockwise by 90° can be broken into two operations:
   - Transpose the matrix.
   - Reverse each row.

2. Transpose:
   - Convert rows into columns by swapping matrix[i][j] with matrix[j][i].
   - Only traverse upper triangle (j = i+1 to n) so swaps happen once.
   - Diagonal elements (i == j) remain unchanged.

3. Reverse rows:
   - Each transposed row is reversed in-place.
   - This reorders elements to match 90° clockwise rotation.

TIME COMPLEXITY:
- O(n²) → traverse matrix for transpose + traverse for row reverse.

SPACE COMPLEXITY:
- O(1) → no extra matrix allocated, rotation done directly on input.
"""
