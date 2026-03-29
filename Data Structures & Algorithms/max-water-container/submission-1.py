class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        bestArea = 0

        while l < r:
            width = (r - l)
            height = min(heights[l], heights[r])
            area = width * height
            bestArea = max(area, bestArea)

            if heights[l] > heights[r]:
                r-=1
            elif heights[l] <= heights[r]:    
                l+=1


        return bestArea