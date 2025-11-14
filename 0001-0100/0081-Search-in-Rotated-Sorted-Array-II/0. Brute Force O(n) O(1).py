# 81. Search in Rotated Sorted Array

# * Brute force iterate left to right and return true if we find the element
# * Return false otherwise (it doesn't exist in the array)


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # * Check each element in nums and see if it is equal to target
        for i in range(len(nums)):
            if nums[i] == target:
                return True

        return False


# * Time: O(n) - The time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
