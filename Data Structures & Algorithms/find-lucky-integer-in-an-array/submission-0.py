class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        
        for ch in arr:
            hashmap[ch] = 1 + hashmap.get(ch, 0)

        res = 0
        for key, val in hashmap.items():
            if val == key:
                res = max(res, key)
        
        return res if res else -1