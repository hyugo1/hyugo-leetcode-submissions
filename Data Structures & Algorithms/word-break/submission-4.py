class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        positive = 1
        negative = 1
        res = max(nums)
        for n in nums:
            if n == 0:
                positive = 1
                negative = 1
                continue

            temp = n * negative
            negative = min(n * negative, n * positive, n)
            positive = max(temp, n * positive, n)
            res = max(res, negative, positive)
        return res