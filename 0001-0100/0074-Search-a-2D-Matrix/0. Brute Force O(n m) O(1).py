# 74. Search a 2D Matrix


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == target:
                    return True

        return False


# * Time: O(n * m) - In the worst case we check the entire array, so the time taken scales with n and m

# * Space: O(1) - The memory usage remains constant regardless of input size
