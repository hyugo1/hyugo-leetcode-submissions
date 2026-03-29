class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            lengthofstring = int(s[i:j])
            decoded = s[j+1:j + 1 + lengthofstring]
            res.append(decoded)
            i = j + 1 + lengthofstring

        return res


