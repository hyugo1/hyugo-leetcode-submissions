class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = ""
        hashmap = {}
        for s in arr:
            hashmap[s] = 1 + hashmap.get(s, 0)
        for s in arr:
            if hashmap[s] == 1:
                res = hashmap[s]
                k -= 1
                if k == 0:
                    return s

        return ""