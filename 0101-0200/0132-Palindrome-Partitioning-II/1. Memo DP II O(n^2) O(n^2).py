# 132. Palindrome Partitioning II

# * The problem can be rephrased as finding the minimum recursion depth to solve the problem
# * Why? Because in the worst case, the number of cuts is (n - 1)
# * Lets say we have "aba":
# *     - We can cut after index 0, and after index 1 (3 - 1 == 2)
# * And we know that a substring of length 1 is always a palindrome
# * Thus, in the absolute worst case, we could repeatedly take substrings of length 1
# * Ideally we find palindromes though, which allows us to lesssen the amount of recursive calls on the current branch
# * Therefore, we can think of the problem as attempting to maximize the (valid) substring length
# ! Maximizing the (valid) substring length minimizes the recursion depth
# * We can apply dynamic programming here as an optimization
# * The goal is to find the MINIMUM no. of cuts (recursive calls on each branch)
# * If we have "aab", before we hit index 2, we have two possible paths:
# *     - "a", which takes you to (i = 1) -> "a" which takes you to (i = 2)
# *     - "aa", which takes you to (i = 2)
# ! Thus, dp[i] depends on dp[i + 1] (and thus, dp[i + 1] must be computed first)
class Solution:
    def minCut(self, s: str) -> int:
        def solve(start: int) -> int:
            # * Base Case: We can't split an empty string
            if start == n:
                return 0

            min_cuts: int = MAX_INT

            # * Try splitting at every index (every split point)
            for i in range(start, n):
                if is_pal[start][i]:
                    if i + 1 == n:
                        # * No more string remains, thus requiring 0 cuts
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, 1 + solve(i + 1))

            return min_cuts

        # * Base Case: Empty strings and strings of length 1 require 0 cuts
        if len(s) in (0, 1):
            return 0

        n: int = len(s)
        MAX_INT: int = (1 << 31) - 1

        # * is_pal[i][j] = Whether or not substring [i:j+1] is a palindrome
        is_pal: list[list[bool]] = [[False] * n for _ in range(n)]

        # * Precompute palindrome checks
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        return solve(0)


sol: Solution = Solution()
print(sol.minCut("aab"))  # * 1 ("aa", "b")
print(sol.minCut("aaa"))  # * 0 ("aaa")
print(sol.minCut("abcd"))  # * 3 ("a", "b", "c", "d")
print(sol.minCut("ab"))  # * 1 ("a", "b")
print(sol.minCut("abbazyz"))  # * 1 ("abba", "zyz")
print(sol.minCut("abbababbabba"))  # * 2
print(sol.minCut("zabbazabc"))  #  * 3

# * Time: O(n^2) - We precompute all of the palindromes and their respective checks
# * Thus, at each level of recursion, we perform an O(n) loop, and there are `n` levels of recursion at worst

# * Space: O(n^2) - Memoizing all of the palindrome checks requires O(n^2) memory
