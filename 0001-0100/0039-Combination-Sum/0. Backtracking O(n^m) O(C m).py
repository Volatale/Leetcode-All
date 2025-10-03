# 39. Combination Sum

# * We are given an int[] `candidates` and an int `target`
# * The goal is to return an array of the unique combinations that such to `target`
# * Naturally, this is a backtracking problem since it involves combinations
# ! We are allowed to reuse the same element multiple times within the same combination
# * Backtracking algorithms can be optimized by pruning redundant branches
# *     - In our case, if we sort the array, we ensure monotonicity exists within the array
# * At each level of recursion, we try all of the candidates in `candidates`
# *       target - candidates[i] = new_target
# * Thus, since the array is sorted, if (target - candidates[i] > target)
# *     - Then we might as well break out of the current loop
# *     - The array is monotonically increasing, and candidate[i] failed
# *       Thus we can assume that any later candidates in the subarray `candidates[i + 1.. n - 1]` will ALSO fail
# ! The parameter `start` is used to determine what index we should start iterating from
# *     - The purpose being to avoid redundant work


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
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
        if target < 0:
            return
        if target == 0:
            results.append([*curr])
            return

        # * Try every candidate (we pass `i` so we can potentially reuse the number)
        for i in range(start, len(candidates)):
            # * candidates[i] > target, and the array is sorted, cand[i..n-1] > target too
            if target - candidates[i] < 0:
                break

            curr.append(candidates[i])  # * Choose candidate
            self._backtrack(i, curr, candidates, target - candidates[i], results)
            curr.pop()  # * Un-choose candidate


sol: Solution = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))  # * [[2, 2, 3], [7]]
print(sol.combinationSum([1], 3))  # * [[1, 1, 1]]
print(sol.combinationSum([1, 2, 5], 3))  # * [[1, 1, 1], [1, 2]]

# * Time: O(n^m) - The branching factor is `n` (len(candidates))
# * The depth of the recursion scales with target `m`
# * In the worst case, we subtract 1 from target at each level of recursion

# * Space O(C * m) - Where `c` is the number of valid combinations, and `m` is target
# * In the worst case, a valid combination will have `m` length ([1], target = 50 -> [1] * 50)
