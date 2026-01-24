# 154. Find Minimum in Rotated Sorted Array II

# * Since nums[left] == nums[mid] and nums[mid] == right, the two outer values are redundant
# * If this value does end up being the minimum, we still have access to at least one of them in the smaller subarray
# * So we can safely remove nums[left] and nums[right] from the search space without any issues:
# *     - If we have three "5" in an array, and we remove the two our ones, we still have access to the singular
# *     - 3 - 2 == 1, not 0, so we can still find the lone 3 if we really need to
# *      0  1  2  3  4
# *     [2, 2, 2, 1, 2]
# *      L     M     R

# *     [2, 2, 2, 1, 2]
# *         L  M  R

# *     [2, 2, 2, 1, 2]
# *               LR
# *


class Solution:
    def findMin(self, nums: list[int]) -> int:
        # * Base Case: The only element is the minimum
        if len(nums) == 1:
            return nums[0]

        # * Our search space is the range of indices [0, n-1]
        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            # * `mid` represents the element we "think" is the minimum
            mid: int = left + ((right - left) >> 1)

            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                # * Remove the outer elements from the search space
                left += 1
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1  # * Minimum element exists on the right partition
            else:
                right = mid  # * Min element exists on the left, or we found it

        return nums[left]


# * Time: O(n) - In the worst case, if the entire array is duplicates then we process every element

# * Space: O(1) - The memory usage remains constant reardless of input size
