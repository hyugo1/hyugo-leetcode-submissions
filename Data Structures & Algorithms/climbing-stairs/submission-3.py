class Solution:
    def climbStairs(self, n: int) -> int:
        # #bottom up tabulization
        
        onestepago = 1
        twostepago = 1

        for i in range(n - 1):
            temp = onestepago
            onestepago = onestepago + twostepago
            twostepago = temp
        return onestepago