class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heap.append((dist, [x, y]))

        heapq.heapify(heap)
        res = []
        while k > 0:
            a = heapq.heappop(heap)[1]
            res.append(a)
            k -= 1

        return res
