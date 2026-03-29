class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashmap = {}


        # count 
        for i in range(len(s1)):
            hashmap[s1[i]] = 1 + hashmap.get(s1[i], 0)


        window = {}
        l = 0
        matched = 0

        for r in range(len(s2)):
            c = s2[r]
            if c in hashmap:
                window[c] = 1+ window.get(c, 0)
                if window[c] == hashmap[c]:
                    matched += 1

            
            if r - l + 1 > len(s1):
                l_char = s2[l]
                if l_char in hashmap:
                    if hashmap[l_char] == window[l_char]:
                        matched -= 1
                    window[l_char] -= 1
                l+= 1

            if matched == len(hashmap):
                return True

        return False

