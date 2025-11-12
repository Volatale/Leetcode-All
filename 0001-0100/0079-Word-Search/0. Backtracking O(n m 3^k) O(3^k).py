# 79. Word Search

# * From each cell we can move up, right, down, or left
# *     - Thus, we have 4 choices in the worst case
# * The character we are trying to find can be denoted by word[index]
# *     - Where index represents the index of the ith character of `word`
# * We are looking for len(word) consecutive characters, which means our recursion depth is len(word) deep at most
# ! Instead of tracking visited characters using a set, we can simply mark the character with a `#`
# * Then, when we backtrack, we can replace the `#` with whatever character was there pre-exploration
# * Before any backtracking can be done, we must first find the 0th character (word[0]) in the board
# *     - If it doesn't exist, we return False
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(row: int, col: int, index: int) -> bool:
            # * Base Case: Successfully created the word
            if index == len(word):
                return True

            # * Base Case: Failed to stay in bounds, incorrect char, or already visited cell
            if (
                out_of_bounds(row, col)
                or board[row][col] != word[index]
                or board[row][col] == "#"
            ):
                return False

            # * Choose candidate (also mark as visited)
            char: str = board[row][col]
            board[row][col] = "#"

            # * Explore: Try all 4 directions (up, right, down, left)
            res: bool = (
                backtrack(row - 1, col, index + 1)
                or backtrack(row, col + 1, index + 1)
                or backtrack(row + 1, col, index + 1)
                or backtrack(row, col - 1, index + 1)
            )

            # * Un-choose candidate (backtrack)
            board[row][col] = char
            return res

        def out_of_bounds(row: int, col: int):
            return row < 0 or col < 0 or row >= ROWS or col >= COLS

        ROWS: int = len(board)
        COLS: int = len(board[0])

        # * Try starting from every (relevant) cell
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True

        return False


sol: Solution = Solution()
print(
    sol.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "ABCCED",
    )
)

print(
    sol.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "SEE",
    )
)

print(
    sol.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "ABCB",
    )
)

# * Time: O(n * m * 3^k) - Where `k` is the length of `word`. At each level of recursion, there are 4 branches
# * However, 1 of them immediately returns (direction we just came from), so in reality there are 3 branches
# * And the maximum recursion depth is at most len(word)

# * Space: O(3^k) - The number of stack frames is 3^k in the worst case for the reasons above
