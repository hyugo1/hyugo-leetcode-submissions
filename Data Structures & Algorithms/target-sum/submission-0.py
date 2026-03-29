class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        def dfs(i, curr):
            if i == len(nums):
                return curr == target

            return (dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i]))

        return dfs(0, 0)