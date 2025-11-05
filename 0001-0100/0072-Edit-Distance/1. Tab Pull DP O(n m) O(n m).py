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
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "" and word2 == "":
            return 0

        n, m = len(word1), len(word2)

        # * dp[i][j] = Min. no. of operations to convert word1[:i] into word2[:j]
        dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # * An empty string is always equal to an empty string

        # * Handle case where word1 == "" and word2 isn't doesn't
        # * Each successive character needed takes 1 additional operation
        # * "" -> "son" needs 3 characters
        for j in range(1, m + 1):
            # dp[0][j] = m - j
            dp[0][j] = dp[0][j - 1] + 1

        # # * Handle case where word1 isn't empty and word2 == ""
        for i in range(1, n + 1):
            # dp[i][0] = n - i
            dp[i][0] = dp[i - 1][0] + 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # * Case 1: Characaters match (no operation needed)
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # * Case 2: Try all three operations
                    insert_op = dp[i][j - 1] + 1
                    delete_op = dp[i - 1][j] + 1
                    replace_op = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(insert_op, delete_op, replace_op)

        return dp[n][m]


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

# * Space: O(n * m) - Since there are (n * m) unique subproblems, all of their results must be cached
