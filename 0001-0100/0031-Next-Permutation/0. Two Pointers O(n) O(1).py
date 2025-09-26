# 31. Next Permutation

# * We are given an int[], and the goal is to return the (lexicographically) next permutation
# * For example, if we have [1, 2, 3], the next lexicographically greater permutation would be [1, 3, 2]
# * In the event there isn't one (in the case of [3, 2, 1]), we return the array in sorted order ([1, 2, 3])
# * Using a monotonic stack here (Next Greater Element style) won't work here
# *     - NGE works when we want to find the next greater element of a SINGLE element
# *     - However, our concern takes the entire array into account
# ! The key insights:
# *     - The next permutation must be:
# *         1. Larger than the previous
# *         2. The smallest possible larger one (so we change the rightmost part to be as little as possible)
# *       How do we achieve this?
# *            Look at the array from right to left
# *     - If it is strictly decreasing (5, 4, 3, 2, 1), we are at the final permutation
# *         In which case the next is simply the reverse of the sequence
# * Otherwise, there is a point at which the sequence begins decreasing
# ! From right to left, find the "pivot" index (where nums[i] < nums[i + 1])
# *     - This is the point at which we can increase the value the least
# ! Then, also from right to left, find the first nums[j] > nums[i]
# * Swap nums[i] and nums[j]
# * Now, nums[0..i] is descending, and nums[i..n-1] is descending
# * But we want the lexicographically SMALLEST permutation
# * So we still need to reverse nums[i + 1..n - 1]


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        if len(nums) <= 1:
            return

        n: int = len(nums)

        # * 1. Find the pivot (rightmost element smaller than the next)
        i: int = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # * 2. Find the first element larger than nums[i] in the descending suffix
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            # * 3. Swap pivot with this next bigger element
            nums[i], nums[j] = nums[j], nums[i]

        # * 4. Reverse this suffix to make it as small as possible
        nums[i + 1 :] = reversed(nums[i + 1 :])


sol: Solution = Solution()
print(sol.nextPermutation([1, 2, 3]))  # * [1, 3, 2]
print(sol.nextPermutation([1, 2, 3, 6, 5, 4]))  # * [1, 2, 4, 3, 5, 6]
print(sol.nextPermutation([3, 2, 1]))  # * [1, 2, 3]
print(sol.nextPermutation([1, 1, 5]))  # * [1, 5, 1]

# * Time: O(n) - In the worst case, we iterate over the entire array twice O(n) + O(n) = O(n)

# * Space: O(1) - The memory usage remains constant regardless of input size
