# Leetcode : 54. Spiral Matrix : Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def spiral_matrix(self, matrix: list[list[int]]) -> list:

        # Edge case: If the matrix is empty or has no columns, return an empty list
        if not matrix or not matrix[0]:
            return []

        # Initialize boundary pointers
        row_begin, col_begin = 0, 0  # Starting row and column
        row_end, col_end = len(matrix) - 1, len(matrix[0]) - 1  # Ending row and column
        result = []  # To store elements in spiral order

        # Continue traversal until the boundaries overlap
        while row_begin <= row_end and col_begin <= col_end:

            # 1. Traverse from Left → Right along the top row
            for i in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][i])
            row_begin += 1  # Move top boundary down

            # 2️. Traverse from Top → Bottom along the right column
            for i in range(row_begin, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1  # Move right boundary left

            # 3️. Traverse from Right → Left along the bottom row. Check is needed to avoid duplicate traversal
            if row_begin <= row_end:
                for i in range(col_end, col_begin - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1  # Move bottom boundary up

            # 4️. Traverse from Bottom → Top along the left column. Check is needed to avoid duplicate traversal
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1  # Move left boundary right

        return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# matrix = []
obj = Solution()
print(obj.spiral_matrix(matrix))

"""
1. We maintain four boundaries:
   - row_begin → top boundary
   - row_end   → bottom boundary
   - col_begin → left boundary
   - col_end   → right boundary

2. We traverse the matrix in 4 steps repeatedly:
   a) Left to Right (top row)
   b) Top to Bottom (right column)
   c) Right to Left (bottom row)
   d) Bottom to Top (left column)

3. After completing each direction, we shrink the corresponding boundary
   to avoid revisiting elements.

4. Boundary checks (row_begin <= row_end and col_begin <= col_end)
   prevent duplicate traversal when the matrix has odd rows or columns.
   
   - Why boundary checks are needed for the last two loops:

        • After completing the first two traversals (top row and right column),
        the row_begin and col_end boundaries are already updated.

        • In cases where the matrix has:
        - a single remaining row (e.g., 1 x n)
        - or a single remaining column (e.g., m x 1)

        the bottom row or left column may have already been traversed.

        • The checks:
            if row_begin <= row_end
            if col_begin <= col_end

        ensure that:
        - We do NOT traverse the same row twice
        - We do NOT traverse the same column twice
        - We avoid duplicate elements in the result

        • Without these checks:
        - The bottom row traversal may repeat the top row
        - The left column traversal may repeat the right column

5. The loop runs until all elements are visited exactly once.

Time Complexity: O(m x n)
- Every element is visited exactly one time.

Space Complexity: O(m x n)
- Used to store the result list.
"""
