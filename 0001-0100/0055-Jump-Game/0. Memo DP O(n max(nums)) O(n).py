# * 55. Jump Game

# * At every level of recursion we try making between 1 and nums[i] jumps (inclusive)
# * Our goal is simply to reach the end of the array (n - 1)
# *     - Thus, that is our base case
# ! As per the rules, there is no index beyond n - 1, so we can't "land there"
# *     - Hence, if i >= n, we return False
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        def solve(i: int):
            # * Check for memoized subproblem
            if i in memo:
                return memo[i]

            # * Successfully made it to the last index
            if i == n - 1:
                return True

            # * Travelled too far (or we can't move at all)
            if i >= n or nums[i] == 0:
                return False

            # * Try all of the jumps in the range [1, nums[i]]
            for j in range(1, nums[i] + 1):
                if solve(i + j):
                    memo[i] = True
                    return True

            # * Failed to reach index n - 1
            memo[i] = False
            return False

        n: int = len(nums)
        memo: dict[int, bool] = {}
        return solve(0)


sol: Solution = Solution()
print(sol.canJump([1, 1, 1]))
print(sol.canJump([2, 3, 1, 1, 4]))  # * True
print(sol.canJump([3, 2, 1, 0, 4]))  # * False
print(sol.canJump([3, 1, 0, 0, 1, 0, 0]))  # * False
print(sol.canJump([1, 0, 0, 2]))  # * False
print(sol.canJump([4, 0, 0, 0, 0]))  # * True
print(sol.canJump([2, 3, 1, 10, 0, 0, 0, 4]))  # * True

# * Time: O(n * max(nums)) - There are `n` unique subproblems
# * Within each iteration, we perform an O(max(nums)) loop in the worst case

# * Space: O(n) - The number of unique subproblems scales with the size of the input
# * Additonally, the depth of recursion is O(n) in the worst case
