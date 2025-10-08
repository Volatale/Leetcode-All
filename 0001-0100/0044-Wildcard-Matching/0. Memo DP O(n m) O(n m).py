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

# ! We use memoization because otherwise the time complexity is O(2^(n+m))
# *     - In the worst case, at each level of recursion, we have two branches
# *         - That is, the case where we have p[j] == "*"
# *             We can either skip the "*" (i, j + 1)
# *             Or we can match the "*" (i + 1, j)
# *     - The other case is simply linear (since we progress both `i` and `j`)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo: dict[tuple[int, int], bool] = {}
        return self._dp(0, 0, s, p, memo)

    def _dp(
        self, i: int, j: int, s: str, p: str, memo: dict[tuple[int, int], bool]
    ) -> bool:
        # * Check for overlapping subproblems
        if (i, j) in memo:
            return memo[(i, j)]

        # * Success Base Case: both strings consumed
        if i == len(s) and j == len(p):
            return True

        # * `p` was consumed, but `s` hasn't been consumed
        if j == len(p):
            return False

        # * If `s` is consumed, the rest of `p` must be all "*"
        if i == len(s):
            return all(x == "*" for x in p[j:])

        # * Match characters
        if s[i] == p[j] or p[j] == "?":
            memo[(i, j)] = self._dp(i + 1, j + 1, s, p, memo)
        elif p[j] == "*":
            # * The "*" wildcard can either match a character or not match anything
            memo[(i, j)] = self._dp(i + 1, j, s, p, memo) or self._dp(
                i, j + 1, s, p, memo
            )
        else:
            # * No match
            memo[(i, j)] = False

        return memo[(i, j)]


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

# * Time: O(n * m) - In the worst case, we have a branching factor of 2 (the "*" case)
# * However, we are using memoization to cache subproblems
# * The length of `s` is n and the length of `p` is m, thus there are (n * m + 2) unique subproblems

# * Space: O(n * m) - There are (n * m + 2) unique subproblems, and (n * m) are cached within `memo`
