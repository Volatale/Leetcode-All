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
        memo: dict[tuple[int, int], bool] = {}

        def dp(i: int, j: int) -> bool:
            # * Handle memoization
            if (i, j) in memo:
                return memo[(i, j)]

            # * Check if we reached the end of the pattern
            if j == len(p):
                return i == len(s)

            # * Check if current chars match, or if we have a wildcard
            matched = i < len(s) and p[j] in (s[i], ".")

            result: bool = False  # * Implicitly assume failure

            # * If the next char in `p` is "*", try these options:
            # * Try matching ZERO occurrences in s (i, j + 2), OR, try matching ONE (i + 1, j)
            # *     - In the latter case, "j" STILL points to the "*" (reuse the * to check every possibility)
            # * Otherwise, increment both i and j if the characters match (and no "*")
            if j + 1 < len(p) and p[j + 1] == "*":
                result = dp(i, j + 2) or (matched and dp(i + 1, j))
            else:
                # *
                result = matched and dp(i + 1, j + 1)

            # * Cache the result
            memo[(i, j)] = result
            return result

        return dp(0, 0)


sol: Solution = Solution()
print(sol.isMatch("aa", "a"))  # * False (didn't match index 0)
print(sol.isMatch("aa", "a*"))  # * True (match ANY amount of adjacent a)
print(sol.isMatch("ab", ".*"))  # * True (match ANY amount of ANY character, auto match)
print(sol.isMatch("xywezz", "xy.z*"))  # * False (matched z, but failed at the "w")
print(sol.isMatch("xyabzzz", "x.ab*z"))  # * False
print(sol.isMatch("x", "x*z"))  # * False

# * Time: O(n * m) - Without memoization, the function has a time complexity of O(2^(m *n))
# * In the worst case, within each branch, there are two calls to `dp`
# * The depth of the recursion scales with the lengths of `s` and `p` respectively
# * Due to memoization, the time complexity is reduced to O(n * m)

# * Space: O(n * m) - Without memoization, the memory usage is O(n + m)
# * However, memoization, we need to cache every possible combination of (i, j)
# * Thus, the memory usage scales according to O(n * m)
