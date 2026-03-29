class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap = {}
        for ch in chars:
            hashmap[ch] = 1 + hashmap.get(ch, 0)
        res = 0
        for w in words:
            freq = {}
            for ch in w:
                freq[ch] = freq.get(ch, 0) + 1
            good = True
            for c in freq:
                if freq[c] > hashmap.get(c, 0):
                    good= False
                    break
            if good:
                res += len(w)
        return res
                
            