# 62. Unique Paths

# * From each cell, we can move down or right
# * Thus, there are two choices at each level of recursion
# * If i == m or j == n, then we went out of bounds
# *     - We didn't successfully reach (m - 1, n - 1), so we return 0
# * If i == m - 1 and j == n - 1, then we reached the bottom-right cell
# *     - Thus we return 1 because we found a valid path (1)
# ! It is worth noting that it is possible to reach the same cell from multiple paths
# * In other words, we have overlapping subproblems
# ! Dynamic programming can be applied to reduce the solution space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i: int, j: int) -> int:
            # * Check for memoized subproblem
            if (i, j) in memo:
                return memo[(i, j)]

            # * Base Case: Out of bounds
            if i == m or j == n:
                return 0

            # * Base Case: Successfully made it to m - 1 and n - 1
            if i == m - 1 and j == n - 1:
                return 1

            memo[(i, j)] = solve(i + 1, j) + solve(i, j + 1)
            return memo[(i, j)]

        memo: dict[tuple[int, int], int] = {}
        return solve(0, 0)


sol: Solution = Solution()
print(sol.uniquePaths(3, 7))  # * 28
print(sol.uniquePaths(2, 2))  # * 2
print(sol.uniquePaths(1, 1))  # * 1
print(sol.uniquePaths(3, 4))  # * 10
print(sol.uniquePaths(8, 5))  # * 330

# * Time: O(m * n) - The time taken scales with the number of unique subproblems
# * In our case since we are using memoization: (m + 1) * (n + 1) = (m * n + 2)

# * Space: O(m * n) - There are m * n unique subproblems in the worst case, so all of them must be memoized
