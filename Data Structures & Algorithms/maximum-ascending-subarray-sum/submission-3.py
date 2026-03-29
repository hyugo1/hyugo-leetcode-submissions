class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res= nums[0]
        curSum = nums[0]
        i = 1
        while i < len(nums):
            if nums[i - 1] >= nums[i]:
                curSum = 0
            curSum += nums[i]
            res = max(curSum, res)
            i += 1
        return res