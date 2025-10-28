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
        def solve(i: int, j: int) -> int:
            # * Check for memoized subproblem
            if (i, j) in memo:
                return memo[(i, j)]

            # * Base Case: Out of Bounds
            if i == m or j == n:
                return (1 << 31) - 1

            # * Base Case: Found a path to bottom-right
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            # * At each level of recursion, take the minimum of right and left, and add the current value
            memo[(i, j)] = min(solve(i + 1, j), solve(i, j + 1)) + grid[i][j]
            return memo[(i, j)]

        m: int = len(grid)
        n: int = len(grid[0])
        memo: dict[tuple[int, int], int] = {}
        return solve(0, 0)


# * Time: O(n * m) - The time taken scales wtih the size of the input (no. of rows and columns)
# * There are `n` possible values for `i` and `m` possible values for `j`
# * Thus there are n * m unique subproblems to solve

# * Space: O(n * m) - Since there are n * m unique subproblems, there are as many subproblems to cache
