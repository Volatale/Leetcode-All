# 26. Remove Duplicates from Sorted Array

# * The goal is to return the number of unique elements in the array
# ! However, the unique elements must also be the first `k` elements (where `k` = no. of unique elements)
# * Thus, the "real" goal is move all of the unique elements to the front of the array, while retaining relative ordering
# * The easiest thing to do is track the index of where the next unique element should go
# * Ultimately, we know the current element is a duplicate if nums[i] == nums[i - 1]
# ! If that is NOT the case, then we can set nums[curr] = nums[i]
# *     - This allows us to retain the sorted ordering
# * Swapping here might not always work if there are an odd number of elements
# *     - The reason being that we technically risk losing the relative ordering of elements
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # * There are no unique elements if the array is empty
        if len(nums) == 0:
            return 0

        # * `curr` represents the index of the next unique element
        curr: int = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[curr] = nums[i]
                curr += 1

        # * `curr` now represents the number of unique elements in nums
        return curr


sol: Solution = Solution()
print(sol.removeDuplicates([1, 1, 1, 2, 3]))  # * 3
print(sol.removeDuplicates([1, 5, 9]))  # * 3
print(sol.removeDuplicates([10, 10, 10, 10]))  # * 1
print(sol.removeDuplicates([4]))  # * 1

# * Time: O(n) - The time taken scales with the input size (n)

# * Space: O(1) - The memory usage remains constant regardless of input size
