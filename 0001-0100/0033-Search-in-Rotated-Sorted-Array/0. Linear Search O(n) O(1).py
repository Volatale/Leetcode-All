# 33. Search in Rotated Sorted Array

# * In a brute force manner, we can simply search the entire array linearly
# * Eventually, we arrive at one of two possibilities:
# *     - The element (it exists within the array)
# *     - We don't find the element (it doesn't exist in the array)
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # * The array is empty, so `target` cannot possibly exist within
        if len(nums) == 0:
            return -1

        # * Linearly search every index for target
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        # * `target` does not exist within `nums`
        return -1


# * Time: O(n) - The time taken scales with the length of the input
# * In the worst case `target` does not exist within `nums`, thus we search the entire array

# * Space: O(1) - The memory usage remains constant regardless of input size
