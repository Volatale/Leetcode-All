# 123. Best Time to Buy and Sell Stock III

# * dp[i][sales][have]. have: 0 -> not holding, 1 -> holding
# * buy1 -> Best profit after buying first stock (dp[i][0][1])
# * sell1 -> Best profit after selling first stock (dp[i][1][0])
# * buy2 -> Best profit after buying second stock (dp[i][1][1])
# * sell2 -> Best profit after selling second stock (dp[i][2][0])

# * Every transition depends only on the next "stage" of the transition
# * The order must be: buy1 -> sell1 -> buy2 -> sell2
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1: float = float("-inf")  # * Best profit after buying 1st stock
        buy2: float = buy1  # * Best profit after selling 1st stock
        sell1: float = buy1  # * Best profit after buying 2nd stock
        sell2: float = buy2  # * Best profit after selling 2nd stock

        for p in prices:
            buy1 = max(buy1, -p)  # * -p because we are LOSING money to buy the stock
            sell1 = max(sell1, buy1 + p)  # * "loss" from buy is implicit from above
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)

        return sell2


sol: Solution = Solution()
print(sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(sol.maxProfit([1, 2, 3, 4, 5]))
print(sol.maxProfit([7, 6, 4, 3, 1]))

# * Time: O(n) - We iterate over the entire input once in total (but each element is processed 4x)

# * Space: O(1) - The memory usage remains constant regardless of input size
