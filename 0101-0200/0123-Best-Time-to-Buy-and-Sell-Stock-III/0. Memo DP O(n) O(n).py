# 123. Best Time to Buy and Sell Stock III

# * Essentially the same as Leetcode 0122, except we can only sell two stocks
# * So instead of 2D DP, we have 3D DP (tracking the number of sales made)
from typing import Literal


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def solve(i: int, have: bool, sales: Literal[0, 1, 2]) -> int:
            # * Check for memoized subproblems
            if (i, have, sales) in memo:
                return memo[(i, have, sales)]

            # * Base Cases: Out of Bounds, or Out of Sales
            if i == len(prices) or sales == 2:
                return 0

            best: int = 0

            if have:
                best = max(
                    solve(i + 1, True, sales),  # * Hold
                    solve(i + 1, False, sales + 1) + prices[i],  # * Sell
                )
            else:
                best = max(
                    solve(i + 1, False, sales),  # * Don't buy
                    solve(i + 1, True, sales) - prices[i],  # * Buy
                )

            memo[(i, have, sales)] = best
            return best

        memo: dict[tuple[int, bool, int], int] = {}
        return solve(0, False, 0)


sol: Solution = Solution()
print(sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(sol.maxProfit([1, 2, 3, 4, 5]))
print(sol.maxProfit([7, 6, 4, 3, 1]))

# * Time: O(n) - There are `n` possible values for `i`, 2 possible values for `have`
# * And finally, 3 (realistically 2) possible values for `sales`
# * That gives us (n * 2 * 3) unique subproblems. However 2 and 3 are constant so they are dropped

# * Space: O(n) - Based on the above, the number of unique subproblems scales linearly
