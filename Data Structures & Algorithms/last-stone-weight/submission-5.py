class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        maxheap = stones
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            if x < y:
                diff = y - x
                heapq.heappush(stones, -diff)

        return -stones[0] if stones else 0

                

            