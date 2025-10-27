# * 63. Unique Paths II

# * Same as Leetcode 62. Unique Paths, except we have to contend with obstacles
# * If obstacleGrid[i][j] = 1, return 0
# *     - We can't move to this cell since there is an obstacle in the way
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        def solve(i: int, j: int) -> int:
            # * Check for memoized subproblem
            if (i, j) in memo:
                return memo[(i, j)]

            # * Base Case: Out of bounds or obstacle encountered
            if i == m or j == n or obstacleGrid[i][j] == 1:
                return 0

            # * Base Case: Successfully made it to bottom-right
            if i == m - 1 and j == n - 1:
                return 1

            memo[(i, j)] = solve(i + 1, j) + solve(i, j + 1)
            return memo[(i, j)]

        m: int = len(obstacleGrid)
        n: int = len(obstacleGrid[0])

        memo: dict[tuple[int, int], int] = {}
        return solve(0, 0)


# * Time: O(n * m) - There are `n` possible values for `i` and `m` possible values for `j`
# * We are using memoization so there are n * m unique subproblems

# * Space: O(n * m) - There are n * m unique subproblems to memoize
