class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        for key, value in hashmap.items():
            if value > n:
                return key

        return 0


        