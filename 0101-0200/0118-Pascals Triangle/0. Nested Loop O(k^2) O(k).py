# 118. Pascal's Triangle

# * Each row begins and ends with a 1
# * So for each new row, we push a 1 to the row, and then compute the elements between
# * For the last element, we append another 1
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]

        results: list[list[int]] = [[1]]

        for row in range(1, numRows):
            new_row: list[int] = [1]  # * Each row starts with a 1

            # * Grab the values above for each index [1:row] (row = no. of elements on this level)
            for col in range(1, row):
                new_row.append(results[row - 1][col - 1] + results[row - 1][col])

            new_row.append(1)  # * And each row ends with a 1

            results.append(new_row)

        return results


sol: Solution = Solution()
print(sol.generate(5))

# * Time: O(numRows) - The time taken scales with the number of rows

# * Space: O(numRows) - The number of rows scales with the size of the input
