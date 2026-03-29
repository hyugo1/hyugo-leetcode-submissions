class Solution:
    def minOperations(self, s: str) -> int:
        res0 = 0
        res1 = 0

        for i in range(len(s)):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            if s[i] != expected0:
                res0 += 1
            if s[i] != expected1:
                res1 += 1


        return min(res0, res1)