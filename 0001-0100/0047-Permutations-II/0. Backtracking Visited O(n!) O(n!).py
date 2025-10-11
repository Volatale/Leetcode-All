# 47. Permutations II

# * We need to return a list of every UNIQUE permutation
# * Thus, the input amy contain duplicates
# * To handle duplicates, we should sort the array to ensure monotonicity
# * Then, if i > start, skip any duplicate elements because they will lead to duplicate permutations
# ! Use a visited array to track which indices have already been used
# * if i > 0 and nums[i-1] == nums[i], then we have an adjacent duplicate
# * However, we also need to ensure that visited[i-1] HAS been used
# *     - If it wasn't, then we know we should skip the current element because it will lead to a duplicate permutation
# * Why do we need to handle duplicates this way?
# * Imagine we have an input like [1, 1, 2]
# * The first permutation we encounter is [1, 1, 2]
# * However, in the first stack frame, after iteration 0, we risk encountering duplicates
# *     - i = 1, visited = [F, F, F] and path = []
# *     - Since visited[i-1] == False, that means including [1] will lead to another occurrence of [1, 1, 2]
# *         - Why? Because on the next stack frame, visited[0] == False, so then our path becomes [1, 1]
# *         - Then, on the next stack frame after, we get [1, 1, 2], which is exactly the same permutation
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path: list[int]):
            # * Base Case
            if len(path) == len(nums):
                results.append(path[:])
                return

            # * Iterate over every element at every level of recursion
            for i in range(len(nums)):
                # * Don't reuse the same index
                if visited[i]:
                    continue

                # * Imagine we have [1, 1, 2]. We get a permutation of [1, 1, 2]
                # * Now if i = 1, and !visited[i-1], its inclusion would lead to [1, 1, 2] again
                # * Because then visited[0] = False, the next level of recursion leads to [1, 1], then [1, 1, 2]
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visited[i] = False

        nums.sort()  # * Sorting ensures duplicates are adjacent
        results: list[list[int]] = []
        visited = [False] * len(nums)

        backtrack([])
        return results


sol: Solution = Solution()
print(sol.permuteUnique([1, 1, 2]))
print(sol.permuteUnique([1, 2, 3]))
print(sol.permuteUnique([5]))
print(sol.permuteUnique([1, 1]))
print(sol.permuteUnique([0, 1, 0, 0, 9]))

# * Time: O(n!) - The time taken scales with n factorial

# * Space: O(n!) - The number of permutations scales with the size of n
