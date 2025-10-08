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
        memo: list[int] = [-1] * len(nums)
        return self._dp(0, nums, memo)

    def _dp(self, i: int, nums: list[int], memo: list[int]) -> int:
        # * Base Case
        if i == len(nums) - 1:
            return 0

        # * Check for memoized subproblem
        if memo[i] != -1:
            return memo[i]

        min_jumps: int = 1 << 31

        # * Try every possible jump from 1 to nums[i] inclusive
        for j in range(1, nums[i] + 1):
            # * Avoid going out of bounds
            if i + j >= len(nums):
                break

            # * We want the MINIMUM amount of jumps
            min_jumps = min(min_jumps, self._dp(i + j, nums, memo) + 1)

        memo[i] = min_jumps
        return min_jumps


sol: Solution = Solution()
print(sol.jump([2, 3, 1, 1, 4]))  # * 2
print(sol.jump([1, 1, 1]))  # * 2
print(sol.jump([4]))  # * 0
print(sol.jump([1, 2, 1, 2, 1, 2]))  # * 3
print(sol.jump([2, 3, 0, 1, 2]))  # * 2

# * Time: O(n * max(nums)) - There are `n` indices, and at each level of recursion, we have a loop
# * The number of iterations depends on nums[i], so in the worst case, the no. of iterations at each level is max(nums)

# * Space: O(n) - The depth of recursion is at most `n`, and there are `n` subproblems to cache
