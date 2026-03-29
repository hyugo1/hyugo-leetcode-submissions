class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * (n + 2)
        #  for i in range(n - 1, -1, -1):
        #     dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        # return dp[0]

        #[rob1, rob2, n, n + 1]
        # rob1, rob2 = 0, 0
        # for n in nums:
        #     temp = max(rob1 + n, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        # return rob2

        n = len(nums)
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n - 1]