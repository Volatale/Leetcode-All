# 36. Valid Sudoku


# * The goal is simply to validate the board
# *     - We don't have to solve the sudoku game itself
# * Each digit can only appear once per row, column, and subgrid
# * So the easiest solution is to simply track which cells have been taken using sets
# *     - Sets enforce the uniqueness, and allow for fast membership tests
# * To handle the subgrid checks, we can use one of the following intuition:
# *     - There are 9 subgrids (thus, we have an internal 3x3 matrix)
# *         - r = row // 3
# *         - c = col // 3
# *     - Then, we can use {value}-{r}-{c} to check for uniqueness
# *         - This is saying "value was found at subgrid[r][c]"
# *           Which is different to saying "value was found at board[row][col]" ({value}-r-{row})
# * Alternatively, since we now we have an internal 3x3 matrix, we can use the 2D to 1D index conversion formula
# *     - There are 3 rows and 3 columns
# *         - r = row // 3
# *         - c = col // 3
# *     - Then, subgrid = r * COLS + c
# *         - So for example, if we got (2, 2)
# *         - Then the conversion gives us: 2 * 3 + 2 = 8
# *             - So we know that "subgrid" is equal to subgrid 8 in particular


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # * Used to track the uniqueness of the cells
        seen: set[str] = set()

        for row in range(9):
            for col in range(9):
                # * Get the current value
                value: str = board[row][col]

                # * Only operate on numbers, ignore unfilled spaces
                if value == ".":
                    continue

                row_key: str = f"{value}-r-{row}"
                col_key: str = f"{value}-c-{col}"

                # * 8 // 3 = 2, 7 // 3 = 2 ([2][2] would target the last subgrid)
                # * subgrid_idx: int = (r // 3) * 3 + (c // 3)
                r = row // 3
                c = col // 3
                subgrid_key = f"{value}-s-{r}{c}"

                # * A duplicate value exists in a row, column or subgrid
                if row_key in seen or col_key in seen or subgrid_key in seen:
                    return False

                # * Mark this cell as seen
                seen.add(row_key)
                seen.add(col_key)
                seen.add(subgrid_key)

        # * The board is valid
        return True


# * Time: O(1) - We always perform two nested loops, both of which scale with 9 (regardless of input)

# * Space: O(1) - The memory usage remains constant regardless of input size
