# 120. Triangle

# * At each step, we can either move down or down-right
# * Ultimately, we want the MINIMUM possible path sum
# *     - So in other words, the global minimum
# * Thus, we need to take the local minimum at each step
# *     - This gives us the optimal substructure property
# * Additionally, we can reach the same subproblem from multiple other subproblems
# *     - This indicates the presence of overlapping subproblems
# ! Therefore, with the above knowledge, we know that dynamic programming can likely be applied as an optimization


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        def solve(row: int, col: int) -> int:
            # * Check for memoized subproblems
            if (row, col) in memo:
                return memo[(row, col)]

            # * Base Case: Out of Bounds
            if col >= len(triangle[row]):
                return (1 << 31) - 1

            # * Base Case: Reached the bottom row
            if row == ROWS - 1:
                return triangle[row][col]

            memo[(row, col)] = (
                min(solve(row + 1, col), solve(row + 1, col + 1)) + triangle[row][col]
            )
            return memo[(row, col)]

        memo: dict[tuple[int, int], int] = {}
        ROWS: int = len(triangle)
        return solve(0, 0)


sol: Solution = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(sol.minimumTotal([[-10]]))

# * Time: O(n * m) - There are `n` rows and `m` columns at most
# * In reality, there are `n` possible values for `i` and `m` possible values for `m`

# * Space: O(n * m) - There are (n * m) unique subproblems to cache
