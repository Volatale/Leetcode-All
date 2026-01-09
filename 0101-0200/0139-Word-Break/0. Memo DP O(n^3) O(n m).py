# 139. Word Break

# * We are just trying to reach index `n` by using words in `wordDict`
# * This can be optimized via Dynamic Programming due to the following reasons:
# *     - Subproblems are only dependent one way (dp[i] depends on dp[i + len(substring)])
# *     - We are trying to `optimize` our path such that we can complete it in general (not necessarily in the minimum steps)
# * Thus, we have Overlapping Subproblems and Optimal Substructure
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def solve(start: int) -> bool:
            # * Check for memoized subproblem
            if start in memo:
                return memo[start]

            # * Base Case: Successfully created `s`
            if start == n:
                return True

            # * We want to keep extending from `i` to create larger substrings
            for i in range(start, n):
                substring: str = s[start : i + 1]

                # * Prune paths: Only explore valid paths
                if substring in words and solve(start + len(substring)):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        n: int = len(s)
        memo: dict[int, bool] = {}
        words: set[str] = set(wordDict)
        return solve(0)


# * Time: O(n^3) - There are `n` possible values for start, and within each level of recursion, we have an O(n) loop
# * Within each iteration of that loop, in the worst case, we create a string of length n

# * Space: O(n * m) - The maximum recursion depth is `n`, thus the number of unique keys in `memo` is also n
# * The `words` set's size scales with the size of the wordDict, and in the worst case each word is the same length
