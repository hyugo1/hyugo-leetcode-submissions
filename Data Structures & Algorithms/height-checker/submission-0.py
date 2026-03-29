class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        sorted_h = sorted(heights)
        for i in range(len(heights)):
            if sorted_h[i] != heights[i]:
                res += 1
        return res