# 115. Distinct Subsequences

# * At each step, we either take s[i] or we skip it
# * Subsequences give us two options at every possible subproblem
# * We can take advantage of dynamic programming since we have:
# *     - Overlapping subproblems (multiple ways to reach the same (i, j) pair)
# *     - Optimal Substructure (trying to count the number of ways)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def solve(i: int, j: int) -> int:
            # * Check for memoized subproblems
            if (i, j) in memo:
                return memo[(i, j)]

            # * Base Case: Reached the end of i, validate
            if i == len(s):
                return 1 if j == len(t) else 0

            ways: int = 0

            # * Case 1: Take the current char (s[i])
            if j < len(t) and s[i] == t[j]:
                ways += solve(i + 1, j + 1)

            # * Case 2: Don't take the current char (s[i])
            ways += solve(i + 1, j)

            memo[(i, j)] = ways
            return ways

        if len(s) < len(t):
            return 0

        memo: dict[tuple[int, int], int] = {}
        return solve(0, 0)


# * Time: O(n * m) - There are `n` possible values for `i` and `m` possible values for `j`
# * Thus, the number of (i, j) pairs is approximately n * m

# * Space: O(n * m) - There are n * m unique subproblems to cache in the worst case
