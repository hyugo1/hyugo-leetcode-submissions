class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robbert(nums[:-1]), self.robbert(nums[1:]))



    def robbert(self, nums):
        twostepago = 0
        onestepago = 0

        for i in range(len(nums)):
            temp = max(nums[i] + twostepago, onestepago)
            twostepago = onestepago
            onestepago = temp

        return onestepago