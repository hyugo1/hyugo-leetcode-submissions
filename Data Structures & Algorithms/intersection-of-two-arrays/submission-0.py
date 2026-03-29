class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num1freq = {}
        num2freq = {}
        res = []
        for ch in nums2:
            num2freq[ch] = 1 + num2freq.get(ch, 0)
        for i in range(len(nums1)):
            if nums1[i] in num2freq and nums1[i] not in res:
                res.append(nums1[i])

        return res
