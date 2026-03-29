class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shashmap = {}
        hhashmap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            shashmap[s[i]] = 1 + shashmap.get(s[i], 0)
            hhashmap[t[i]] = 1 + hhashmap.get(t[i], 0)
            
        return shashmap == hhashmap
