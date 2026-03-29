class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHashMap = {}
        tHashMap = {}

        for i in range(len(s)):
            sHashMap[s[i]] = 1 + sHashMap.get(s[i], 0)
            tHashMap[t[i]] = 1 + tHashMap.get(t[i], 0)

        return sHashMap == tHashMap
