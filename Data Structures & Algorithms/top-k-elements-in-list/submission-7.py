class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        # key = num, value = freq
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))

        res = []
        while k > 0:
            temp = heapq.heappop(heap)[1]
            res.append(temp)
            k -= 1

        return res
