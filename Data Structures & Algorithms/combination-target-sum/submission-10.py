class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(nums):
                return

            dfs(i + 1, total)

            curr.append(nums[i])            
            dfs(i, total + nums[i])
            curr.pop()

        dfs(0, 0)
        return res

            
            
