# 77. Combinations

# * We are not able to choose the same element multiple times within the same combination
# * So in other words, this involves combinations WITHOUT replacement
# * At each level of recursion, we try appending every element to the combination list
# * Then, we backtrack to undo the work
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(start: int) -> None:
            if len(comb) == k:
                results.append(comb[:])
                return

            # * Try choosing each of the `n` numbers in each position
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1)
                comb.pop()

        results: list[list[int]] = []
        comb: list[int] = []
        backtrack(1)
        return results


# * Time: O(n^k) - The branching factor is `n` and the depth of recursion is `k`

# * Space: O(C(n,k)) - The space usage scales with the number of combinations
