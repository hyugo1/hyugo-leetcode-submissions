class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #best subarray sum currently at index i
        res = nums[0]
        cur = 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            res = max(res, cur)
        return res

            