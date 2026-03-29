class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                trap = maxL - height[l]
                res += trap

            else:
                r -= 1
                maxR = max(height[r], maxR)
                trap = maxR - height[r]
                res += trap

        return res