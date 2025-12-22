# 118. Pascal's Triangle II

# * Each row begins and ends with a 1
# * So for each new row, we push a 1 to the row, and then compute the elements between
# * For the last element, we append another 1
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]

        prev: list[int] = [1]  # * Previous row (implicit row-1)

        for row in range(1, rowIndex + 1):
            curr: list[int] = []  # * Current row
            curr.append(1)  # * Each row begins with a 1

            # * Populate the middle values
            for col in range(1, row):
                curr.append(prev[col - 1] + prev[col])

            curr.append(1)  # * And each row ends with a 1
            prev = curr  # * "new" previous (for next row) is the current row

        return prev


sol: Solution = Solution()
print(sol.getRow(0))
print(sol.getRow(1))
print(sol.getRow(3))

# * Time: O(k^2) - The time taken scales with the number of rows; We have a nested for loop

# * Space: O(k) - The number of rows scales with the size of the input
