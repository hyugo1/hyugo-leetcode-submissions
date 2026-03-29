class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_prices:
                min_prices = p
            
            profit = p - min_prices
            max_profit = max(profit, max_profit)

        return max_profit

                