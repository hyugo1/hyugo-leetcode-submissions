class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        buy = prices[0]
        for p in prices:
            profit = p - buy
            if profit > 0:
                res = max(profit, res)
            else:
                buy = p

        return res