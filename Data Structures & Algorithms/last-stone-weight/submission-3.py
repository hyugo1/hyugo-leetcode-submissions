class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        maxheap = stones
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            a = -heapq.heappop(maxheap)
            b = -heapq.heappop(maxheap)
            diff = a - b
            heapq.heappush(maxheap, -diff)
        
        return -maxheap[0]
