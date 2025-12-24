# 121. Best Time to Buy and Sell Stock

# * We have to buy and sell on different days
# * It only makes sense to make a sale if we bought for less than we are selling
# * A two pointer solution is applicable here (one represents buy day and the other representing sell day)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_gains: int = 0

        left: int = 0  # * Represents the buy day
        right: int = 1  # * Represents sell day

        while right < len(prices):
            if prices[left] < prices[right]:
                # * If prices[left] < prices[right], we can make soe profit
                max_gains = max(max_gains, prices[right] - prices[left])
            else:
                # * Otherwise, all the elements between left and right are useless
                left = right

            right += 1

        return max_gains


# * Time: O(n) - We have to process every element in the input array, so the time taken scales linearly

# * Space: O(1) - The memory usage remains constant regardless of input size
