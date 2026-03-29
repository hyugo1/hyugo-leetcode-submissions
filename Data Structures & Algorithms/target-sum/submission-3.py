class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        if not nums:
            return 0

        def dfs(i, curr):
            if i >= len(nums):
                return 1 if curr == target else 0

            if (i, curr) in memo:
                return memo[(i, curr)]

            left = dfs(i + 1, curr + nums[i])
            right = dfs(i + 1, curr - nums[i])
            total = left + right
            memo[(i, curr)] = total
            return total

        return dfs(0, 0)