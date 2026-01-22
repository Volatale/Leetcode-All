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


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # * Base Case: The product of a single element is said to be the element
        if len(nums) == 1:
            return nums[0]

        n: int = len(nums)
        max_product: int = -(1 << 31)

        for i in range(n):
            # * The identity element of multiplication is 1
            product: int = 1

            for j in range(i, n):
                product *= nums[j]
                max_product = max(max_product, product)

        return max_product


sol: Solution = Solution()
print(sol.maxProduct([2, 3, -2, 4]))  # * 6
print(sol.maxProduct([1, 2, 3, 4, 5]))  # * 120
print(sol.maxProduct([-3]))  # * -3
print(sol.maxProduct([0, 1, 0, 1, 0]))  # * 1
print(sol.maxProduct([-2, 0, -1]))  # * 0 (0 is the largest element)

# * Time: O(n^2) - We have a pair of nested loops both of which scale with `n`

# * Space: O(1) - The memory usage remains constant regardless of input size
