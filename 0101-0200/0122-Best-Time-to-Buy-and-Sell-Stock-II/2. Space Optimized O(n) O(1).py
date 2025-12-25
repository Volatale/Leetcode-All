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
        flat: int = 0  # * Max profit if you are NOT holding a stock
        hold: int = -prices[0]  # * Max profit if you are holding a stock

        for p in prices:
            # * Either we didn't sell last time, or we did and made a gain
            flat = max(flat, hold + p)

            # * Either we held our stock last time, or we bought and "lost"
            hold = max(hold, flat - p)

        return flat


sol: Solution = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # * 7
print(sol.maxProfit([1, 2, 3, 4, 5]))  # * 4
print(sol.maxProfit([7, 6, 4, 3, 1]))  # * 0
print(sol.maxProfit([1]))  # * 0

# * Time: O(n) - We process each element in the input array

# * Space: O(1) - The memory usage remains constant regardless of input size
