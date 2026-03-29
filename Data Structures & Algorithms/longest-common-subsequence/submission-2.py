class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp = [[0] * (n + 1) for i in range(m + 1)]
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # return dp[0][0]

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)

            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j +1))
            return memo[(i, j)]
        return dfs(0, 0)
