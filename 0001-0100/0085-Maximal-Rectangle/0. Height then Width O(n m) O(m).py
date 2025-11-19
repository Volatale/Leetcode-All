# 85. Maximal Rectangle

# * This problem isn't solvable the same way you can solve Maximal Square
# * A square has 4 equal sides, so we can simply use the following recurrence relation:
# *     dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# * Here, we're working with rectangles, so we don't have the luxury of an equilateral
# ! In a brute force manner, we can compute the heights of each of the "bars" (going down)
# *     heights[i][j] = heights[i-1][j] + 1 if matrix[i][j] == "1"
# *     else heights[i][j] = 0
# * In other words, we can use DP to compute the height of each bar, and then the heights are finished
# ! Then, we can move onto calculating the width of each row one by one
# * Thus, the problem has devolved into "Largest Rectangle in Histogram"
# * We can create a helper function that solves the above, and uses heights[i] as the input (for each row)
# ! Additionally, instead of creating an (n x m) heights matrix, we can apply a DP space optimization
# * We know that in the height matrix:
# *     Each cell's value is dependent on the one above (in the height matrix), and
# *     The current matrix cell
# * If we encounter a "0" in the current column, then we end up with a "0"
# * Otherwise, we keep a rolling total (heights[i][j] += 1)
# * Since we haven't used the future values yet, we can simply keep a singular heights array instead of an entire matrix
# * heights[i][j] = heights[i-1][j] + 1 becomes
# *     heights[j] += 1 (keep rolling total)
# * heights[i][j] = 0 becomes
# *     heights[j] = 0 (reset the rolling total)
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        def largestHistogram(heights: list[int]) -> int:
            stack: list[int] = [-1]  # * Monotonically non-decreasing stack
            heights.append(0)  # * Sentinel value to enforce inner while loop activation
            max_area: int = 0

            # * Find the next smaller element
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    height: int = heights[stack.pop()]
                    width: int = i - stack[-1] - 1

                    max_area = max(max_area, height * width)

                stack.append(i)

            heights.pop()
            return max_area

        if not matrix or not matrix[0]:
            return 0

        n: int = len(matrix)
        m: int = len(matrix[0])

        # * Represents the heights of the current row (space-optimized DP row)
        heights: list[int] = [0] * m
        max_area: int = 0

        # * Compute the largest histogram for each row
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    heights[j] += 1  # * heights[i][j] = heights[i-1][j] + 1
                else:
                    heights[j] = 0  # * Sequence breaks here, can't extend rectangle

            max_area = max(max_area, largestHistogram(heights))

        return max_area


# * Time: O(n * m) - The time taken scales with the number of rows and columns
# * It takes O(m) to calculate the rectangles for each row, and there are `n` rows

# * Space: O(m) - The heights array scales with the number of columns
# * Additionally, the stack size for each row is at most m + 1
