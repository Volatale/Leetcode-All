# 78. Subsets

# * At each level of recursion, we have two choices
# *     - Include the element
# *     - Exclude the element
# * A subset is essentially a subsequence (and it can be empty)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(i: int) -> None:
            # * Base Case: Completed the subset
            if i == len(nums):
                results.append(subset[:])
                return

            # * Case 1: Exclude element
            backtrack(i + 1)

            # * Case 2: Include element
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

        subset: list[int] = []
        results: list[list[int]] = []
        backtrack(0)
        return results


# * Time: O(2^n * n) - There are two choices at each level of recursion so the branching factor is 2
# * The depth of recursion can be at most n (n + 1 to be precise)
# * For each subset, we need to create a copy, which takes O(n) in the worst case (the entire input being copied)

# * Space: O(2^n) - The number of subsets given `n` elements is always 2^n
