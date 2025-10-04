# 40. Combination Sum II

# * The problem is essentially the same as Combination Sum
# *     - Except that `candidates` may contain duplicates
# *     - And we cannot reuse the same element multiple times
# * Thus, whenever we are exploring a branch, we pass `i + 1` to the parameter of `start`
# *     - This is as opposed to passing `i` itself
# *     - `i + 1` prevents the next stack frame from being able to reuse the same index we just used
# ! Since `candidates` may contain duplicates, we need to handle this case
# * For example, imagine we have ([1, 1, 7], target = 8)
# *     - [1, 7] is valid (using indices (0, 2) respectively)
# *     - But so is [1, 7] (using indices (1, 2) respectively)
# ! The problem is the "root" values (the 1s) are identical
# * To handle this case, if (i > start and candidates[i] == candidates[i-1])
# *     - Then we'll skip to the next index and only get indices (0, 2) instead of (1, 2)
# * Put simply, skip all adjacent duplicates at every level of recursion
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results: list[list[int]] = []
        candidates.sort()
        self._backtrack(0, [], candidates, target, results)
        return results

    def _backtrack(
        self,
        start: int,
        curr: list[int],
        candidates: list[int],
        target: int,
        results: list[list[int]],
    ):
        # * (Negative) Base Case
        if target < 0:
            return

        # * (Positive) Base Case
        if target == 0:
            results.append([*curr])
            return

        # * Try all of the candidates from [start..n-1] at each level of recursion
        for i in range(start, len(candidates)):
            # * candidates[i] > target, and the array is sorted. cand[i..n-1] > target too
            if target - candidates[i] < 0:
                break

            # * Skip the duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            curr.append(candidates[i])  # * Choose candidate
            self._backtrack(i + 1, curr, candidates, target - candidates[i], results)
            curr.pop()  # * Un-choose candidate


sol: Solution = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(sol.combinationSum2([2, 5, 2, 1, 1], 5))
print(sol.combinationSum2([5, 1, 2], 5))
print(sol.combinationSum2([3, 6, 9], 9))
print(sol.combinationSum2([2, 5, 1, 1, 1], 5))

# * Time: O(n^m) - The branching factor is `n` (len(candidates))
# * The depth of the recursion scales with target `m`
# * In the worst case, we subtract 1 from target at each level of recursion

# * Space O(C * m) - Where `c` is the number of valid combinations, and `m` is target
# * In the worst case, a valid combination will have `m` length ([1], target = 50 -> [1] * 50)
