class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        res = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            res = max(res, curr)
        return res