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

# ! Why does the bit manipulation version work?
# * We are only dealing with 9 digits (1-9)
# * Bit manipulation can be used as a memory optimization for sets
# * We can perform membership tests via bitmasking:
# *     - rows[r] & (1 << int(board[r][c]))
# * And we can add members (digits) to the set (bitmask):
# *     - rows[r] |= 1 << int(board[r][c])
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # * 9 integers (bitmasks) for rows, columns and subgrids
        rows: list[int] = [0] * 9
        cols: list[int] = [0] * 9
        subgrids: list[int] = [0] * 9

        for r in range(9):
            for c in range(9):
                val: str = board[r][c]

                # * We are only concerned with digits
                if val == ".":
                    continue

                num = int(val)  # * We want to perform bit manipulation
                bit = 1 << num  # * The corresponding bit position for this digit

                subgrid_idx: int = (r // 3) * 3 + (c // 3)

                # * Check if this bit is already set
                if rows[r] & bit or cols[c] & bit or subgrids[subgrid_idx] & bit:
                    return False

                # * Set the corresponding bits
                rows[r] |= bit
                cols[c] |= bit
                subgrids[subgrid_idx] |= bit

        return True


# * Time: O(1) - We always perform two nested loops, both of which scale with 9 (regardless of input)

# * Space: O(1) - The memory usage remains constant regardless of input size
