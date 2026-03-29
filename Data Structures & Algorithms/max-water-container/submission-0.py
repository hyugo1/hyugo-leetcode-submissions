class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result = 0


        while l < r:
            width = r - l
            area = min(heights[l], heights[r]) * width
            result = max(result, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        

        return result
