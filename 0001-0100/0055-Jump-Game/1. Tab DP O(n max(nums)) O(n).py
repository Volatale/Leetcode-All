# * 55. Jump Game


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n: int = len(nums)

        # * dp[i] = Whether or not we can reach index i
        dp: list[bool] = [False] * n
        dp[0] = True  # * We can always reach index 0 (we start there)

        for i in range(0, n - 1):
            # * We can't reach this step from anywhere
            if nums[i] == 0:
                continue

            # * Try all jumps within range [1, nums[i]]
            for j in range(1, nums[i] + 1):
                if i + j < n and dp[i]:
                    dp[i + j] = True

        return dp[n - 1]


sol: Solution = Solution()
print(sol.canJump([1, 1, 1]))
print(sol.canJump([2, 3, 1, 1, 4]))  # * True
print(sol.canJump([3, 2, 1, 0, 4]))  # * False
print(sol.canJump([3, 1, 0, 0, 1, 0, 0]))  # * False
print(sol.canJump([1, 0, 0, 2]))  # * False
print(sol.canJump([4, 0, 0, 0, 0]))  # * True
print(sol.canJump([2, 3, 1, 10, 0, 0, 0, 4]))  # * True

# * Time: O(n * max(nums)) - There are `n` outer iterations in the worst case
# * Within each iteration, we perform an O(max(nums)) loop in the worst case

# * Space: O(n) - The size of the dp array scales with the input size
# * There are `n` unique subproblems to cache in the worst case
