# * 63. Unique Paths II

# * Same as Leetcode 62. Unique Paths, except we have to contend with obstacles
# * If obstacleGrid[i][j] = 1, return 0
# *     - We can't move to this cell since there is an obstacle in the way
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m: int = len(obstacleGrid)
        n: int = len(obstacleGrid[0])

        # * The start or the end are blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # * dp[i][j] = No. of Ways to reach cell [i][j]
        dp: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1  # * We start at the top-left, so there is always 1 way

        for i in range(0, m):
            for j in range(0, n):
                # * Skip all of the obstacle cells
                if obstacleGrid[i][j] == 1:
                    continue

                # * Sum the no. of ways to move up and left
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]

                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]


# * Time: O(n * m) - There are `n` possible values for `i` and `m` possible values for `j`

# * Space: O(n * m) - There are n * m unique subproblems to cache
