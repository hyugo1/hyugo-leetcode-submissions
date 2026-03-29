class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.robber(nums[1:]), self.robber(nums[:-1]), nums[0])

    def robber(self, nums):
        if not nums:
            return 0
        # [rob1, rob2]
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
