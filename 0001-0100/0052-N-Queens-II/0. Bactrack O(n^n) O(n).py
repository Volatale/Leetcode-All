# 52. N-Queens II


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int):
            # * Successfully placed `n` queens
            if row == n:
                nonlocal count
                count += 1
                return

            for col in range(n):
                # * A queen cannot share a row, column or diagonal
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # * Place the queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # * Move to the next row
                backtrack(row + 1)

                # * Backtrack
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        cols: set[int] = set()
        diag1: set[int] = set()  # * Tracks (row - col) diagonals
        diag2: set[int] = set()  # * Tracks (row + col) diagonals
        count: int = 0
        board: list[list[str]] = [["."] * n for _ in range(n)]

        backtrack(0)

        return count


sol: Solution = Solution()
print(sol.totalNQueens(1))  # * 1
print(sol.totalNQueens(2))  # * 0
print(sol.totalNQueens(3))  # * 0
print(sol.totalNQueens(4))  # * 2
print(sol.totalNQueens(5))  # * 10
print(sol.totalNQueens(6))  # * 4
print(sol.totalNQueens(7))  # * 40
print(sol.totalNQueens(8))  # * 92

# * Time: O(n^n) - At each level of recursion we perform an O(n) loop, thus the branching factor is n
# * The depth of recursion is also `n` since there are `n` rows

# * Space: O(n) - There are `n` levels of recursion
