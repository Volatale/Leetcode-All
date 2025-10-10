# 46. Permutations

# * Build each of the permutations progressively as we go
# * From each level of recursion, we try adding every element to the current permutation
# * However, to ensure we don't reuse any elements, we need to track what we've already used
# *     - Thus, we need to use a visited array
# *     - If visited[i], then we have already used nums[i] within the current permutation
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def _backtrack(path: list[int]) -> None:
            # * Base Case
            if len(path) == len(nums):
                results.append(path[:])
                return

            # * Try adding every element at every level
            for i in range(len(nums)):
                # * We can't reuse the same index
                if visited[i]:
                    continue

                visited[i] = True
                path.append(nums[i])
                _backtrack(path)
                path.pop()
                visited[i] = False

        results: list[list[int]] = []
        visited: list[bool] = [False] * len(nums)
        path: list[int] = []

        _backtrack(path)
        return results


sol: Solution = Solution()
print(sol.permute([1, 2, 3]))
print(sol.permute([1, 2]))

# * Time: O(n!) - The time taken scales with n factorial

# * Space: O(n!) - The number of permutations scales with the size of n
