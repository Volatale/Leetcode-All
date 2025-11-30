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
        def solve(i: int, j: int) -> bool:
            # * Check for memoized subproblem
            if (i, j) in memo:
                return memo[(i, j)]

            # * Base Case: Consumed both s1 and s2 and matched s3 completely
            if i + j == len(s3):
                return i == len(s1) and j == len(s2)

            # * Case 1: s1[i] == s3[i + j]
            if s1[i] == s3[i + j] and solve(i + 1, j):
                memo[(i, j)] = True
                return True

            # * Case 2: s2[j] == s3[i + j]
            if s2[j] == s3[i + j] and solve(i, j + 1):
                memo[(i, j)] = True
                return True

            memo[(i, j)] = False
            return False

        memo: dict[tuple[int, int], bool] = {}
        return solve(0, 0)


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
# * We are memoizing the result of subproblems, so there are (n * m) unique subproblems in total

# * Space: O(n * m) - Since there are `n` unique values for `i` and `m` unique values for `j`
# * There are (n * m) unique subproblems to memoize
