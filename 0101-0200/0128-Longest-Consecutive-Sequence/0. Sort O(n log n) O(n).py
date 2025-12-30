# 128. Longest Consecutive Sequence

# * We want the length of the longest consecutive sequence
# * An important note is that adjacent duplicates do not break the sequence
# *     - They simply won't contribute to the count
# * The easiest thing to do is to sort the input such that it is monotonically non-decreasing
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # * Sort the array to ensure it is monotonically non-decreasing
        nums.sort()

        longest: int = 0
        length: int = 1

        for i in range(1, len(nums)):
            # * This element is one greater than the previous
            if nums[i] == nums[i - 1] + 1:
                length += 1
                longest = max(longest, length)
            elif nums[i] != nums[i - 1]:
                length = 1

        return max(longest, length)


sol: Solution = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # * 4
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # * 9
print(sol.longestConsecutive([1, 0, 1, 2]))  # * 3

# * Time: O(n log n) - On average, it takes O(n log n) to sort the input
# * Additionally, iterating over the array takes O(n)

# * Space: O(n) - The memory usage remains constant regardless of input size
