# 35. Search Insert Position

# * We are given a sorted, distinct int[]
# * The goal is to return the index of `target`, or the index where it WOULD be if it existed
# ! Since we have a distinct, sorted array, we have a monotonically increasing array
# * Indices themselves are also monotonically increasing
# ! Thus, our search space is the range of indices [0, n]
# *     - The range of indices is [0, n] and not [0, n - 1] because the inserted element may exist at the END
# * For example, imagine we have [1, 2, 3] and `target` = 4
# *     - The correct (ordered) insertion position is therefore index 3
# *         - If the search space were [0, n - 1], then we'd binary search over (0, 1, 2)
# *     - But we actually want to binary search over (1, 2, 3, 4)
# *         - Thus, the length of the array should be included in the search space


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        # * The search space is the range of indices [0, n]
        left: int = 0
        right: int = len(nums)

        while left < right:
            # * `mid` represents the current index we are checking
            mid: int = left + ((right - left) >> 1)

            if nums[mid] >= target:
                right = mid  # * Found target, or it exists in the left partition
            else:
                left = mid + 1  # * The target exists in the right partition

        return left


sol: Solution = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))  # * 2
print(sol.searchInsert([1, 3, 5, 6], 7))  # * 4
print(sol.searchInsert([1, 3, 5, 6], 1))  # * 0
print(sol.searchInsert([1, 2, 3], 3))  # * 2
print(sol.searchInsert([1], 2))  # * 1
print(sol.searchInsert([5], 0))  # * 0

# * Time: O(log n) - The search space is halved every iteration

# * Space: O(1) - The memory usage remains constant regardless of input size
