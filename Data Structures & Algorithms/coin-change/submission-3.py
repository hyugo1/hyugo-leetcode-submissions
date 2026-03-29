class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0

            res = float('inf')
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))

            memo[amount] = res
            return res


        mincoins = dfs(amount)
        return mincoins if mincoins != float('inf') else -1