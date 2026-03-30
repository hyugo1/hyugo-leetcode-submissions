class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = set()
        dp.add(0)
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        # memo = {}
        # def dfs(i, total):
        #     if i >= len(nums):
        #         return total == target
        #     if (i, total) in memo:
        #         return memo[(i, total)]
        #     if total == target:
        #         return True
        #     res = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)
        #     memo[(i, total)] = res
        #     return res
        # return dfs(0, 0)

        for i in range(n - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False
