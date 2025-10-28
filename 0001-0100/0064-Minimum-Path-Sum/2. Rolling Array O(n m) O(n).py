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
# ! Since we are only relying on the previous row (i - 1), we only need to keep two rows in memory at any given point
# *     - Thus we can use a rolling array to cut down on the memory usage
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])

        # * Rolling arrays
        prev: list[int] = [0] * n  # * Represents previous row
        curr: list[int] = [0] * n  # * Represents current row
        prev[0] = grid[0][0]

        # * Handle case where we only move right
        for col in range(1, n):
            prev[col] = prev[col - 1] + grid[0][col]

        for i in range(1, m):
            # * Set the value of the first cell in the row
            curr[0] = prev[0] + grid[i][0]

            for j in range(1, n):
                # * Minimum of previous row and left + the current cell
                curr[j] = min(curr[j - 1], prev[j]) + grid[i][j]

            # * Swap the rows (this is a rolling array)
            prev, curr = prev, curr

        return prev[n - 1]


sol: Solution = Solution()
print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # * 7
print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]))  # * 12


# * Time: O(n * m) - The time taken scales with the size of the input
# * There are n possible values for `i` and m possible values for `j`, hence O(n * m)
# * Additionally, we need to preprocess the top row and leftmost column

# * Space: O(n) - We are using a rolling array, hence the memory usage scales with the no. of columns
