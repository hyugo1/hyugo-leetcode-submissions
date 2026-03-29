class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap = {}
        for ch in chars:
            hashmap[ch] = 1 + hashmap.get(ch, 0)
        res = 0
        for w in words:
            counter = Counter(w)
            good = True
            for c in counter:
                if counter[c] > hashmap.get(c, 0):
                    good= False
                    break
            if good:
                res += len(w)
        return res
                
            