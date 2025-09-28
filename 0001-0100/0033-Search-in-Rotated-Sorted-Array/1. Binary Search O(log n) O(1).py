# 33. Search in Rotated Sorted Array


# * We are given a rotated SORTED array (of unique values)
# * The goal is to find the index of `target` in `nums`
# *     - If it doesn't exist, we return -1
# * Since the array is sorted, and we know we want to find an index within some set of indices:
# ! The search space is the array of indices [0..i]
# ! And we know the array is monotonically increasing (as are the indices)
# * Thus, we can say we have a sorted search space
# * Split the array up into two partitions
# *     - [left..mid]
# *     - [mid..right]
# * Due to the rotation, ONE of these subarrays will be monotonically increasing
# * Since that is the case, we can determine whether or not it is possible that `target` exists within it
# * For example, if we have [1, 2, 3, 4] and target is = 2
# *     - 1 <= target and target <= 4
# ! Therefore, it is entirely possible that `target` exist in the subarray [left..mid]
# * Since the input contains unique integers, if `target` can exist in ONE subarray, it cannot ALSO exist in the other
# * Therefore, we can eliminate the other subarray from consideration
# * Repeat this process until completion
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # * The array is empty, so `target` cannot possibly exist within
        if len(nums) == 0:
            return -1

        # * The search space is the range of indices [0..n - 1]
        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            # * `mid` represents the index we are currently searching
            mid: int = left + ((right - left) >> 1)

            # * [left..mid] is a monotonically increasing subarray
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid  # * `target` could exist in the [left..mid] subarray
                else:
                    left = mid + 1  # * `target` does NOT exist in this subarray
            # * [left..mid] is NOT monotonically increasing
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid  # * `target` could exist in the [mid..right] subarray
                else:
                    right = mid - 1  # * `target` does NOT exist in this subarray

        return left if nums[left] == target else -1


sol: Solution = Solution()
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # * 4
print(sol.search([1, 2, 3, 4], 2))  # * 1
print(sol.search([1, 2, 9, 10], 11))  # * -1
print(sol.search([], 20))  # * -1
print(sol.search([4, 5, 6], 20))  # * -1
print(sol.search([4, 5, 6], 4))  # * 0
print(sol.search([4, 5, 6], 5))  # * 1

# * Time: O(log n) - The search space is halved each iteration

# * Space: O(1) - The memory usage remains constant regardless of input size
