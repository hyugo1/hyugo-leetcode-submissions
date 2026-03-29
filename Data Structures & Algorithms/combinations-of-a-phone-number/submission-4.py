class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = { "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"}

        res = []
        if not digits:
            return []
            
        def dfs(i, curr):
            if i == len(digits):
                # res.append(curr.copy())
                res.append(''.join(curr))
                return

            for d in hashmap[digits[i]]:
                # if d not in curr:
                curr.append(d)
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res
