# 70. Climbing Stairs

# * Start at `n`, and at each level of recursion, try jumping one AND two steps
# * We want the number of distinct ways among both paths, so we sum the results
class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(i: int) -> int:
            # * Check for memoized subproblem
            if i in memo:
                return memo[i]

            # * Base Case: Successfully reached nth stair
            if i == 0:
                return 1

            # * Base Case: We jumped too far
            if i < 0:
                return 0

            # * Try climbing one step and two step at each level, take the sum of both
            memo[i] = solve(i - 1) + solve(i - 2)
            return memo[i]

        memo: dict[int, int] = {}
        solve(n)
        return memo[n]


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
