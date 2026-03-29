class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1,
        # dp = [] * len(nums) + 1

        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue

            temp = n * curmin
            curmin = min(n, n*curmax, n*curmin)
            curmax = max(n, n*curmax, temp)
            
            res = max(res, curmin, curmax)


        return res
            

