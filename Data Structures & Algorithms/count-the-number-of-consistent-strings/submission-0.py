class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        alw = set(allowed)
        res = 0
        for w in words:
            good = True
            print(w)
            for i in w:
                if i not in alw:
                    print(f"NOT ALLOWED {i}")
                    good = False
                    break

            if good:
                print(f"ALLOWED {w}")
                res += 1

        return res