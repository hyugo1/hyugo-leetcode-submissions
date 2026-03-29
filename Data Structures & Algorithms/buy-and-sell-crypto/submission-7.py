class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0
        res = 0
        r = 1
        while r < len(prices):
            total_prices =  prices[r] - prices[l]
            if total_prices > 0:
                res = max(res, total_prices)
            else:
                l = r
            r += 1

        return res
