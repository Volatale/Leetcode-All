# 44. Wildcard Matching

# * We are given two input strings `s` and `p` and we need to implement wildcard matching
# * The wildcard matching behaviour is as follows:
# *     - A "?" matches any singular character
# *     - A "*" matches any sequence of characters (including an empty sequence)
# * Thus, we have a few cases to consider
# * In the most basic case:
# *     - If s[i] == p[j] or p[j] == "?", then we have a match
# * However, the "*" case is different
# *     - If p[j] == "*", then we can either use the "*", or we can ignore it
# ! When it comes to base cases, we have a few cases to consider
# *     - The case where we consume both `s` and `p`
# *          - Return True
# *     - The case where we consumed `p` but not `s`
# *         - Return False, because the matching failed (both `s` and `p` must be consumed)
# *     - The case where we consumed `s` but not `p`
# *         - In this case, the rest of the characters in `p` must be "*"
# *           If they aren't, then there is no way to consume the rest of the characters in `p`
# *         - So return False

# * An empty string always matches an empty string
# *     - However, an empty string also matches a sequence of "*"
# *     - Hence we precompute the first (0th) row
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n: int = len(s)
        m: int = len(p)

        # * dp[i][j] = whether s[:i] matches p[:j] (we include the empty prefixes at index 0)
        dp: list[list[bool]] = [[False] * (m + 1) for _ in range(n + 1)]

        # * Seed Value: "" matches with ""
        dp[0][0] = True

        # * If string is empty, pattern must be all "*"
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # * We either have a match or p's char is a "?"
                if p[j - 1] == s[i - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # * Try skipping the "*" and try using the "*"
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[n][m]


sol: Solution = Solution()
print(sol.isMatch("", ""))  # * True
print(sol.isMatch("aa", "a"))  # * False
print(sol.isMatch("aa", "aa"))  # * True
print(sol.isMatch("aa", ""))  # * False
print(sol.isMatch("aa", "*"))  # * True
print(sol.isMatch("", "*"))  # * True
print(sol.isMatch("cb", "?a"))  # * False
print(sol.isMatch("sonic", "?????"))  # * True
print(sol.isMatch("sonic", "??????"))  # * False
print(sol.isMatch("sonic", ""))  # * False
print(sol.isMatch("wdadw", "adwda*"))  # * False
print(sol.isMatch("abcdefgh", "abc*"))  # * True
print(sol.isMatch("abcdefgh", "a*"))  # * True
print(sol.isMatch("abcdefgh", "a*l"))  # * False

# * Time: O(n * m) - The number of subproblems scales with the size of both inputs' lengths (n and m)

# * Space: O(n * m) - There are (n * m + 2) unique subproblems, and (n * m) subproblems are cached
