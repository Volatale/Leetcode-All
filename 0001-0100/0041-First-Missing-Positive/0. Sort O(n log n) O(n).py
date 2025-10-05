# 41. FIrst Missing Positive

# * In the most brute force manner, we can simply sort the array and remove the duplicates
# !     - ONLY count elements that are > 0 (since we want to find the first missing POSITIVE)
# * Then, we can compare the current index and the element that "should" exist there
# * For example, imagine we have [1, 2, 3, 4]
# *     -  0  1  2  3
# *     - [1, 2, 3, 4]
# ! The following observations are true:
# *     1 should be stored at index 0
# *     2 should be stored at index 1
# *     3 should be stored at index 2
# *     4 should be stored at index 3
# * In other words, if nums[i] != i + 1, then we found the missing positive
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # * Get all of the unique elements and sort them
        nums = sorted(set([x for x in nums if x > 0]))

        # * nums[i] should store i + 1
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return i + 1

        # * The missing element doesn't exist in the input
        return len(nums) + 1


sol: Solution = Solution()
print(sol.firstMissingPositive([6, 4, 5, 1, 2]))  # * 3
print(sol.firstMissingPositive([4, 3, 2]))  # * 1
print(sol.firstMissingPositive([1, 2, 3, 4]))  # * 5
print(sol.firstMissingPositive([-1]))  # * 1
print(sol.firstMissingPositive([-1, 0]))  # * 1
print(sol.firstMissingPositive([4, 1, 3]))  # * 2

# * Time: O(n log n) - It takes O(n) for the list comprehension, followed by O(n) for the set initialization
# * Then, it takes O(n log n) to sort, followed by O(m) where `m` <= `n` to find the missing element

# * Space: O(n) - In the worst case, the list (and the set) hold `n` elements
