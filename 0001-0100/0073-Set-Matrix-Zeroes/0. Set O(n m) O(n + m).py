# 73. Set Matrix Zeroes

# * We need to split the work into two phases
# * Technically, we could modify the matrix in place as we encounter each "0"
# * However, this would mean that we create extra work for ourselves and is hard to follow
# *     - If we have [[1, 0, 1], [0, 1, 0]], then the top row becomes 0, but then we reach [0][2]
# *     - And at [0][2], we find another 0, so we have to once again modify the top row (which was already done)
# * Instead, we iterate through the array and mark the rows and columns that will need to be zeroed
# * And after, we iterate through the matrix again and only now do we actually modify the matrix
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m: int = len(matrix)
        n: int = len(matrix[0])

        # * Mark the rows and columns that need to be zeroed
        rows: set[int] = set()
        cols: set[int] = set()

        # * Phase 1: Determine what rows and columns need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # * Mark both the row and column as "to be zeroed"
                    rows.add(i)
                    cols.add(j)

        # * Phase 2: Zero out the relavent rows and columns
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0


sol: Solution = Solution()
print(sol.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(sol.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(sol.setZeroes([[0]]))
print(sol.setZeroes([[0, 1, 0], [1, 0, 1]]))

# * Time: O(n * m) - The time taken scales with the size of the input (no. of rows and columns)

# * Space: O(n + m) - There are `n` rows and `m` columns, thus the set's size scales to n + m at worst
