# 128. Longest Consecutive Sequence

# * For each element in nums, check if (nums - 1) exists in the set
# * If it DOES, then we know `num` is NOT the start of a new sequence
# *     - Thus we can safely ignore it
# * Otherwise, `num` IS the start of a new sequence
# * Now, we repeatedly expand the "window" while (val + length) exists in the set
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest: int = 0
        vals: set[int] = set(nums)

        for val in vals:
            # * If the set does NOT contain val - 1, val is the start of a new sequence
            if (val - 1) not in vals:
                length: int = 0

                # * If val + length exists in the set, we can extend the sequence
                while (val + length) in vals:
                    length += 1

                longest = max(longest, length)

        return longest


sol: Solution = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # * 4
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # * 9
print(sol.longestConsecutive([1, 0, 1, 2]))  # * 3

# * Time: O(n) - It takes O(n) to add all the elements to the set
# * Then, it takes O(n) to iterate over the elements in the set

# * Space: O(n) - The memory usage remains constant regardless of input size
