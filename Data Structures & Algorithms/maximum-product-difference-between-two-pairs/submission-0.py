class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        seen = set(nums)
        res = []
        for i in range(len(nums)):
            res.append(nums[i])
        res.sort()
        biggest = res[-1]
        secondbiggest = res[-2]
        secondsmallest = res[1]
        smallest = res[0]
        return (biggest * secondbiggest) - (secondsmallest * smallest)