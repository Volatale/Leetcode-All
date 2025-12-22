# 118. Pascal's Triangle II

# * Each row begins and ends with a 1
# * So for each new row, we push a 1 to the row, and then compute the elements between
# * For the last element, we append another 1

# * The row simultaneously acts as both the prev AND the curr arrays
# ! Iterate backwards to ensure we don't overwrite values before they are used
# * Think of the elements to the LEFT of `j` as existing on the PREVIOUS plane (array)
# * And elements on the RIGHT of `j` as existing on the CURRENT plane (array)
# * Why? Because the values on the left haven't been used yet, so they must be the "previous" values
# * And the values on the right HAVE been processed during this iteration, so they represent the "current" values
# * This is essentially a dynamic programming solution + space optimization
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row: list[int] = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            # * Only process elements in the range [1:n-1]
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]  # * row[j] = row[j] + row[j-1]

        return row


sol: Solution = Solution()
print(sol.getRow(0))
print(sol.getRow(1))
print(sol.getRow(3))

# * Time: O(k^2) - The time taken scales with the number of rows; We have a nested for loop

# * Space: O(k) - The number of rows scales with the size of the input
