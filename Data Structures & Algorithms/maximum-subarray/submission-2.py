class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #best subarray sum currently at index i
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            res = max(res, dp[i])
        return res