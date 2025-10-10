# 46. Permutations

# * We need to form every possible permutation
# * To achieve this, we can apply a backtracking approach
# *     - Swap nums[i] and nums[start] before the exploration (as the candidate choice)
# *     - Swap nums[i] and nums[start] after the exploration (to undo the candidate choice)
# * At each level of recursion:
# *     - Index `start` is the index that is always swapped per level
# *     - index `i` is the index non-recuring index that we swap with
# * Everything to the left of `start` is essentially locked into place for the remainder of this branch
# *     - Hence we pass (start + 1) as a parameter within each iteration
# *     - By doing this at every level of recursion and every iteration, we end up getting every permutation
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results: list[list[int]] = []
        self._backtrack(0, nums, results)
        return results

    def _backtrack(self, start: int, nums: list[int], results: list[list[int]]):
        # * Base Case
        if start == len(nums):
            results.append([*nums])
            return

        # * Try every possible permutation at every level of recursion
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]  # * Choose candidate
            self._backtrack(start + 1, nums, results)  # * Explore
            nums[i], nums[start] = nums[start], nums[i]  # * Un-choose candidate


sol: Solution = Solution()
print(sol.permute([1, 2, 3]))

# * Time: O(n!) - The time taken scales with n factorial

# * Space: O(n!) - The number of permutations scales with the size of n
