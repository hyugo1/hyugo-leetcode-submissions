class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    curr.append(s[i:j + 1])
                    dfs(j + 1)
                    curr.pop()
        dfs(0)
        return res

    def isPal(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left+= 1
            right -= 1
        return True