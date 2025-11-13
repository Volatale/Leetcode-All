# 80. Remove Duplicates from Sorted Array II

# * This is a problem involving frequency
# * Specifically, each element in the (final) array can only appear twice
# * We can use a two pointers approach to retain the relative ordering of elements
# *     `left` indicates the position of the next element
# *     `right` iterates through the array and is used to find elements
# * Keep track of the number of equal consecutive elements
# *     If we find an element that is equal, count += 1
# *     Else, count = 1 (because we found a different element)
# * If count <= 2, then we can set nums[left] = nums[right]
# *     Why? Because even if `left` and `right` are the same, this assignment won't change anything
# *     And if nums[left] == nums[right + 1], the same applies
# * Every time left is used to perform an assignment, increment `left`
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n: int = len(nums)
        left: int = 1  # * Index of next element
        count: int = 1  # * Consecutive count of current element

        for right in range(1, n):
            if nums[right] == nums[right - 1]:
                count += 1  # * Increase consecutive count
            else:
                count = 1  # * Reset the count (different element)

            # * This element's inclusion doesn't violate our condition
            if count <= 2:
                nums[left] = nums[right]
                left += 1

        # * The no. of elements in the "new" array
        return left


sol: Solution = Solution()
print(sol.removeDuplicates([1, 1, 2, 2]))  # * 4
print(sol.removeDuplicates([1, 1, 1, 1, 1]))  # * 2
print(sol.removeDuplicates([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3]))  # * 6

# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
