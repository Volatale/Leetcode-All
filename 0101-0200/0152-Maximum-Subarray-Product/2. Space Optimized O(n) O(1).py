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
# * Additionally, for each element `x`, we need to check if "x < 0"
# *     - Why? Because if `curr_max` is positive, and `x` is negative, the product will become NEGATIVE
# *     - Conversely, if `curr_min` is negative, and `x` is negative, the product will become POSITVIE
# * The meaning / roles of both variables will be reversed
# *     - Thus, we need to pre-emptively swap the values to retain the meaning
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # * Base Case: The product of a single element is said to be the element
        if len(nums) == 1:
            return nums[0]

        # * We need both min and max because the min could become our max (-a * -b = +c)
        curr_max: int = nums[0]
        curr_min: int = nums[0]
        results: int = nums[0]

        for x in nums[1:]:
            # * The roles of max/min swapped, so swap them back
            if x < 0:
                curr_max, curr_min = curr_min, curr_max

            # * Either take nums[i] alone, or extend the subarray (for both)
            curr_max = max(x, curr_max * x)
            curr_min = min(x, curr_min * x)
            results = max(results, curr_max)

        return results


sol: Solution = Solution()
print(sol.maxProduct([2, 3, -2, 4]))  # * 6
print(sol.maxProduct([1, 2, 3, 4, 5]))  # * 120
print(sol.maxProduct([-3]))  # * -3
print(sol.maxProduct([0, 1, 0, 1, 0]))  # * 1
print(sol.maxProduct([-2, 0, -1]))  # * 0 (0 is the largest element)

# * Time: O(n) - We have to iterate over the entire input, which scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
