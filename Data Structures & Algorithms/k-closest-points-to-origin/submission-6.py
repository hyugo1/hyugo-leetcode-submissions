class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for x, y in points:
            z = (x**2) + (y ** 2)
            heapq.heappush(heap, (z, (x, y)))
        res = []
        for i in range(k):
            a, b = heapq.heappop(heap)
            res.append(b)
        return res






