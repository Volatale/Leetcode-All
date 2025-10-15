# 51. N-Queens

# * We have an (n x n) chessboard and we want to place N queens in such a way that none can attack each other
# * The following constraints must be followed for this to be possible:
# *     - No two queens share the same row
# *     - No two queens share the same column
# *     - No two queens share the same diagonal
# * Our goal is to return all of the possible configurations given our board
# *     - Naturally, this can be handled via backtracking
# *     - Backtracking is fundamentally a recursive approach to problem-solving
# ! We know each queen belongs on a different row
# *   - Therefore, whenever we choose our candidate we move to the next row
# *   - That is, row + 1
# * The row constraint is automatically handled via recursion
# * That leaves the column constraint and the diagonal constraint
# ! To handle the column constraint, we can simply iterate from [0..n-1] within each level of recursion
# *     - We can check if a queen exists in this column using a set
# ! Finally, we have the the diagonal constraint
# * Every cell in our chess board can be defined by a point (row, col)
# * Diagonals have a simply algebraic property:
# ! A main diagonal (top-left to bottom-right) has points where:
# *     - row - col = constant
# *         - (0, 0), (1, 1), (2, 2), (3, 3) all have (row - col = 0)
# *         - (1, 0), (2, 1), (3, 2) all have (row - col = 1)
# *         - (0, 1), (1, 2), (2, 3) all have (row - col = -1)
# ! A anti-diagonal (top-right to bottom-left) has points where:
# *     - row + col = constant
# *         - (0, 3), (1, 2), (2, 1), (3, 0) all have (row + col = 3)
# *         - (0, 2), (1, 1), (2, 0) all have (row + col = 2)
# *         - (1, 3), (2, 2), (3, 1) all have (row + col = 4)

# * When we move along a diagonal
# *     - If we go down-right, every time we increase the row by 1, the column increases by 1
# *         - So (row - col) stays constant because we add 1 to both sides of the equation
# *     - If we go down-left, every time we increase the row by 1, the column decreases by 1
# *         - So (row - col) stays constant because you add 1 to one and subtract from the other
# * This is basically the equation of a line in a grid:
# *     - Slope 1 = row - col = k
# *     - Slope -1 = row + col = k
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def backtrack(row: int):
            # * Base Case: successfully placed every queen
            if row == n:
                results.append(["".join(row) for row in board])
                return

            # * Try placing the queen in every column for each row (level of recursion)
            for col in range(n):
                # * Queen can't share a row, column or diagonal ()
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # * Place queen (choose candidate)
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # * Try placing the next queen
                backtrack(row + 1)

                # * Backtrack (remove queen)
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        results: list[list[str]] = []
        cols: set[int] = set()
        diag1: set[int] = set()  # * Tracks (row - col) diagonals
        diag2: set[int] = set()  # * Tracks (row + col) diagonals
        board: list[list[str]] = [["."] * n for _ in range(n)]

        backtrack(0)
        return results


sol: Solution = Solution()
print(sol.solveNQueens(1))
print(sol.solveNQueens(2))
print(sol.solveNQueens(3))
print(sol.solveNQueens(5))

# * Time: O(n^n) - At each level of recursion we perform an O(n) loop, thus the branching factor is n
# * The depth of recursion is also `n` since there are `n` rows

# * Space: O(n) - There are `n` levels of recursion, and the output size scales with the input size in the worst case
