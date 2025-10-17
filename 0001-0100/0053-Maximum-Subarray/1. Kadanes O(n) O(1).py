# 53. Maximum Subarray

# * The goal is to return the sum of the maximum subarray given an int[] input
# ! Note that the array may contain negative values
# *     - Therefore we have no guarantee that the inclusion of new elements won't decrease the sum
# * With the above knowledge, a sliding window approach is not possible
# * Sliding window approaches rely on a sliding window constraint
# *     - In our case, that would be that the inclusion of elements into the window results in a sum >= what we currently have
# *     - And conversely, the exclusion of elements would result in a sum <= what we currently have
# * Since we have potential for negative elements:
# *     - The inclusion of a negative element may decrease the sum
# *     - The exclusion of a negative element may increase the sum
# * Instead, we can try another approach - Kadane's Algorithm
# * At each index, we either start a brand new subarray (with nums[i]), or we extend the current subarray
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # * There are no elements to sum
        if len(nums) == 0:
            return 0

        curr_sum: int = nums[0]  # * The weight of our current subarray
        max_sum: int = nums[0]  # *The weight of the maximum subarray found thus far

        for i in range(1, len(nums)):
            # * Either start a new subarray or extend the current subarray with nums[i]
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


sol: Solution = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # * 6
print(sol.maxSubArray([1]))  # * 1
print(sol.maxSubArray([12, 3, 5]))  # * 20
print(sol.maxSubArray([-50]))  # * -50
print(sol.maxSubArray([5, 4, -1, 7, 8]))  # * 23

# * Time: O(n) - The time taken scales with the input size - each element is processed once

# * Space: O(1) - The memory usage remains constant regardless of input size
