# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_prof=0
        n=len(prices)
        min_prices=prices[0]
        for i in range (0,n):
            min_prices=min(min_prices,prices[i])
            max_prof=max(prices[i]-min_prices,max_prof)
        return max_prof