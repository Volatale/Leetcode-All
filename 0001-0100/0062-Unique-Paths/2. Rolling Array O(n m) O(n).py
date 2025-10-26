# 62. Unique Paths

# ! Recurrence Relation: F(m, n) = F(m - 1) + F(m, n - 1)
# *     - We only need to keep two rows in memory at any given point
# *     - Thus we can utilize a rolling array
# * Apply tabulation to avoid recursion overhead
# *     - We have two non-constant parameters, hence 2D state


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0

        # * dp[i][j] = No. of unique ways to reach cell [i][j]
        # * We are using a rolling array since we only need to keep two rows in memory
        # * Fill with 1s because we know there is only 1 way to reach the cells on top, or on left
        dp: list[list[int]] = [[1 for _ in range(n)] for _ in range(2)]
        dp[0][0] = 1  # * There is always 1 way to reach the start (we start there)

        for i in range(1, m):
            for j in range(1, n):
                dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j - 1]

        # * No. of ways to get to bottom-right
        return dp[(m - 1) & 1][n - 1]


sol: Solution = Solution()
print(sol.uniquePaths(3, 7))  # * 28
print(sol.uniquePaths(2, 2))  # * 2
print(sol.uniquePaths(1, 1))  # * 1
print(sol.uniquePaths(3, 4))  # * 10
print(sol.uniquePaths(8, 5))  # * 330

# * Time: O(m * n) - The time taken scales with the number of unique subproblems
# * In our case since we are using tabulation: (m + 1) * (n + 1) = (m * n + 2)

# * Space: O(n) - We only need to keep 2 rows in memory, so "m" is now a constant factor of 2
