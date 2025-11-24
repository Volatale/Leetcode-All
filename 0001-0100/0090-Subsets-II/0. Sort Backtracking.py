# 90. Subsets II

# * At each level of recursion, we have two choices
# *     - Include the element
# *     - Exclude the element
# * A subset is essentially a subsequence (and can be empty)
# * In our case, we want to exclude the duplicate subsets
# ! Thus, we can sort the input to ensure a non-monotonically decreasing array
# * Then, at each level of recursion, if nums[i] == nums[i + 1], skip the current element
# *     - Why? Its inclusion won't help at all; it'll only lead to a duplicate
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def backtrack(i: int) -> None:
            # * Base Case: Completed the subset
            if i == n:
                results.append(subset[:])
                return

            # * Case 1: Include the element (and ignore duplicates)
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # * Skip to the end of the duplicate series
            while i > 0 and nums[i] == nums[i - 1]:
                i += 1

            # * Case 2: Exclude the element
            backtrack(i + 1)

        n: int = len(nums)
        subset: list[int] = []
        results: list[list[int]] = []
        nums.sort()  # * Sort the array to ensure a non-decreasing ordering

        backtrack(0)
        return results


# * Time: O(n * 2^n) - At each level of recursion, we have two choices
# * Additionally, within each stack frame, we potentially create an O(n) copy of `subset`

# * Space: O(2^n) - In the worst case, there are no duplicates
# * And the number of subsets given `n` elements is at most 2^n
