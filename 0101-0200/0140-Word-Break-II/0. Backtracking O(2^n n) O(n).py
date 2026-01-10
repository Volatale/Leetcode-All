# 140. Word Break II

# * We essentially have to find a path to the end of the string `s` using words in `wordDict`
# *     - So it is similar to the previous problem (Leetcode 139. Word Break)
# * Except in this version, we need to find all possible paths and not just one
# * Whenever we need to enumerate all possible branches/paths, we can think of using Backtracking
# * And using backtracking, we can prune paths that won't lead anywhere
# * The immediate thought is then to try every possible word in `wordDict` at every possible index `i` (in `s`)
# !     - However, this is slow, and unnecessary
# * Since we know each of the words in `wordDict` is unique, we can instead grab substrings and compare them
# * There won't be any overlap since the starting points (i) are all unique, as are all the words in `wordDict`
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        def solve(i: int):
            # * Base Case: Found a valid path
            if i == n:
                # * Append a space between each word and add it to the results
                results.append(" ".join(path))
                return

            # * Starting from `i`, try every possible suffix such that s[i:n]
            for j in range(i, n):
                substring: str = s[i : j + 1]

                # * Validate canddiate
                if substring in words:
                    path.append(substring)  # * Choose candidate
                    solve(j + 1)  # * Explore candidate
                    path.pop()  # * Unchoose candidate

        n: int = len(s)
        results: list[str] = []
        path: list[str] = []
        words: set[str] = set(wordDict)
        solve(0)
        return results


sol: Solution = Solution()
print(sol.wordBreak("sonicthehedgehog", ["sonic", "the", "hedgehog"]))
print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(
    sol.wordBreak(
        "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
    )
)
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

# * Time: O(2^n * n) - At every index `i`, you can choose any j >= i such that s[i:j+1] is a word
# * So at worst (when every substring is a word), each position has roughly (n - i) choices
# * The number of ways to cut a string is roughly 2^{n-1} because we can either cut or not cut at each index
# * The extra `n` factor comes from the joining of the path array

# * Space: O(n) - The maximum recursion depth is at most `n`, and the `words` set scales accordingly
