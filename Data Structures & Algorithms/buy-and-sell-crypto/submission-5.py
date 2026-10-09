class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while l < r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                res = max(res, profit)
            else:
                l = r # if price is dipping, new buy spot found
            r += 1
        return res