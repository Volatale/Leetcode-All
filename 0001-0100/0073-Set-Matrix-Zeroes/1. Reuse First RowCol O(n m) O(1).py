# 73. Set Matrix Zeroes

# * Technically, we could encode a 1 or 0 into each of the values using bit manipulation
# * However, each value is a value in the range of INT_MIN32 to INT_MAX32, so there are no spare bits to use
# * Instead, we can use the first row and first column to indicate whether the respective cell should be zeroed
# ! Immediately check if the 0th row and 0th column need to be zeroed
# *     - If they do, set the respective boolean to True
# * Then, iterate through the matrix to mark the cells
# *     if matrix[i][j] == 0, then we mark both the row and the column as "to be zeroed"
# *         matrix[i][0] = 0
# *         matrix[0][j] = 0
# * Iterate through the matrix once more, and zero out the cell if either the marked row or column is 0
# * Finally, handle the zeroing of the first row and column if necessary

# * Basically, when modifying the matrix, we iterate from i = 1, j = 1 and onwards
# *     - In other words, we iterate over a rectangle of the shape
# *       [1][1] -> [m-1][n-1]
# *     - Row 0 and col 0 are excluded
# * row 0 and col 0 are used to indicate whether the entire row/col gets 0'd out
# * Additionally, we need to mark whether the 0th row and col get zeroed BEFORE doing anything
# *     - Why? Because otherwise, we may get false positives
# *       The 0th row/column may not have originally had 0s, but it may after the modifications
# *     - Therefore, it would be almost guaranteed that we have to clear the row/col, but it could lead to issues
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m: int = len(matrix)
        n: int = len(matrix[0])

        # * Create flags to track if first row/col should be zeroed
        zero_first_row = any(matrix[0][j] == 0 for j in range(n))
        zero_first_col = any(matrix[i][0] == 0 for i in range(m))

        # * Step 1: Use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # * Mark row as to be zeroed
                    matrix[0][j] = 0  # * Mark column as to be zeroed

        # * Step 2: Zero out based on markers
        for i in range(1, m):
            for j in range(1, n):
                # * Check if column or row should be zeroed
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # * Handle first row zeroing
        if zero_first_row:
            for j in range(n):
                matrix[0][j] = 0

        # * Handle first col zeroing
        if zero_first_col:
            for i in range(m):
                matrix[i][0] = 0


sol: Solution = Solution()
print(sol.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(sol.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(sol.setZeroes([[0]]))
print(sol.setZeroes([[0, 1, 0], [1, 0, 1]]))

# * Time: O(n * m) - The time taken scales with the size of the input (no. of rows and columns)

# * Space: O(1) - The memory usage remains constant regardless of input size
