class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashmap = {}


        # count 
        for i in range(len(s1)):
            hashmap[s1[i]] = 1 + hashmap.get(s1[i], 0)

        window = {}
        matched = 0
        window_size = len(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] in hashmap:
                window[s2[r]] = 1 + window.get(s2[r], 0)
                if window[s2[r]] == hashmap[s2[r]]:
                    matched += 1

            
            if (r - l + 1) > window_size:
                if s2[l] in hashmap:
                    if hashmap[s2[l]] == window[s2[l]]:
                        matched -= 1
                    window[s2[l]] -= 1
                l += 1

            if matched == len(hashmap):
                return True

        return False