class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = 0

        high = 1

        profit = 0

        while high < len(prices):

            if prices[high] - prices[low] < 0:

                low = high

            else: profit = max(profit, prices[high] - prices[low])

            high = high + 1

        return profit