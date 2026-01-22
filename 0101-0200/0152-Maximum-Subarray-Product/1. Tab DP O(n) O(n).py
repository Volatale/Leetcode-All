# 152. Maximum Product Subarray

# * We are dealing with positives, negatives and zero, so all of these need to be considered
# * Some lemmas involving multiplication are:
# *     - a * b = +c
# *     - a * -b = -c
# *     - -a * -b = +c
# * In our case, we could just brute force using two nested for loops
# * The multiplicative identity is 1, so we take 1 as the "starting" product (so the multiplicand retains its sign)
# *     - 1 * a = a
# *     - 1 * -a = a
# ! We need to track not only the maximum subarray so far, but we also need to track the minimum subarray so far
# * Why? Because if the minimum is negative, if we find another negative, then we get (-a * -b), which gives us a positive
# *     - And it is possible that the product is greater than our current maximum
# * For example, lets say we have (6, -9), and nums[i] = -3
# *     - Then we end up with (6 * -3 == -18) and (-9 * -3 == +27)
# *     - The "minimum" we had became a positive, and ended up being larger than our previous maximum
# ! Hence we need to track both the minimum AND the maximum as we go; neither role is set in stone
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # * Base Case: The product of a single element is said to be the element
        if len(nums) == 1:
            return nums[0]

        n: int = len(nums)
        result: int = nums[0]

        # * dp[i] = Max & Min product subarray in the range nums[0:i+1]
        max_dp: list[int] = [0] * (n + 1)
        min_dp: list[int] = [0] * (n + 1)
        max_dp[n] = min_dp[n] = 1

        for i in range(n - 1, -1, -1):
            candidates: tuple[int, int, int] = (
                nums[i],  # * Try taking nums[i] alone
                nums[i] * max_dp[i + 1],  # * Try extending max subarray with nums[i]
                nums[i] * min_dp[i + 1],  # * Try extending min subarray with nums[i]
            )

            max_dp[i] = max(candidates)
            min_dp[i] = min(candidates)
            result = max(result, max_dp[i])

        return result


sol: Solution = Solution()
print(sol.maxProduct([2, 3, -2, 4]))  # * 6
print(sol.maxProduct([1, 2, 3, 4, 5]))  # * 120
print(sol.maxProduct([-3]))  # * -3
print(sol.maxProduct([0, 1, 0, 1, 0]))  # * 1
print(sol.maxProduct([-2, 0, -1]))  # * 0 (0 is the largest element)

# * Time: O(n) - We have to iterate over the entire input, which scales with the input size
# * Additionally, we create two `dp` arrays, both of which scale with `n`

# * Space: O(n) - We have to `dp` arrays that scale in size linearly with `n` (+1)
