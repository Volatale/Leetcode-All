# 44. Wildcard Matching

# * The greedy solution is similar to how a sliding window works
# * We only "expand" the window while we have a "*" to use
# * The greedy nature of this algorithm comes from the fact that the "*" is "lazy"
# *     - That is, we only expand when we HAVE to
# *     - In other words, when there is no other choice
# * Take these examples: s = "abczzzde", p = "ab*de"
# *     - "abc" matches "abc"
# *     - But "*" does not match z, so we have to use the "*" to skip the first "z"
# *         - The same applies for the following "z"s since they don't match either
# ! This algorithm is also similar to backtracking
# * When we find a "*", we do two things:
# *     - Store the current index (so we have the index of the last "*")
# *     - Store the index of the current match
# * "j" backtracks to star + 1
# *     - Which is the index immediately AFTER the last "*"
# * "i" backtracks to match + 1
# *     - Which is the index immediately AFTER the last match
# *     - We are basically choosing to use the "*" to match the current character
# *       hence the + 1 takes us to the next
# ! Greedily assume that we skip all of the "*"
# * But track its index so we can backtrack if necessary
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n: int = len(s)
        m: int = len(p)

        # * Tracks progress through `s` and `p`
        i: int = 0
        j: int = 0

        star: int = -1  # * Index of last "*" found
        match: int = 0  # * Index to backtrack to

        while i < n:
            if j < m and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < m and p[j] == "*":
                star = j  # * Record the index of this star
                match = i  # * The furthest i has successfully travelled thus far
                j += 1  # * Initially treat this as no match (hence no i += 1) so we can still normal match
            elif star != -1:
                # ! Backtrack
                j = star + 1  # * Reset j to where we left off last time
                match += 1  # * Use the "*" to match s[i]
                i = match
            else:
                return False  # * There were no matches and no stars found

        # * Skip any remaining "*" in `p`
        while j < m and p[j] == "*":
            j += 1

        # * i == n, but we don't know if j == m
        return j == m


sol: Solution = Solution()
print(sol.isMatch("aaa", "a*b"))  # * True
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

# * Time: O(n * m) - In the absolute worst case, we repeatedly backtrack
# * Which means we end up doing O(n * m) work. However, in the average case, the complexity is O(n + m)

# * Space: O(1) - The memory usage remains constant regardless of input size
