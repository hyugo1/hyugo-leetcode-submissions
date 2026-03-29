class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        if not height: return 0


        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                trap = maxL - height[l]
                res += trap
            else:
                r -=1
                maxR = max(maxR, height[r])
                trap = maxR - height[r]
                res += trap

        return res