# 45. Jump Game II

# * From each index `i`, we can jump between 1 and nums[i] (inclusive) steps ahead
# !     - We want the MINIMUM number of jumps required to get to index n - 1
# * It is possible that we end up at the same index from multiple previous subproblems
# * With all of this, we can apply dynamic programming to reduce repetitive work
# *     - We have overlapping subproblems
# *     - We have optimal substructure (the min no. of steps needed to get to n - 1 depends on prior subproblems)
# *     - And we want to minimize the no. of jumps required to get to each index
# ! To minimize the no. of steps required to get to index n - 1, we first need to minimize the steps along the path
# * dp[i] = No. of Steps required to get to index `i`
class Solution:
    def jump(self, nums: list[int]) -> int:
        n: int = len(nums)
        INT_MAX: int = (1 << 31) - 1

        # * dp[i] = Min no. of jumps to get to index `i`
        dp: list[int] = [INT_MAX] * n
        dp[n - 1] = 0  # * We start at index (n - 1)

        for i in range(n - 2, -1, -1):
            # * We can't make any jumps
            if nums[i] == 0:
                continue

            # * Make any number of jumps in the range 1..nums[i]
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    break

                if dp[i + j] != INT_MAX:
                    dp[i] = min(dp[i], dp[i + j] + 1)

        # * The min no. of jumps to get from index to to n-1
        return dp[0]


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
