# 130. Surrounded Regions

# * We should immediately explore the matrix and find all of the border-aligned "O"
# * If we do find a border-aligned "O", we can perform a DFS and mark all of the connected "O" as "E"
# *     - Anything marked "E" essentially means that the cell is connected to a border-aligned "O" somewhere
# *     - The "E" implicitly counts as being marked as "visited" (it becomes a cell we can't revisit)
# * Once all of the invalid cells are marked, we can iterate over the matrix once more
# * If we find an "O", then we mark it as "X" (to capture it)
# * If we find an "E", then we mark it as being "O"
# !     - Remember, the "E" were only temporary so we didn't end up with false positives
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        def dfs(row: int, col: int):
            # * Base Case: Out of Bounds, or redundant cell
            if not in_bounds(row, col) or board[row][col] != "O":
                return

            # * Mark as connected to border "0"
            board[row][col] = "E"

            # * Explore neighbors (up, right, down, left)
            for r, c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dfs(row + r, col + c)

        def in_bounds(row: int, col: int) -> bool:
            return row >= 0 and col >= 0 and row < ROWS and col < COLS

        def is_border(row: int, col: int) -> bool:
            return row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1

        ROWS: int = len(board)
        COLS: int = len(board[0])

        # * Find all of the border "0" and turn them into "E" (edge)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and is_border(row, col):
                    dfs(row, col)

        # * Modify the board (capture regions and revert border)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "E":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"


# * Time: O(n * m) - In the worst case, the entire board is connected to a border "O"
# * Thus, we have to call DFS on every cell, and there are n * m cells

# * Space: O(n * m) - If every cell is connected to a border "O", then the max recursion depth is O(n * m)
