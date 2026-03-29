class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        frequency = []

        for num, cnt in count.items():
            frequency.append([cnt, num])

        frequency.sort()
        
        res = []
        while k > 0:
            res.append(frequency.pop()[1])
            k -= 1

        return res
