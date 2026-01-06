# 136. Single Number

# * We can populate a frequency map of all the elements in the input
# * Then, iterate through that frequency map and find the element that only occurs once
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # * Frequency Map: num -> frequency
        freq: dict[int, int] = {}

        # * Get the frequency of the elements in the array
        for i in range(len(nums)):
            freq[nums[i]] = (freq.get(nums[i]) or 0) + 1

        # * Find the non-duplicate (frequency of 1)
        for key in freq:
            if freq[key] == 1:
                return key

        return -1


sol: Solution = Solution()
print(sol.singleNumber([2, 2, 1]))  # * 1
print(sol.singleNumber([4, 1, 2, 1, 2]))  # * 4
print(sol.singleNumber([1]))  # * 1

# * Time: O(n) - We perform an O(n) loop over the input array, followed by an O(k) loop over the dict
# * However, k <= n, so the time taken scales with the input size

# * Space: O(n) - There are ((n / 2) + 1) unique keys, so the memory usage scales linearly
