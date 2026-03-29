class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for i in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i >= n:
                return False

            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[i][target]
        return dfs(0, target)