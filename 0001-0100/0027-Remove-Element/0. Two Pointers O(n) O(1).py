# 27. Remove Element

# * Simply put, the goal is to move all of the elements that are == val to the BACK of the array
# ! Alternatively, we can think of it as moving all of the elements != val to the FRONT of the array
# * Thus, `index` represents the place where the next element that is NOT equal to val should be placed
# * Anything to the left of index can therefore be treated as valid
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # * There are no elements that are not val
        if len(nums) == 0:
            return 0

        # * `index` represents the index of an element equal to "val", and should be swapped
        index: int = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index


sol: Solution = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))  # * 2
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # * 5
print(sol.removeElement([1, 2, 3], 4))  # * 3
print(sol.removeElement([], 10))  # * 0
print(sol.removeElement([4], 1))  # * 1
print(sol.removeElement([4], 4))  # * 0

# * Time: O(n) - The time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
