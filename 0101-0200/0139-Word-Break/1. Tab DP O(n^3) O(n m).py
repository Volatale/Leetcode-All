# 139. Word Break

# * We are just trying to reach index `n` by using words in `wordDict`
# * This can be optimized via Dynamic Programming due to the following reasons:
# *     - Subproblems are only dependent one way (dp[i] depends on dp[i + len(substring)])
# *     - We are trying to `optimize` our path such that we can complete it in general (not necessarily in the minimum steps)
# * Thus, we have Overlapping Subproblems and Optimal Substructure
# ! We iterate backwards because in the recursive version, we iterated bottom-up
# *     - Thus the subproblems must be computed in top-down order for the iterative version
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n: int = len(s)
        words: set[str] = set(wordDict)

        # * dp[i] = Whether we can reach the end from index `i`
        dp: list[bool] = [False] * (n + 1)
        dp[-1] = True

        # * Keep extending from `i` to create substrings
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                substring: str = s[i : j + 1]

                if substring in words and dp[i + len(substring)]:
                    dp[i] = True

        return dp[0]


sol: Solution = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))  # * True
print(sol.wordBreak("sonic", ["s", "o", "n", "i", "c"]))  # * True
print(sol.wordBreak("shadow", ["shadow"]))  # * True
print(sol.wordBreak("a", ["b"]))  # * False
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # * False

# * Time: O(n^3) - There are `n` possible values for start, and within each level of recursion, we have an O(n) loop
# * Within each iteration of that loop, in the worst case, we create a string of length n

# * Space: O(n * m) - There are `n` unique subproblems to cache values for
# * The `words` set's size scales with the size of the wordDict, and in the worst case each word is the same length
