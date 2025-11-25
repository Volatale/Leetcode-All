# 91. Decode Ways

# * A valid symbol can only have one or two digits
# * In the one digit case, we only used ONE character
# *     - So on the next stack frame we start 1 character ahead
# *     - (i + 1)
# * In the two digit case, we used TWO characters
# *     - So on the next stack frame, we start 2 characters ahead
# *     - (i + 2)
# ! Thus, this can be optimized using dynamic programming
# *     - F(n) = F(n - 1) + F(n - 2)
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0":
            return 0

        n: int = len(s)

        # * dp[i] = No. of ways to decode a string of length `i` (starting)
        dp: list[int] = [0] * (n + 1)

        # * Seed values: there is exactly 1 way to decode strings of length 0 and 1 respectively
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # * Handle single digit case
            if s[i - 1] > "0":
                dp[i] += dp[i - 1]

            # * Handle double digit case
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]

        return dp[n]


sol: Solution = Solution()
print(sol.numDecodings("1"))
print(sol.numDecodings("1"))
print(sol.numDecodings("111"))
print(sol.numDecodings("06"))
print(sol.numDecodings("1201234"))

# * Time: O(n) - The number of iterations scales with the input size

# * Space: O(n) - There are `n` unique subproblems that must be cached
