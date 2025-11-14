# 81. Search in Rotated Sorted Array II

# * Since the array is sorted into a monotoncially non-decreasing order, we know PART of the array is increasing
# * We don't know where the pivot is exactly, but we can determine which side to search in if we break it in half
# * Using binary search, we can determine which of the subarrays ([left:mid] and [mid:right]) is non-decreasing
# * Once we know which subarray is non-decreasing, we can check if it is possible that the value COULD exist in that partition
# * If it is possible, we move the pointers in that direction
# * Otherwise, move them in the other direction
# ! Since the array can contain duplicates, those need to be handled
# * In most cases, this doesn't make a difference, but in sometimes it does
# * If nums[left] == nums[mid] and nums[mid] == nums[right], then we don't know which side to search
# *      0  1  2  3  4
# *     [1, 0, 1, 1, 1]
# *      L     M     R
# * In the above example, if our target is 1, then it doesn't matter
# * But if our target is 0, we'll end up at the incorrect index at the very end
# * Why? Because the subarray [left:mid] is NOT non-decreasing, so we'll search in [mid + 1:right]
# * But in doing so, we lost the ability to find our target (0)
# * If we instead do this:
# *     0  1  2  3  4
# *    [1, 0, 1, 1, 1]
# *        L  M  R
# * Then now we can see that [left:mid] is monotonically non-decreasing
# * Technically so is 1, but remember that if `1` is our target, we still have at least one left (two in this case)
# ! Essentially, we're removing elements that are equal to both ends, at worst we'd still have nums[mid]
# *     0  1  2      0  1  2
# *    [4, 4, 4] -> [4, 4, 4], target = 4
# *     L  M  R         LR -> Still successful


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # * The search space is the range of indices [0, n-1]
        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            # * `mid` represents the current index we are checking
            mid: int = left + ((right - left) >> 1)

            # * Handles situation where all three point to the same number
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1

            # * Check if [left:mid] is monotonically non-decreasing
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # * Then [mid:right] must be monotonically non-decreasing
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1

        return True if nums[left] == target else False


sol: Solution = Solution()
print(sol.search([3, 4, 5, 1, 2], 4))  # * True
print(sol.search([0, 0, 0, 1, 0], 1))  # * True
print(sol.search([0, 0, 0, 0, 0], 3))  # * False
print(sol.search([1, 0, 0, 0, 0, 1], 1))  # * True
print(sol.search([1, 2, 3], 3))  # * True
print(sol.search([1], 4))  # * False
print(sol.search([1, 2], 1))  # * True
print(sol.search([1, 2], 2))  # * True
print(sol.search([1, 2], 3))  # * False

# * Time: O(n) - In the worst case, the entire array is identical, so the time taken scales with `n`
# * We'd end up processing every element eventually

# * Space: O(1) - The memory usage remains constant regardless of input size
