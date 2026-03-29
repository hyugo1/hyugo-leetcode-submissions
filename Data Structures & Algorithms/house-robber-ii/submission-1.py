class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        





    def helper(self, nums):
        two_ago = 0
        one_ago = 0


        for n in nums:
            temp = max(two_ago + n, one_ago)
            two_ago = one_ago
            one_ago = temp

        return one_ago