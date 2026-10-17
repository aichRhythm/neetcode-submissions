class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # select a window of dates. 2dates
        # see if profit is greater than 0
        # if not increase both pointer on the window by 1
        # if yes increase right pointer (not beyond eoa)
        # store profit in variable

        profit = 0

        left = 0

        right = 1

        while right < len(prices):
            if prices[right] - prices[left] < 0:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
            right = right + 1
        return profit