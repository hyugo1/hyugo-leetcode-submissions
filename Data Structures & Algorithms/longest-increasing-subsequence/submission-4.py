class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1] * n
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])

        # return max(dp)

        # n = len(nums)
        # dp = [[0] * (n + 1) for i in range(n + 1)]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i - 1, -2, -1): # previous number
        #         LIS = dp[i + 1][j + 1]

        #         #j == -1 means no prev element was chosen yet
        #         if j == -1 or nums[j] < nums[i]:
        #             LIS = max(LIS, 1 + dp[i + 1][i + 1]) #just picked nums[i], therefore i becomes the new "previous nums[i]"

        #         dp[i][j + 1] = LIS

        # return dp[0][0]

        n = len(nums)
        def dfs(i, prev):
            if i == n:
                return 0
            #skip
            res = dfs(i + 1, prev)
            if prev == -1 or nums[prev] < nums[i]: # take curr value
                res = max(res, 1 + dfs(i + 1, i))
            return res

        return dfs(0, -1)