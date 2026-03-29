class Solution:
    def rob(self, nums: List[int]) -> int:
        two_houses_ago = 0
        one_house_ago = 0

        for n in nums:
            tmp = max(n + two_houses_ago, one_house_ago)
            two_houses_ago = one_house_ago
            one_house_ago = tmp

        return one_house_ago