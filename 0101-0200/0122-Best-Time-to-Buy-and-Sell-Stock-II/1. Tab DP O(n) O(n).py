# 122. Best Time to Buy and Sell Stock II

# * We implicitly encode the "have" stock boolean into the two possible states
# *     - flat[i] means we were not holding a stock on day i
# *     - hold[i] means we WERE holding a stock on day i
# ! If we are NOT holding:
# *     - Either we were already flat yesterday
# *     - Or, we sell today (so we WERE holding yesterday)
# ! If we ARE holding:
# *     - Either we were already holding yesterday
# *     - Or, we buy today (so we WERE flat yesterday)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)

        flat: list[int] = [0] * n  # * Max profit if you are NOT holding a stock
        hold: list[int] = [0] * n  # * Max profit if you are holding a stock

        # * We already hold the stock (so we are technically in debt)
        hold[0] = -prices[0]

        for i in range(1, n):
            # * Either you previously held nothing, or you just sold
            flat[i] = max(flat[i - 1], hold[i - 1] + prices[i])

            # * Either you held a stock, or you previously bought
            hold[i] = max(hold[i - 1], flat[i - 1] - prices[i])

        return flat[-1]


sol: Solution = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # * 7
print(sol.maxProfit([1, 2, 3, 4, 5]))  # * 4
print(sol.maxProfit([7, 6, 4, 3, 1]))  # * 0
print(sol.maxProfit([1]))  # * 0

# * Time: O(n) - There are `n` possible values for `i` and 2 possible values for `have`
# * That gives us (2 * n) unique subproblems total

# * Space: O(n) - The memory usage scales with the number of unique subproblems
