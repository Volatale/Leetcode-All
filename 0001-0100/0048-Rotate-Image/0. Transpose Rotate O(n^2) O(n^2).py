# 48. Rotate Image

# * To rotate an image 90 degrees, we can simply perform a matrix transpose
# * For each point (i, j), the value is moved to (j, n - 1 - i)
# * This is hard to do in-place because we would be moving things around all at once
# * Instead of moving (i, j) -> (j, n - 1 - i) in one step, we can break it down into two steps
# * The transpose achieves the (j, i) swap
# * Then, reversing each row achieves the (n - 1 - j) swap
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n: int = len(matrix)

        # * Transpose the matrix
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # * Reverse each row
        for row in range(n):
            matrix[row].reverse()


sol: Solution = Solution()
print(sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sol.rotate([[2, 1], [4, 3]]))
print(sol.rotate([[1]]))

# * Time: O(n^2) - The time taken scales with the number of rows and columns

# * Space: O(1) - The memory usage remains constant regardless of input size
