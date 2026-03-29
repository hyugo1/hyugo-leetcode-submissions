class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        shashmap = {}
        thashmap = {}

        for i in range(len(s)):
            shashmap[s[i]] = 1 + shashmap.get(s[i], 0)
            thashmap[t[i]] = 1 + thashmap.get(t[i], 0)

        return shashmap == thashmap
