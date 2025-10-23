# 54. Spiral Matrix

# * We can use boundary pointers and use them as stopping points
# * The cycle goes as follows:
# *     - Iterate from left to right along the top
# *         - Increment top by 1 (top row is done)
# *     - Iterate from top to bottom along the right
# *         - Increment right by 1 (right column is done)
# *     - Iterate from right to left along the bottom
# *         - Increment bottom by 1 (bottom row is done)
# *     - Iterate from bottom to top along the left
# *         - Increment left by 1 (left column is done)
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        num: int = 1
        matrix: list[list[int]] = [[0] * n for _ in range(n)]

        # * Boundary pointers
        top, bottom, left, right = 0, n - 1, 0, n - 1

        while left <= right and top <= bottom:
            # * Iterate from left to right along top
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # * Iterate from top to bottom along right
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # * Iterate from right to left along bottom
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # * Iterate from bottom to top along left
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix


# * Time: O(n * m) - The time taken scales with the size of the input (number of rows and columns)

# * Space: O(n * m) - We return an matrix of all of the cells' values
# * As such, the number of values returned scales with input size
