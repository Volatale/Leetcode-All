# 54. Spiral Matrix

# * All in all, there are (m * n) cells, and we need to record the values of them all in order
# * The order of travel is as follows:
# *     - Right, Down, Left, Up, Right, Down, Left, Up, Right, Down ...
# *     - This process is followed until completion
# * Since we have a matrix, and a matrix can be represented as a graph, we can think of it as such
# * Graph problems are easier to solve if we apply graph algorithms to them (like DFS and BFS)
# *     - In our case, BFS will work since we don't really need to use recursion
# * The cell we want to move to needs to be:
# *     - In bounds
# *     - Not already visited
# * To handle the visited-ness, we can simply use a set of tuples (row, col)
# * If we would move to a cell that is out of bounds or has been visited, we simply switch directions
# *     - 0 -> Right
# *     - 1 -> Down
# *     - 2 -> Left
# *     - 3 -> Up
# * There are only four directions we care about, thus we can MOD by 4 to repeatedly loop
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        def is_in_bounds(row: int, col: int):
            return row >= 0 and col >= 0 and row < ROWS and col < COLS

        # * Handle empty array case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])
        total_cells: int = ROWS * COLS  # * So we know when to stop iterating

        values: list[int] = []

        direction: int = 0  # * 0 -> Right, 1 -> Down, etc
        directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # * Current position
        row: int = 0
        col: int = 0

        visited: set[tuple[int, int]] = set()
        visited.add((0, 0))
        values.append(matrix[0][0])

        while len(values) < total_cells:
            r, c = directions[direction]
            newRow = row + r  # * The row we are moving to
            newCol = col + c  # * THe column we are moving to

            # * Move to an in-bounds, non-visited cell
            if is_in_bounds(newRow, newCol) and (newRow, newCol) not in visited:
                row = newRow
                col = newCol
                values.append(matrix[row][col])
                visited.add((row, col))
            else:
                # * Change directions: out of bounds or cell already visited
                direction = (direction + 1) % 4

        return values


# * Time: O(n * m) - The time taken scales with the size of the input (number of rows and columns)

# * Space: O(n * m) - We return an array of all of the cells' values
# * As such, the number of values returned scales with input size
