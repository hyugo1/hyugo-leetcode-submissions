class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for ch in nums:
            hashmap[ch] = 1 + hashmap.get(ch, 0)

        heap = []
        for num in hashmap.keys():
            heapq.heappush(heap, (hashmap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            a = heapq.heappop(heap)[1]
            res.append(a)
        return res
        # 1.48gb 30.2%