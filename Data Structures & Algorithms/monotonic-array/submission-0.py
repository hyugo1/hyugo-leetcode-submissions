class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        increase = decrease = True
        for i in range(1, n):
            if not (nums[i - 1] <= nums[i]):
                increase = False
            if not (nums[i - 1] >= nums[i]):
                decrease = False
        return increase or decrease