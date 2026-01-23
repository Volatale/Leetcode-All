# 153. Find Minimum in Rotated Sorted Array

# * The array is rotated and sorted [1, n] times
# * Thus, within the array, there exists a subarray such that:
# *     - nums[i] < nums[i + 1] < ... < nums[j - 1]
# * Since we know that nums[0] < nums[2] within that array, we know nums[1] is > nums[0] and < nums[2]
# * In other words, we only need to check the "start" and "end" of the subarray to make some observations
# * Since the array is rotated and sorted, we know:
# *     - The array exhibits increasing monotonicity
# * Our goal is to find the element (and therefore the index) of the minimum element in the array
# * Thus, this is an optimization problem where our "search space" is limited to the indices (0, n-1)
# * We can use a binary search approach to take advantage of these facts
# * If nums[mid] > nums[right], then we know that in the subarray nums[mid+1:right+1], there exists the minimum element
# * Thus, we should search the right partition of the array
# * Otherwise, the minimum element has to exist on the left partition nums[left:mid]


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

            if nums[mid] > nums[right]:
                left = mid + 1  # * The minimum element exists on the right partiton
            else:
                right = mid  # * We either found the minimum element or it exists on the left somewhere

        return nums[left]


# * Time: O(log n) - The search space is halved each iteration, so the time taken scales logarithmically with respect to base 2

# * Space: O(1) - The memory usage remains constant regardless of input size
