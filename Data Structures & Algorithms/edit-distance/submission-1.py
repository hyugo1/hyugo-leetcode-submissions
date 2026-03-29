class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[float('inf')] * (n + 1) for i in range(m + 1)]

        if not word1:
            return n
        if not word2:
            return m
            
        for i in range(m + 1):
            dp[i][n] = m - i
        
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = dp[i][j + 1]
                    remove = dp[i + 1][j]
                    replace = dp[i + 1][j + 1]
                    dp[i][j] = 1 + min(insert, remove, replace)

        return dp[0][0]