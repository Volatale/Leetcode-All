# 64. Minimum Path Sum

# * At each step we can either move down or move right
# * We want the minimum path sum overall, so take the minimum of both choices at each step
# ! Ensure that we add the value of the current cell at each level too (since we need the sum of all)
# * A greedy choice won't work here because we can't really predict what will be next in that cell
# * Imagine we have the following matrix
# *     [1,3,1]
# *     [1,5,1]
# *     [4,2,1]
# * If we prioritize the smaller valued cells, we'd have to move to 1
# * But the choices after that are between 5 and 4, and both would be the wrong choice
# * Instead, we want to move to 3 because there is a trail 1s that lie after the 3
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])

        # * dp[i][j] = Minimum sum we can get from bottom and right at current cell
        dp: list[list[int]] = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]  # * We have no choice but to include the first value

        # * Handle case where we only move right
        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        # * Handle case where we only move down
        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for i in range(1, m):
            for j in range(1, n):
                # * Minimum of top and left + current cell
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]


sol: Solution = Solution()
print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # * 7
print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]))  # * 12


# * Time: O(n * m) - The time taken scales with the size of the input
# * There are n possible values for `i` and m possible values for `j`, hence O(n * m)
# * Additionally, we need to preprocess the top row and leftmost column

# * Space: O(n * m) - Since there are n * m subproblems, as many need to be cached
