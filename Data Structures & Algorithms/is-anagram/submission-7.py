class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashmap = {}
        tHashmap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sHashmap[s[i]] = 1 + sHashmap.get(s[i], 0)
            tHashmap[t[i]] = 1 + tHashmap.get(t[i], 0)

        return tHashmap == sHashmap