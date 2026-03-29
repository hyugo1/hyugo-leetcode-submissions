class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # r = 1
        # maxsofar = 0


        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxsofar = max(profit, maxsofar)

        #     else:
        #         l = r

        #     r += 1

        # return maxsofar


        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profitsofar = sell - buy
                profit = max(profit, profitsofar)
            else:
                # if buy is bigger than sell, we found a new place to buy
                buy = sell

        return profit


            