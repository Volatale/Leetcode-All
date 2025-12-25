# 122. Best Time to Buy and Sell Stock II

# * The entire array represents buy/sell points of a single stock
# * We can buy and sell the same stock multiple times
# *     - However, we can only hold the stock ONE at a time
# * In other words, if we hold the stock, we can't buy it again until we sell
# * Overall, we want the global maximum, so we make the optimal move at each step
# * If we have the stock, we have two chocies:
# *     - Hold the stock (don't sell)
# *     - Sell the stock (potentially make a gain of prices[i])
# * Otherwise, we don't have the stock, so we have two more choices:
# *     - Don't buy the stock at the current price (no loss no gain)
# *     - Buy the stock at the current price (losing prices[i] money)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def solve(i: int, have: int) -> int:
            # * Check for memoized subproblem
            if (i, have) in memo:
                return memo[(i, have)]

            # * Base Case: Out of Bounds
            if i == len(prices):
                return 0

            if have:
                best = max(
                    solve(i + 1, 1),  # * Hold
                    solve(i + 1, 0) + prices[i],  # * Sell
                )
            else:
                best = max(
                    solve(i + 1, 0),  # * Don't buy
                    solve(i + 1, 1) - prices[i],  # * Buy
                )

            memo[(i, have)] = best
            return best

        memo: dict[tuple[int, int], int] = {}
        return solve(0, 0)


sol: Solution = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # * 7
print(sol.maxProfit([1, 2, 3, 4, 5]))  # * 4
print(sol.maxProfit([7, 6, 4, 3, 1]))  # * 0
print(sol.maxProfit([1]))  # * 0

# * Time: O(n) - There are `n` possible values for `i` and 2 possible values for `have`
# * That gives us (2 * n) unique subproblems total

# * Space: O(n) - The memory usage scales with the number of unique subproblems
