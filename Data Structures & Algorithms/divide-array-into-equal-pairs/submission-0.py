class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 1:
            return False
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        for key, value in hashmap.items():
            if value % 2 == 1:
                return False
            else:
                hashmap[key] -= 2
            # if hashmap[key] == 0:
            #     del hashmap[key]
        return True
