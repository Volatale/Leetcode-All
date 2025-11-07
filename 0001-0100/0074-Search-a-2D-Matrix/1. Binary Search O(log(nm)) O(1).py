# 74. Search a 2D Matrix

# * We are searching for an element within a matrix
# * The matrix itself is sorted in monotonically non-decreasing order
# * There are n * m unique indices, all monotonically increasing
# ! Thus, we have a sorted search space (the range of indices)
# * If we take the range of indices and arranged them into a flat 1D array, they are monotonically increasing
# *     - [0, m * n - 1]
# * Thus, `mid` represents the middle (1D) index given out left and right indices (of the flat 1D array)
# * Then, we can convert that 1D index into a 2D index (because we need to index into the matrix)
# * Lets imagine `mid` = 7, and there are 3 columns per row (so COLS = 3)
# *     - To get the ROW, we do:
# *         7 / 3 = 2.33333, because (2.3333 * 3) + 1 = 7 (roughly)
# *             But we can't index using decimals, so we floor
# *         That gives us 7 // 3 (or mid // COLS) = 2
# *     - To get the COLUMN within that row, we do:
# *         7 % 3 = 1
# *         There are 3 columns per row, so if cycle around the row 7 times, we get index 1
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        # * Our search space is the range of indices in the range [0, m * n - 1]
        left = 0
        right = ROWS * COLS - 1

        while left <= right:
            # * `mid` is the (1D) index we are targeting
            mid: int = left + ((right - left) >> 1)

            # * Convert the 1D index into a 2D index
            new_mid: int = matrix[mid // COLS][mid % COLS]

            if new_mid == target:
                return True  # * Found target
            elif new_mid < target:
                left = mid + 1  # * We need a larger index
            else:
                right = mid - 1  # * We need a smaller index

        # * We failed to find the target
        return False


# * Time: O(log(n * m)) - We are halving the search space of the entire array every iteration

# * Space: O(1) - The memory usage remains constant regardless of input size
