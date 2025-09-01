# 6. Zigzag Conversion

# ! The characters themselves are irrelevant, what we really care about is their INDICES:
# *     - 0     4     8      12
# *     - 1  3  5  7  9  11  13  15
# *     - 2     6     10     14
# ! Notice that the top and bottom rows have gap of FOUR between them
# * And the middle gap has a gap of 2
# ! How do we devise a formula for this?
# * Take numRows = r. If we start at 0, then:
# *     1. Go downward: row 0 -> row 1 -> ... -> row (r - 1)
# *         - This takes (r - 1) steps
# *     2. Then go upward diagonally: row (r - 1) -> row (r - 2) -> ... row 1 -> row 0
# *         - This also takes (r - 1) steps
# ! Thus, one FULL "zigzag" = down + up = (r - 1) + (r - 1) steps
# *     - Each step corresponds to consuming ONE character from the input string
# *     - Therefore cycleLen = 2(r - 1) = 2r - 2
# * Example: r = 4
# *       row 0: 0        6        12
# *       row 1: 1     5  7     11 13
# *       row 2: 2  4     8  10    14
# *       row 3: 3        9        15
# * If we look at row 0, we see the indices are (0, 6, 12, ... 18)
# *     - cycleLen = 6
# *           2r - 2
# *           2 * 4 - 2 = 6
# * So now we know:
# *       numRows = r
# *       Full zigzag cycle = 2r - 2
# *       For each row `i` (0 <= i < r), find all the characters that belong to this row
# * Example 2, numRows = 4:
# *       0        6          12          18
# *       1     5  7      11  13      17  19
# *       2  4     8  10      14  16      20
# *       3        9          15          21
# ! The inner rows (r != 0 and r != numRows - 1) follow this formula:
# *       Row 0: j = 0 + k * cycleLen
# *       Row 3: j = (r - 1) + k * cycleLen
# *         - k = kth character on the current row
# ! As for the middle rows, it is more complicated:
# *       Row 1: 1, 5, 7, 11, 13, 17, 19
# * The pattern is as follows:
# *       Start = 1
# *       Add 4 -> 5
# *       Add 2 -> 7
# *       Add 4 -> 11
# *       Add 2 -> 13
# *       etc.
# * The formuals for the jumps are:
# *       2 = cycleLen - 2 * i
# *         6 - (2 * 2) = 2
# *       4 = 2 * i
# *         2 * 2 = 4
# *       So the diagonal elements alternate between (cycleLen - 2 * i) and (2 * i)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # * No zigzag is present, so just return the string itself
        if numRows == 1:
            return s

        cycleLen = 2 * numRows - 2  # * Steps T/B and B/T = (r - 1) * (r - 1)
        res: list[str] = []
        n: int = len(s)

        # * Row by Row
        for row in range(numRows):
            j = row

            # * Process characters within the ith row
            while j < n:
                res.append(s[j])  # * kth character in the ith row

                # * For middle rows, add the "diagonal" character
                if row != 0 and row != numRows - 1:
                    diag: int = j + cycleLen - 2 * row

                    if diag < n:
                        res.append(s[diag])

                j += cycleLen

        return "".join(res)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(sol.convert("SONICTHEHEDGEHOG", 4))  # SHEOTEGHNCHDOIEG
print(sol.convert("AB", 1))  # AB

# * Time: O(n) - This version doesn't need to build all of the arrays to get started
# * Instead, we use (closed) mathematical formulas to calculate which characters belong to which rows/indices

# * Space: O(n) - Ultimately, we create a string of equal length to the input
