class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        for ch in s:
            hashmap[ch] = 1 + hashmap.get(ch, 0)
        odd = []
        even = []
        for value in hashmap.values():
            if value % 2 == 1:
                odd.append(value)
            else:
                even.append(value)
        return max(odd) - min(even)