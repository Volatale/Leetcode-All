# 115. Distinct Subsequences

# * At each step, we either take s[i] or we skip it
# * Subsequences give us two options at every possible subproblem
# * We can take advantage of dynamic programming since we have:
# *     - Overlapping subproblems (multiple ways to reach the same (i, j) pair)
# *     - Optimal Substructure (trying to count the number of ways)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n: int = len(s)
        m: int = len(t)

        # * dp[i][j] = No. of distinct subsequences for up to s[0:i] and t[0:j] respectively
        dp: list[list[int]] = [[0] * (m + 1) for _ in range(2)]
        dp[0][0] = 1  # * It is always possible create an empty string

        for i in range(1, n + 1):
            dp[i & 1][0] = 1  # * It is always possible to create an empty string

            for j in range(1, m + 1):
                # * Case 1: Exclude the current character
                dp[i & 1][j] = dp[(i - 1) & 1][j]

                # * Case 2: Include the current character
                if j - 1 >= 0 and s[i - 1] == t[j - 1]:
                    dp[i & 1][j] += dp[(i - 1) & 1][j - 1]

        return dp[n & 1][m]


sol: Solution = Solution()
print(sol.numDistinct("aa", "aa"))
print(sol.numDistinct("rabbbit", "rabbit"))
print(sol.numDistinct("babgbag", "bag"))


# * Time: O(n * m) - There are `n` possible values for `i` and `m` possible values for `j`
# * Thus, the number of (i, j) pairs is approximately n * m

# * Space: O(m) - We have a (2 x m) matrix, so the memory usage scales solely based on the length of t
