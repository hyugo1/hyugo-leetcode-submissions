class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i]  == nums[j] and i < j:
        #             res += 1

        # return res
        res = 0
        hashmap = {} # number to freq
        for i in range(len(nums)):
            if nums[i] in hashmap:
                res += hashmap[nums[i]]
                hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
            else:
                hashmap[nums[i]] = 1

        return res