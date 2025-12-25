# 123. Best Time to Buy and Sell Stock III

# * Essentially the same as Leetcode 0122, except we can only sell two stocks
# * So instead of 2D DP, we have 3D DP (tracking the number of sales made)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)

        # * dp[i][sales][have]; have: 0 = flat, 1 = holding
        dp: list[list[list[int]]] = [[[0] * 2 for _ in range(3)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for sales in range(3):
                # * Future sales must provide 0 profit
                if sales == 2:
                    dp[i][sales][0] = 0
                    dp[i][sales][1] = 0
                    continue

                # * Holding a stock
                dp[i][sales][1] = max(
                    dp[i + 1][sales][1],  # * Keep holding
                    dp[i + 1][sales + 1][0] + prices[i],  # * Make a sale
                )

                # * Not holding a stock
                dp[i][sales][0] = max(
                    dp[i + 1][sales][0],  # * Stay flat
                    dp[i + 1][sales][1] - prices[i],  # * Buy a stock
                )

        return dp[0][0][0]


sol: Solution = Solution()
print(sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(sol.maxProfit([1, 2, 3, 4, 5]))
print(sol.maxProfit([7, 6, 4, 3, 1]))

# * Time: O(n) - There are `n` possible values for `i`, 2 possible values for `have`
# * And finally, 3 (realistically 2) possible values for `sales`
# * That gives us (n * 2 * 3) unique subproblems. However 2 and 3 are constant so they are dropped

# * Space: O(n) - Based on the above, the number of unique subproblems scales linearly
