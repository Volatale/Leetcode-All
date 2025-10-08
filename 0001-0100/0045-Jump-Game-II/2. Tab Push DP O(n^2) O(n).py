class Solution:
    def jump(self, nums: list[int]) -> int:
        n: int = len(nums)
        INT_MAX: int = (1 << 31) - 1

        # * dp[i] = Min no. of jumps to get to index `i`
        dp: list[int] = [INT_MAX] * n
        dp[0] = 0  # * We start at index 0

        for i in range(n):
            # * We can't make any jumps
            if nums[i] == 0:
                continue

            # * Make any number of jumps in the range 1..nums[i]
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    break

                if dp[i] != INT_MAX:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n - 1]


sol: Solution = Solution()
print(sol.jump([2, 3, 1, 1, 4]))  # * 2
print(sol.jump([1, 1, 1]))  # * 2
print(sol.jump([4]))  # * 0
print(sol.jump([1, 2, 1, 2, 1, 2]))  # * 3
print(sol.jump([2, 3, 0, 1, 2]))  # * 2

# * Time: O(n^2) - For each index `i`, we do nums[i] inner iterations
# * The number of iterations we do is bounded by i + j (where 1 <= j <= nums[i])
# * In the worst case, we do n^2 iterations (imagine we have [3, 3, 3, 3])
# * We do 3 iterations, then 2, then 1, then 0: (n * (n + 1)) / 2

# * Space: O(n) - There are `n` subproblems to cache the results for
