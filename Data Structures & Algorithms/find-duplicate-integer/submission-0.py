class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        moreThanOnce = set()


        for n in nums:
            if n in moreThanOnce:
                return n
            moreThanOnce.add(n)

        return

            