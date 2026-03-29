class Solution:
    def climbStairs(self, n: int) -> int:

        #bottom up tabulization

        onestep = 1
        twostep = 1

        for i in range(n - 1):
            temp = onestep
            onestep = onestep + twostep
            twostep = temp


        return onestep
