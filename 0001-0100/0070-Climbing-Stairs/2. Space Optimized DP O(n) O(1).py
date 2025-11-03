# 70. Climbing Stairs

# * Start at `n`, and at each level of recursion, try jumping one AND two steps
# * We want the number of distinct ways among both paths, so we sum the results
# ! The recurrence relation looks like: F(n) = F(n - 1) + F(n - 2)
# * Thus, we only need the two previous values to compute the current
# * Therefore it is possible to remove the `dp` array entirely and solely rely on two values
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        # * There is only 1 way to get to the 0th and 1st steps
        first: int = 1  # * dp[0] (1 way, because we start here)
        second: int = 1  # * dp[1] (make a 1 jump from first)

        # * dp[i] = dp[i - 2] + dp[i - 1]
        for _ in range(2, n + 1):
            third: int = first + second
            first = second
            second = third

        return second


sol: Solution = Solution()
print(sol.climbStairs(1))  # * 1
print(sol.climbStairs(2))  # * 2
print(sol.climbStairs(3))  # * 3
print(sol.climbStairs(4))  # * 5
print(sol.climbStairs(5))  # * 8
print(sol.climbStairs(6))  # * 13
print(sol.climbStairs(7))  # * 21

# * Time: O(n) - There are `n` unique values of `i`, hence the time taken scales with `n`

# * Space: O(1) - The memory usage remains constant regardless of input size
# * We removed the necessecity of the `dp` array, so we only need two integers
