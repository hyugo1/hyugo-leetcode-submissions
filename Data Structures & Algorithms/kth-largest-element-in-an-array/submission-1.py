class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-n for n in nums]
        # heap = list(set(nums))
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]