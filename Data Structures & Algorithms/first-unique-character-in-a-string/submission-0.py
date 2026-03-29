class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {} # letter : index
        for ch in s:
            hashmap[ch] = 1 + hashmap.get(ch, 0)

        for i in range(len(s)):
            ch = s[i]
            if hashmap[ch] == 1:
                return i
        return -1
