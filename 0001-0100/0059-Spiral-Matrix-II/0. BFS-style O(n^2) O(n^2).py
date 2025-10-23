# 59. Spiral Matrix II

# * Uses the same solution from 54. Spiral Matrix
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        def is_valid(row: int, col: int) -> bool:
            return (
                row >= 0
                and col >= 0
                and row < n
                and col < n
                and (row, col) not in visited
            )

        if n == 1:
            return [[1]]

        i: int = 1
        total_cells: int = n * n
        matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]

        direction: int = 0  # * R -> 0, D -> 1, L -> 2, U -> 3
        directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # * This is where we currently are
        row: int = 0
        col: int = 0

        visited: set[tuple[int, int]] = set()
        visited.add((0, 0))  # * Add the first cell to the visited matrix
        matrix[0][0] = i  # * Fill the first cell
        i += 1

        # * Keep moving while we haven't filled every cell
        while i <= total_cells:
            # * The position of the new cell we are moving to
            new_row: int = row + directions[direction][0]
            new_col: int = col + directions[direction][1]

            if is_valid(new_row, new_col):
                row = new_row
                col = new_col
                matrix[row][col] = i  # * Fill the cell
                visited.add((row, col))  # * Mark as visited
                i += 1
            else:
                # * Change directions: out of bounds or already visited
                direction = (direction + 1) % 4

        return matrix


sol = Solution()
print(sol.generateMatrix(1))
print(sol.generateMatrix(2))
print(sol.generateMatrix(3))
print(sol.generateMatrix(4))

# * Time: O(n^2) - The time taken scales with the input size

# * Space: O(n^2) - By the end of the algorithm's run, the visited set size will be n^2
