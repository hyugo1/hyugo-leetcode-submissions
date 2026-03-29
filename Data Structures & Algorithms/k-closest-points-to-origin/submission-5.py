class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []


        for a, b in points:
            dist = a*a + b*b
            heap.append([dist, (a, b)])


        heapq.heapify(heap)
        res = []
        for i in range(k):
            a = heapq.heappop(heap)[1]
            res.append(a)

        return res