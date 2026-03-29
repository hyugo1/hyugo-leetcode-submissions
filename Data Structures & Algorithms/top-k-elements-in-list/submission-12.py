class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for ch in nums:
            hashmap[ch] = 1 + hashmap.get(ch, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in hashmap.items():
            freq[count].append(num)

        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if k == len(res):
                    return res


        