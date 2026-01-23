# 153. Find Minimum in Rotated Sorted Array

# * The array is sorted, so there is always an element nums[i] < nums[i - 1]
# * That element is the one we need to return


class Solution:
    def findMin(self, nums: list[int]) -> int:
        # * Find the first element that is smaller than the previous
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]

        return nums[0]


# * Time: O(n) - We iterate over the entire array, so the time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
