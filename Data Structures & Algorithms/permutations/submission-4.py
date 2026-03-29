class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    dfs(i + 1, curr)
                    curr.pop()

        dfs(0, [])
        return res