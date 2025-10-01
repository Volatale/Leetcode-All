# 37. Sudoku Solver

# * We are given a sudoku board, and the goal is to solve it
# * Each value must be unique in each row, column, and subgrid
# ! One important observation is that the board may already contain cells
# *     - We are only concerned with the EMPTY cells, so we track their positions (row, col)
# ! The subgrid can be thought of as being a 3 x 3 matrix
# *     - We know we can get the row via: row // 3
# *     - And we can get the column via: col // 3
# *     - Thus, using the 2D to 1D index conversion formula, we get the subgrid:
# *         - row * COLS + col
# * This problem involves backtracking since we have no guarantee that our choice will be valid
# *     - But we still need to try all of the (relevant) possibilities
# ! We can prune the number of branches we explore via the `empty_cell` list
# *     - We only need to populate len(empty_cell) cells
# *     - Thus, the maximum recursion depth is also equal to len(empty_cells)
# * We "start" at index 0 (where the index represents the empty cell)
# * Get the (row, col) from the empty_cells list
# * Then, we iterate from [1...9] and try populating (row, col) with the current digit
# *     - If the digit doesn't exist in the row, column, or subgrid, then we can proceed with the candidate (digit)
# *     - After exploration is done, (and presumably fails), we undo the board modification
# *         - Then, we can try the next digit (we start with 1, then try 2, then 3, etc all the way up to 9)
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows: list[set[str]] = [set() for _ in range(9)]
        cols: list[set[str]] = [set() for _ in range(9)]
        subgrids: list[set[str]] = [set() for _ in range(9)]

        # * The (row, col) of every cell that we need to populate
        empty_cells: list[tuple[int, int]] = []

        # * Add the values that are already on the board to the sets
        for row in range(9):
            for col in range(9):
                val: str = board[row][col]

                # * Track the empty cells
                if val == ".":
                    empty_cells.append((row, col))
                else:
                    # * Add the value to the respective sets
                    rows[row].add(val)
                    cols[col].add(val)
                    subgrids[(row // 3) * 3 + (col // 3)].add(val)

        def backtrack(index: int):
            # * len(empty_cells) = The max recursion depth we need, and the no. of cells to populate
            if index == len(empty_cells):
                return True

            row, col = empty_cells[index]
            subgrid = (row // 3) * 3 + (col // 3)

            # * Choose candidate
            for digit in map(str, range(1, 10)):
                if (
                    digit not in rows[row]
                    and digit not in cols[col]
                    and digit not in subgrids[subgrid]
                ):
                    # * Place the digit (choose candidate)
                    board[row][col] = digit
                    rows[row].add(digit)
                    cols[col].add(digit)
                    subgrids[subgrid].add(digit)

                    # * Explore candidate
                    if backtrack(index + 1):
                        return True

                    # * Undo the move (reverse modifications)
                    board[row][col] = "."
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    subgrids[subgrid].remove(digit)

            # * This level of recursion failed
            return False

        # * Start from the first empty cell
        backtrack(0)


# * Time: O(9^81) - There are (9 * 9 = 81) cells, and for each cell (assuming it is empty), there are 9 branches
# * We potentially have to try the digits 1-9 for each cell that exists
# * Each digit placement eliminates lots of future possibilities, so deep invalid paths rarely occur
# * However, in reality, the depth of recursion won't scale anywhere near this badly
# * The practical time complexity is closer to O(C), where `c` is small in real puzzles

# * Space: O(1) - There are 27 sets in total, each storing at most 9 digits O(27 * 9) -> O(1)
# * The recursion stack depth is at most 81 -> O(1)
