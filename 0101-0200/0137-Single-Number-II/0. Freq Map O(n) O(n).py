# 137. Single Number II


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # * Frequency Map -> nums[i] : Frequency
        freq: dict[int, int] = {}

        # * Get the frequency of every element
        for i in range(len(nums)):
            freq[nums[i]] = (freq.get(nums[i]) or 1) + 1

        # * Find the element with only a single occurrence
        for key in freq:
            if freq[key] == 1:
                return key

        return -1


# * Time: O(n) - The time taken scales with the input size
# * We perform an O(n) loop over the `nums` array, then an O(k) loop over the frequency map
# * However, k <= n, so the time taken scales solely with the input size

# * Space: O(n) - There are ((n / 3) + 1) unique keys, thus the same number of iterations
