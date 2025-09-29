# 34. Find First and Last Position of Element in Sorted Array


# * We can simply perform two binary searches:
# *     - The first is used to find the first occurrence of `target`
# *     - The second is used to find the last occurrence of `target`
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [self.bisect_left(nums, target), self.bisect_right(nums, target)]

    def bisect_left(self, nums: list[int], target: int) -> int:
        # * The search space is the range of indices [0, n - 1]
        left: int = 0
        right: int = len(nums) - 1
        first: int = -1

        while left < right:
            # * `mid` represents the current index we are checking
            mid: int = left + ((right - left) >> 1)

            # * Update the best
            if nums[mid] == target:
                first = mid

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return first

    def bisect_right(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        last: int = -1

        while left < right:
            mid: int = left + ((right - left) >> 1)

            # * Update the best
            if nums[mid] == target:
                last = mid

            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1

        return last


# * Time: O(log n) - We perform two binary searches on `nums`, both of which take O(log n)

# * Space: O(1) - The memory usage remains constant regardless of input size
