class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for s in s1:
            hashmap[s] = 1 + hashmap.get(s, 0)

        window_size = len(s1)
        matches = 0
        l = 0
        window = {}
        for r in range(len(s2)):
            if s2[r] in hashmap:
                window[s2[r]] = 1 + window.get(s2[r], 0)
                if window[s2[r]] == hashmap[s2[r]]:
                    matches += 1
                elif window[s2[r]] == hashmap[s2[r]] + 1:
                    matches -= 1

            if (r - l + 1) > window_size:
                if s2[l] in hashmap:
                    if window[s2[l]] == hashmap[s2[l]]:
                        matches -= 1
                    elif window[s2[l]] == hashmap[s2[l]] + 1:
                        matches += 1
                    window[s2[l]] -= 1
                l += 1

            if matches == len(hashmap):
                return True
        return False