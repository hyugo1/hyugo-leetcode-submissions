class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2freq = {}

        for n in nums2:
            num2freq[n] = 1 + num2freq.get(n, 0)
        
        res = []
        for i in range(len(nums1)):
            if nums1[i] in num2freq and nums1[i] not in res:
                res.append(nums1[i])

        return res