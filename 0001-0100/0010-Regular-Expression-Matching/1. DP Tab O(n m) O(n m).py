# 10. Regular Expression Matching

# * We are given an input string `s` and a pattern `p`
# * The goal is to implement REGEX matching with support for `.` and `*`:
# *     - . is a wildcard and should match ANY character
# *     - * matches zero or more of the previous element
# *     - .* means means zero or more of ANY character
# ! The matching should cover the entire input string, not just a partial match
# * Since this is a "matching" problem, it is inherently brute force and recursive
# * There are a few cases that must be handled:
# *     1. p[j] either matches s[i], or p[j] is a wildcard (*)
# *     2. The next character is a "*"
# ! Regardless, everything changes if the next character is "*"
# * if j + 1 < len(p), and p[j + 1] == "*"
# *     - Then we need to handle the kleene star
# ! A kleene star matches ZERO OR MORE occurrences of the PRECEEDING character
# *     - Recursively, the "minimum" work we can do per call is to increment "i" ONCE
# *     - However, since a kleene star is technically infinitely recursive, LEAVE "j" where it is
# *         - This enables us to reuse the same kleene star on the next call (which is what is supposed to happen)
# *     - This approach lets us try every possibility that arose due to the existence of the kleene star
# * if dp(i, j + 2) didn't work, then try dp(i + 1, j)
# *     - In the former case, j is incremented by 2 because we are NOT using the kleene star
# !         - In other words, we try matching ZERO characters using it (thereby moving beyond it and its character)
# *     - In the latter case, we match ONE character, and can reuse the kleene star in the next iteration
# ! Otherwise, we don't have a kleene star, in which case i and j are both incremented once
# * Why do we handle the "." first? Because the "." and s[i] == p[j] are effectively the same
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        # * dp[i][j] = whether s[i:] matches p[j:]. Essentially, (i, j) represent STARTING indices of substrings
        dp: list[list[bool]] = [[False] * (m + 1) for _ in range(n + 1)]

        # * Seed value: Two empty strings always match
        dp[n][m] = True

        # * Fill the table backwards because dp[i][j] relies on FUTURE states (pull DP)
        # * i = n means s[i:] = "" (empty string). i = n - 1 would mean the last character of `s`, NOT empty
        # * j = m means p[j:] = "", but we already handled the base case above, so m - 1
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                # * Handle matched chars, or wildcard
                match: bool = i < n and p[j] in (s[i], ".")

                if j + 1 < m and p[j + 1] == "*":
                    # * Handle wildcard case (ignore wildcard, or use it on 1 char)
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                else:
                    # * The characters matched, so progress both
                    dp[i][j] = match and dp[i + 1][j + 1]

        # * if dp[0][0], then we pattern matched the entire string
        return dp[0][0]


sol: Solution = Solution()
print(sol.isMatch("aa", "a"))  # * False (didn't match index 0)
print(sol.isMatch("aa", "a*"))  # * True (match ANY amount of adjacent a)
print(sol.isMatch("ab", ".*"))  # * True (match ANY amount of ANY character, auto match)
print(sol.isMatch("xywezz", "xy.z*"))  # * False (matched z, but failed at the "w")
print(sol.isMatch("xyabzzz", "x.ab*z"))  # * False
print(sol.isMatch("x", "x*z"))  # * False
print(sol.isMatch("abbcd", "ab*cd"))

# * Time: O(n * m) - We have two nested loops, both of which scale with the length of `s` and `p`

# * Space: O(n * m) - The memory usage scales with the length of both `s` and `p`
# * There are (n + 1) possible values for `i`, and (m + 1) possible values for `j`
# * Since `i` and `j` are independent, the rule of product applies: n * m and not n + M
