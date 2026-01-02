# 132. Palindrome Partitioning II

# * Why iterate in reverse? Because the recursive version used (i + 1)
# *     - min_cuts = min(min_cuts, 1 + solve(i + 1))
# * With recursion, we go as deep as possible and then return to the caller
# *     - Thus, dp[i] = dp[i + 1] means we need to compute dp[i + 1] BEFORE dp[i]
# * When translating that to tabulation, we need to compute in reverse
# *     - Thus, for `i`, we iterate from n to 0
class Solution:
    def minCut(self, s: str) -> int:
        # * Base Case: Empty strings and strings of length 1 require 0 cuts
        if len(s) <= 1:
            return 0

        n: int = len(s)

        # * is_pal[i][j] = Whether or not substring [i:j+1] is a palindrome
        is_pal: list[list[bool]] = [[False] * n for _ in range(n)]

        # * dp[i] = Min. no of splits for s[0:i+1]
        dp: list[int] = [0] * (n + 1)

        # * Precompute palindrome checks
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        for i in range(1, n + 1):
            # * If the prefix is a palindrome, no split needed
            if is_pal[0][i - 1]:
                dp[i] = 0
                continue

            # * There are at most n-1 cuts, but `n` requires less instructions
            best: int = n

            for j in range(1, n + 1):
                if is_pal[j - 1][i - 1]:
                    best = min(best, 1 + dp[j - 1])
            dp[i] = best

        return dp[-1]


sol: Solution = Solution()
print(sol.minCut("aab"))  # * 1 ("aa", "b")
print(sol.minCut("aaa"))  # * 0 ("aaa")
print(sol.minCut("abcd"))  # * 3 ("a", "b", "c", "d")
print(sol.minCut("ab"))  # * 1 ("a", "b")
print(sol.minCut("abbazyz"))  # * 1 ("abba", "zyz")
print(sol.minCut("abbababbabba"))  # * 2
print(sol.minCut("zabbazabc"))  #  * 3

# * Time: O(n^2) - Precomputing all of the palindromes takes O(n^2)
# * Then, it takes a further O(n^2) to compute the subproblems

# * Space: O(n^2) - Caching all of the palindrome checks requires O(n^2) memory
