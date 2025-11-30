# 97. Interleaving String

# * Essentially, choose try to match characters in s3 using either a character in s1 or s2 at each index
# * Once we use a character, we can't reuse it, so we progress in either string
# * Since there are two strings to "progress" (strings from which we expend characters), we use two pointers
# * There are three cases to consider
# *     s1[i] == s3[index] -> i + 1
# *     s2[j] == s3[index] -> j + 1
# *     Neither works, so we can't progress; return False
# * We have to try both possibilities:
# *     - Take the following example: "a", "ab", "aba"
# *     - Both strings hold an "a" in their 0th indices, so technically we could use either
# *       However, if we use s1's "a", then "index" now points to a "b" (so we need to find a "b")
# *       And we don't have one... But if we use s2's "a", then we have access to s2's following "b"


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # * String lengths do not match up
        if len(s1) + len(s2) != len(s3):
            return False

        n: int = len(s1)
        m: int = len(s2)

        # * dp[i][j] = Whether or not we can contribute to s3 using s1[0:i + 1] and s2[0:j + 1]
        dp: list[list[bool]] = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        # * It is always poissible to make a string of length 0
        dp[0][0] = True

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if j == 0 and i > 0:
                    # * Case 1: s1[i] matches s3[i + j - 1]
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                elif i == 0 and j > 0:
                    # * Case 2: s2[j] matches s3[i + j - 1]
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif i > 0 and j > 0:
                    # * Try both
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                    )

        return dp[n][m]


sol: Solution = Solution()
print(sol.isInterleave("aa", "bc", "abac"))
print(sol.isInterleave("aaa", "aaa", "aaaaaa"))
print(sol.isInterleave("", "", ""))
print(sol.isInterleave("abc", "def", "abcdef"))
print(sol.isInterleave("def", "abc", "abcdef"))
print(sol.isInterleave("a", "b", "ab"))
print(sol.isInterleave("", "b", "b"))
print(sol.isInterleave("a", "", "a"))
print(sol.isInterleave("a", "", "a"))

# * Time: O(n * m) - There are `n` unique values for `i` and `m` unique values for `j`
# * We are caching the result of subproblems, so there are (n * m) unique subproblems in total

# * Space: O(n * m) - Since there are `n` unique values for `i` and `m` unique values for `j`
# * There are (n * m) unique subproblems to cache
