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
        ROWS: int = len(triangle)
        COLS: int = len(triangle[ROWS - 1])

        MAX_INT: int = (1 << 31) - 1

        # * dp[i][j] = Min. Path Sum we can get at index `i` and `j`
        dp: list[list[int]] = [[MAX_INT] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1] = [*triangle[ROWS - 1]]

        # * We start the bottom since we want to return the "top"
        for row in range(ROWS - 2, -1, -1):
            for col in range(row + 1):
                dp[row][col] = (
                    min(dp[row + 1][col], dp[row + 1][col + 1]) + triangle[row][col]
                )

        return dp[0][0]


sol: Solution = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(sol.minimumTotal([[-10]]))

# * Time: O(n * m) - There are `n` rows and `m` columns at most
# * In reality, there are `n` possible values for `i` and `m` possible values for `m`

# * Space: O(n * m) - There are (n * m) unique subproblems to cache
