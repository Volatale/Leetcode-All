# 131. Palindrome Partition

# * The definition for a palindome is as follows:
# *     - Outer characters must match
# *     - AND the inner substring must also be a palindrome
# * So we can think of this as a recursive relationship
# * In the to pointer palindrome check, we do:
# *     - s[left] == s[right], then we do `left += 1` and `right -= 1`
# *     - So we check the OUTER characters, then proceed to check the INNER substring
# *       In other words, we converge upon the center
# ! To avoid the recomputation of palindromes, we can instead use dynamic programming via the above logic
# * Lets say we have "ababa"
# *     - s[0] == s[4]
# *     - s[1] == s[3]
# *     - s[2] == s[2]
# * Now, if we take the DP approach:
# *     - dp[0][4] depends on dp[1][3]
# *     - dp[1][3] depends on dp[2][2]
# *     - dp[2][2] = True
# ! "ababa" cannot be declared as a palindrome without first confirming "aba"
# * Palindromes of length 1 to 3 are trivial, so we simply check if the difference between i and j <= 2
# *     - A palindrome of length 1 is always a palindrome -> "a"
# *     - A palindrome of length 2 can potentially be a palindrome -> "aa", but "ab" is not
# *         - However, in this case, we'd have already confirmed that s[0] != s[1] so we don't get a false positive
# *     - A palindrome of length 3 must fulfill s[0] == s[2], and then (i - j) is always <= 2 (so it would be valid palindrome)
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def backtrack(start: int, path: list[str]):
            # * Base Case: Used all characters
            if start == len(s):
                results.append(path[:])
                return

            # * Try every substring from the current level
            for i in range(start, len(s)):
                # * Validate candidate
                if dp[start][i]:
                    path.append(s[start : i + 1])  # * Choose candidate
                    backtrack(i + 1, path)  # * Explore branch
                    path.pop()  # * Unchoose candidate

        n: int = len(s)
        results: list[list[str]] = []
        dp: list[list[bool]] = [[False] * n for _ in range(n)]

        # * Precompute palindrome results
        # * s[0][4] depends on s[1][3]. s[1][3] depends on s[2][2] (i + 1, j - 1)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        backtrack(0, [])
        return results


sol: Solution = Solution()
print(sol.partition("ababa"))
print(sol.partition("aab"))  # * [["a", "a", "b"], ["aa", "b"]]
print(sol.partition("a"))  # * [["a"]]
print(sol.partition("abc"))  # * [["a", "b", "c"]]
print(sol.partition("abbab"))

# * Time: O(2^n + n^2) - We have two choices at each level of recursion
# * It takes O(n^2) to generate the DP table for the palindromes
# * Additionally, within each level of recursion, we have an O(n) loop
# * We are no longer computing each substring, so the lookup takes O(1)

# * Space: O(n^2) - If we have a string like "aaaaa", every substring is a substring
# * And all of these substrings are included in the resulting array
