class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        result = r

        while l <= r:
            k = (l + r) // 2

            totaltimes = 0
            for p in piles:
                totaltimes += math.ceil(p / k)

            if totaltimes <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1


        return result



