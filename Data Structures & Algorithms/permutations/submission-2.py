class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, cur):
            nonlocal n    
            if i == n:
                res.append(cur[:])
                return

            for j in range(n):
                if nums[j] not in cur:
                    cur.append(nums[j])
                    dfs(i + 1, cur)
                    cur.pop()

            # dfs(i + 1, cur)
        
        dfs(0, [])
        return res