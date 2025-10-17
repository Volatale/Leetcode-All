# 53. Maximum Subarray

# * Simply try every possible subarray that exists
# * Then record the maximum out of all possibilities
# ! Note that the array may contain negative values
# *     - Therefore we have no guarantee that the inclusion of new elements won't decrease the sum
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # * There are no elements to sum
        if len(nums) == 0:
            return 0

        n: int = len(nums)
        max_sum: int = -(1 << 31)

        for i in range(n):
            curr_sum: int = 0

            for j in range(i, n):
                # * Add this element to the subarray
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum


sol: Solution = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # * 6
print(sol.maxSubArray([1]))  # * 1
print(sol.maxSubArray([12, 3, 5]))  # * 20
print(sol.maxSubArray([-50]))  # * -50
print(sol.maxSubArray([5, 4, -1, 7, 8]))  # * 23

# * Time: O(n^2) - We have a pair of nested loops, both of which scale with `n`

# * Space: O(1) - The memory usage remains constant regardless of input size
