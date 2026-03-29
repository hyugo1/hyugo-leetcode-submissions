class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # curmin = float('inf')
        # curmax = float('-inf')
        curmin = 1
        curmax = 1
        res = max(nums)

        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            temp = n*curmin
            curmin = min(n*curmin, n*curmax, n)
            curmax = max(temp, n*curmax, n)
            res = max(res, curmin, curmax)

        return res