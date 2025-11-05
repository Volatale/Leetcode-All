# 72. Edit Distance

# * There are a few different cases to consider
# * If word1[i] == word2[j], then no operation is needed
# *     - solve(i + 1, j + 1)
# * Otherwise, we need to try all three of the operations
# *     Insert = solve(i, j + 1) + 1 (insert word2[j] into word1)
# *     Delete = solve(i + 1, j) + 1 (remove word1[i])
# *     Replace = solve(i + 1, j + 1) + 1 (replace word1[i] with word2[j])
# ! If one of the strings has all of its characters expended, then we have to consider the remaining characters
# *     if i == n, then return (m - j)
# *         - We need to insert the remaining characters of word2 into word1
# *     if j == m, then return (n - i)
# *          - We need to delete the remaining characters of word1

# ! We only rely on the previous row at any given point
# *     - (i, j), (i - 1, j), (i - 1, j - 1)
# * Thus we can utilize a rolling array and recycle rows as necessary
# ! Since we don't have `m` rows to preprocess the row empty case for, we have to lazily compute it
# *     - `i` and `j` start at 1, so dp[i][0] never receives a value
# *     - Instead, we grab it from (dp[i-1][0] + 1), which is what the preprocessing loop would've done
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "" and word2 == "":
            return 0

        n, m = len(word1), len(word2)

        # * dp[i][j] = Min. no. of operations to convert word1[:i] into word2[:j]
        dp: list[list[int]] = [[0] * (m + 1) for _ in range(2)]
        dp[0][0] = 0  # * An empty string is always equal to an empty string

        # * "" -> "son" needs 3 characters
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, n + 1):
            # * Lazily compute dp[i][0] (we don't have m rows, so couldn't precompute)
            dp[i & 1][0] = dp[(i - 1) & 1][0] + 1

            for j in range(1, m + 1):
                # * Case 1: Characaters match (no operation needed)
                if word1[i - 1] == word2[j - 1]:
                    dp[i & 1][j] = dp[(i - 1) & 1][j - 1]
                else:
                    # * Case 2: Try all three operations
                    insert_op = dp[i & 1][j - 1] + 1
                    delete_op = dp[(i - 1) & 1][j] + 1
                    replace_op = dp[(i - 1) & 1][j - 1] + 1
                    dp[i & 1][j] = min(insert_op, delete_op, replace_op)

        return dp[n & 1][m]


sol: Solution = Solution()
print(sol.minDistance("horse", "ros"))  # * 3
print(sol.minDistance("ros", "horse"))  # * 3
print(sol.minDistance("intention", "execution"))  # * 5
print(sol.minDistance("son", "sonic"))  # * 2
print(sol.minDistance("sonic", "son"))  # * 2
print(sol.minDistance("sonic", "sonic"))  # * 0
print(sol.minDistance("son", "son"))  # * 0 (already equal)
print(sol.minDistance("", ""))  # * 0 (already equal)
print(sol.minDistance("mario", ""))  # * 5 removals
print(sol.minDistance("", "mario"))  # * 5 additions
print(sol.minDistance("sonic", "mario"))  # * 4 replacements
print(sol.minDistance("sonic", "mari"))  # * 4 (1 deletion 3 replacements)
print(sol.minDistance("peach", "peaci"))  # * 1 replacement

# * Time: O(n * m) - There are `n` possible values for `i` and `m` possible values for `j`
# * We are caching the result of each subproblem, so there are only (n * m) unique subproblems to solve

# * Space: O(m) - We are using a rolling array, so the memory usage scales with the number of columns
