class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = (r - l)
            minheight = min(heights[l], heights[r])
            area = width * minheight
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res