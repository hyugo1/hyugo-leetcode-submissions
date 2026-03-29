class Solution:
    def rob(self, nums: List[int]) -> int:
        two_house_ago = 0
        one_house_ago = 0

        for n in nums:
            temp = max(one_house_ago, two_house_ago + n)
            two_house_ago = one_house_ago
            one_house_ago = temp

        return one_house_ago