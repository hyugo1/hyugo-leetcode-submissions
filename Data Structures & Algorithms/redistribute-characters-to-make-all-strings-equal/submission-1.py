class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hashmap = {}
        # for i in range(len(words)):
        for w in words:
            for ch in w:
                hashmap[ch] = 1 + hashmap.get(ch, 0)

        n = len(words)

        for value in hashmap.values():
            if value % n != 0:
                return False

        return True