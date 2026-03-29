class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heavy = -heapq.heappop(stones)
            heavy2 = -heapq.heappop(stones)
            diff = abs(heavy - heavy2)
            if diff == 0:
                continue
            else:
                heapq.heappush(stones, -diff)
        return 0 if len(stones) == 0 else -stones[0]

