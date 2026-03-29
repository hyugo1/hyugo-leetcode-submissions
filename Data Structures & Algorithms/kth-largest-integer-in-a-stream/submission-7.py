class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        for n in nums:
            heapq.heappush(self.heap, n)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # heapq.heappop(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # return heapq.heappop(self.heap)
        return self.heap[0]