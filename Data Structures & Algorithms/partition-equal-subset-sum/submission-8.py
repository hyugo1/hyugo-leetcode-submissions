class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = set()
        dp.add(0)


        # def dfs(i, target):
        #     if i >= len(nums):
        #         return target == 0

        #     if target < 0:
        #         return False

            
        #     return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        # return dfs(0, target)

        for i in range(len(nums) -1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDp.add(t)
                nextDp.add(t + nums[i])
            dp = nextDp

        return True if target in dp else False
