class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hashmap = {}
        maxF= 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxF = max(maxF, hashmap[s[r]])

            while (r - l + 1) - maxF > k:
                hashmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res