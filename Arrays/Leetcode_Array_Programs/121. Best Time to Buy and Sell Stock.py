class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < x:
                x = prices[i]
            profit = prices[i] - x
            if profit > max_profit:
                max_profit = profit
        return max_profit