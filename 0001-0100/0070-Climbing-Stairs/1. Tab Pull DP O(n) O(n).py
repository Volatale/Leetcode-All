# 70. Climbing Stairs

# * Start at `n`, and at each level of recursion, try jumping one AND two steps
# * We want the number of distinct ways among both paths, so we sum the results
# ! This uses tabulation instead of recursion to avoid the extra overhead
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # * dp[i] = No. of distinct ways to reach the top step from i
        dp: list[int] = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # * At each step, sum the no. of ways among all paths (one or two steps)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # * No. of ways to reach the nth stair
        return dp[n]


sol: Solution = Solution()
print(sol.climbStairs(1))  # * 1
print(sol.climbStairs(2))  # * 2
print(sol.climbStairs(3))  # * 3
print(sol.climbStairs(4))  # * 5
print(sol.climbStairs(5))  # * 8
print(sol.climbStairs(6))  # * 13
print(sol.climbStairs(7))  # * 21

# * Time: O(n) - There are `n` unique values of `i`, hence the time taken scales with `n`

# * Space: O(n) - There are `n` unique values of `i`, so there are `n` subproblems that must be cached
